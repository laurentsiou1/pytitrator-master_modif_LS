"""programme principal séquence de titrage
Il gère toutes les actions propres à la séquence
En lien entre les instruments et la fenêtre titration_window
"""

from PyQt5 import QtCore, QtWidgets
from datetime import datetime

from IHM import IHM
from titration_window import TitrationWindow
from windowHandler import WindowHandler

from pHmeter import *
from syringePump import *
import spectro.processing as sp

class TitrationSequence:
    
    def __init__(self, ihm:IHM, win:WindowHandler, config):
        self.ihm=ihm
        self.spectro=ihm.spectro_unit
        self.phmeter=ihm.phmeter
        self.syringe=ihm.syringe_pump
        self.pump=ihm.peristaltic_pump
        self.window_handler=win

        #Données de config
        [self.experience_name,self.description,self.OM_type,self.concentration,self.fibers,\
            self.flowcell,self.V0,self.dispense_mode,self.N_mes,self.pH_start,self.pH_end,self.saving_folder]=config
        if self.dispense_mode=='fit on 5/05/2023':
            self.target_pH_list=[4+5*k/(self.N_mes-1) for k in range(self.N_mes)]
        elif self.dispense_mode=='fixed volumes':
            #self.target_volumes_list=[10,10,20,30,50] #pour test interface
            self.target_volumes_list=[288,189,125,76,45,30,33,53,89,143,213,300] #after 11/01/2024 for 50mL
            #self.target_volumes_list=[200,100,100,50,50,100,200,200,500,1500] #before 11/01/2024 for 50mL
            #[400,200,200,100,100,200,400,400,1000,3000] #before 11/01/2024 for 100mL
            self.N_mes=len(self.target_volumes_list)+1  #bon nombre 11 #10 dispenses de base : 11 mesures
        else: #cas d'une dispense adaptée sur le pH initial. 
            self.target_pH_list=[self.pH_start+(self.pH_start-self.pH_end)*k/(self.N_mes-1) for k in range(self.N_mes)]
            self.target_acid=50

        #connexion des appareils
        #listing des appareils connectés
        print("\n\n### Lancement de la séquence de titrage automatique ###\n\n")
        
        """if self.ihm.phmeter.state=='closed':
            try:
                self.ihm.phmeter.connect()
                print("pH-meter connected\n")
            except:
                pass
        
        if self.ihm.syringe_pump.state=='closed':
            try:
                self.ihm.syringe_pump.connect()
                print("syringe pump connected\n")
            except:
                pass
        
        if self.ihm.spectro_unit.state=='closed':
            try:
                self.ihm.spectro_unit.connect()
                print("spectrometer connected\n")
            except:
                pass
        if self.ihm.peristaltic_pump.state=='closed':
            try:
                self.ihm.peristaltic_pump.connect()
                print("peristaltic pump connected\n")
            except:
                pass"""
                
        if self.spectro.state=='open':
            self.lambdas=self.spectro.wavelengths
            self.N_lambda=len(self.lambdas)
            """self.absorbance_spectra = [[1 for k in range(self.N_lambda)] for k in range(self.N_mes)]
            self.absorbance_spectra_cd = [[1 for k in range(self.N_lambda)] for k in range(self.N_mes)]"""
            self.absorbance_spectra = []
            self.absorbance_spectra_cd = [] #corrected from dilution
        else:
            self.absorbance_spectra = []
            self.absorbance_spectra_cd = [] #corrected from dilution

        #ref initial
        self.backgroundSpectrum_init=[]
        self.referenceSpectrum_init=[]
        #ref fin
        self.backgroundSpectrum_end=[]
        self.referenceSpectrum_end=[]

        #tableaux à compléter pendant la séquence. Variable locales
        self.pH_mes = [0 for k in range(self.N_mes)]
        self.absorbance_spectrum1 = None
        self.added_acid_uL = 0
        self.added_volumes = [0 for k in range(self.N_mes)]
        self.total_added_volume = 0
        self.cumulate_volumes = []
        self.dilution_factors = []
        dt=datetime.now()
        self.measure_times=[dt for k in range(self.N_mes)]
        
        #itération
        self.added_base_uL = []
        self.current_measure = 1
        
    def configure(self):
        #Normalement On doit régler le spectro avant la séquence auto. 
        #Le pH mètre est calibré manuellement aussi 
        #Le pousse seringue doit être mis sur la position zéro ? 
        #On a donc déjà des attributs qui sont open pour les sous systèmes. 
        #Devoir connecter les sous-sytèmes est un signe de non ou mauvais réglage. 

        #arrêt des timers liés à control panel. 
        # pour consacrer toute la mémoire sur la séquence
        self.ihm.timer1s.stop()
        self.ihm.timer3s.stop()

        #création de la fenêtre
        #self.window_handler.titration_window0=QtWidgets.QMainWindow()
        #self.window_handler.titration_window0.show()
        
        #graphique
        self.window = TitrationWindow()
        self.window.param_init(seq=self,ihm=self.ihm) 
        self.window.show()
        self.window_handler.titration_window1 = self.window
        #time.sleep(3)

        #actualisation sur le pH mètre
        if self.phmeter.state=='open':
            self.phmeter.voltagechannel.setOnVoltageChangeHandler(self.refresh_pH)
            self.phmeter.activateStabilityLevel()
            self.phmeter.stab_timer.timeout.connect(self.window.refresh_stability_level)
        
        #Pousses seringue
        if self.syringe.state=='open':
            if (self.syringe.base_level_uL-self.syringe.size)>=10: #uL
                self.syringe.full_refill()
            else:
                pass
            self.window.base_level_number.setText("%d uL" %self.syringe.base_level_uL)
            self.window.base_level_bar.setProperty("value", self.syringe.base_level_uL)
        else:
            pass
        
        self.window.ajout_ok.clicked.connect(self.acid_added)   #permet de déclencher la séquence auto
        #proprement dite

    def update_stab_time(self):
        self.phmeter.stab_time=self.window.stab_time.value()
    
    def update_stab_step(self):
        self.phmeter.stab_step=self.window.stab_step.value()

    def acid_added(self): #déclenchée lorsque l'on a ajouté l'acide et cliqué sur OK
        #modif et affichage volume
        vol=self.window.added_acid.value()
        self.added_acid_uL=vol
        self.added_volumes[0]=vol
        self.total_added_volume+=vol
        self.cumulate_volumes.append(self.total_added_volume)
        self.dilution_factors.append((vol+self.V0)/self.V0)
        self.window.append_vol_in_table(1,vol)

        try:
            self.phmeter.signals.stability_reached.disconnect() #disconnect s'applique sur les QObjects
            #permet de déconnecter la laison dans le cas où on clique plusieurs fois sur le bouton
        except:
            pass
        self.phmeter.signals.stability_reached.connect(self.mesure1_acid) #connection du slot mesure1_acid avec le signal stability_reached
        

    def mesure1_acid(self): 
        #la fonction s'execute une fois après un clic sur OK, lorsque le pH est stabilisé
        #print("passage dans mesure 1 acid")

        #mesure
        self.measure_times[0]=datetime.now()
        spec=self.spectro.current_absorbance_spectrum
        pH=self.phmeter.currentPH
        
        #ajout dans les tableaux
        self.absorbance_spectrum1=spec
        self.window.absorbance_spectrum1=spec
        #self.absorbance_spectra[0]=spec
        self.absorbance_spectra.append(spec)
        self.pH_mes[0]=pH
        print("pH_mes=",self.pH_mes)

        #affichage pH
        self.window.append_pH_in_table(1,pH)
        
        #graphe en delta
        self.window.current_delta_abs_curve=self.window.delta_all_abs.plot([0],[0])
        self.window.current_abs_curve=self.window.all_abs.plot([0],[0])
        #self.window.SpectraDelta=self.window.delta_all_abs.plot([0],[0])
        self.window.timer_display.timeout.connect(self.window.update_spectra) #direct

        #Lancement de la première dispense de base
        try: #On déconnecte le slot d'actualisation de valeur du pH
            self.phmeter.signals.stability_reached.disconnect() #disconnect s'applique sur les QObjects
            #permet de déconnecter la laison dans le cas où on clique plusieurs fois sur le bouton
        except:
            pass
        
        self.current_measure=2
        self.add_base() #premier ajout de base correspond à la mesure n°2
        self.phmeter.signals.stability_reached.connect(self.mesureN)
    
    #Séquence pour ajouter la base
    def add_base(self):
        N=self.current_measure
        if self.dispense_mode=='fixed volumes':
            vol=self.target_volumes_list[N-2]
            self.syringe.dispense(vol)
        elif self.dispense_mode=='fit on 5/05/2023':
            current=self.pH_mes[N-2] #lors de la mesure 1 de base, le pH est pH_mes[0]
            target=self.target_pH_list[N-1]
            vol=volumeToAdd_uL(current, target, model='fit on 5/05/2023')
            self.syringe.dispense(vol)
        
        #ajout sur le tableau
        self.added_volumes[N-1]=vol
        self.total_added_volume+=vol
        self.cumulate_volumes.append(self.total_added_volume)
        self.dilution_factors.append((self.total_added_volume+self.V0)/self.V0)
        self.window.append_vol_in_table(N,vol) #N numéro de mesure

        #niveau de la seringue
        self.window.base_level_bar.setProperty("value", self.syringe.base_level_uL)
        self.window.base_level_number.setText("%d uL" % self.syringe.base_level_uL)

        print("added_volumes=",self.added_volumes)

    #Séquence d'executions pour chaque ajout de base
    def mesureN(self):
        try: #On déconnecte le slot d'actualisation de valeur du pH
            self.phmeter.signals.stability_reached.disconnect() #le signal de stabilité 
            #de l'electrode ne pourra enclencher la fonction  
        except:
            pass
        
        #mesure
        N=self.current_measure
        self.measure_times[N-1]=datetime.now()
        spec=self.spectro.current_absorbance_spectrum
        pH=self.phmeter.currentPH
        
        #ajout dans les tableaux
        self.pH_mes[N-1]=pH
        #self.absorbance_spectra[N-1]=spec
        self.absorbance_spectra.append(spec)
        delta=[spec[k]-self.absorbance_spectrum1[k] for k in range(self.N_lambda)]

        #affichage pH
        self.window.append_pH_in_table(N,pH) #N numéro de la mesure
        time.sleep(2) #pour laisser le temps d'afficher 

        #graphe en delta
        self.window.append_abs_spectra(N,spec,delta)

        #actu des données
        self.window.append_total_vol_in_table(self.total_added_volume)  #effacer la valeur précédente
        
        #Quand on a mesuré, on passe au numéro suivant, 
        if N!=self.N_mes:
            self.current_measure+=1
            self.add_base() 
            self.phmeter.signals.stability_reached.connect(self.mesureN) #mise en attente pour mesure suivante
        else: #on est sur la dernière mesure
            #actions à réaliser à la fin du titrage
            self.createFullSequenceFiles()

    def createFullSequenceFiles(self):
        #cette fonction s'adapte à une séquence terminée ou en cours (cas d'interruption de séquence)
        #création d'un fichier compatible avec le traitement de données
        #Ainsi que d'un fichier metadata qui contient toutes les informations annexes à propos de l'expérience
        dt=datetime.now()
        date_for_file=str(dt.strftime("%m-%d-%Y_%Hh%Mmin%Ss"))
        date_txt=str(dt.strftime("%m/%d/%Y %H:%M:%S"))
        metadata = "Sequence automatique sur Pytitrator\n"\
            +"date et heure de l'enregistrement : "+date_txt+"\n\n"
        
        print("saving titration sequence data")
        print(self.pH_mes,self.absorbance_spectra)
        self.N_mes=min(len(self.pH_mes),len(self.absorbance_spectra)) #if one measure is missing

        data="measure n°\t"    #entête
        for k in range(self.N_mes):
            data+=str(k+1)+'\t'
        data+='\ttotal\n'

        if self.syringe.state=='open':
            metadata+=("Syringe Pump : "+str(self.syringe.model)+"\n"
            +"Syringe : "+str("500uL Trajan gas tight syringe\n\n"))
            data+="dispensed volumes (uL)\t"   
            print(self.N_mes,self.added_volumes,self.cumulate_volumes,self.dilution_factors)
                                                                                                           
            for k in range(self.N_mes):
                data+=str(self.added_volumes[k])+'\t'   
            data+='\t'+str(self.total_added_volume)+'\ncumulate\t'                                                                           
            for k in range(self.N_mes):
                data+=str(self.cumulate_volumes[k])+'\t'   
            data+='\ndilution factors\t'
            for k in range(self.N_mes):
                data+=str(self.dilution_factors[k])+'\t' 
            data+='\n'
        else:
            metadata+="Syringe pump not connected\n\n"    
        
        processed_formatted_data=''
        if self.phmeter.state=='open':
            metadata+=("Ph meter\nCurrent calibration data\n"+"date et heure: "+self.phmeter.CALdate+"\n"+
            "température: "+str(self.phmeter.CALtemperature)+"\n"+"nombre de points: "+str(self.phmeter.CALtype)+"\n"+
            "Tensions mesurées: U4="+str(self.phmeter.U1)+"V; U7="+str(self.phmeter.U2)+"V; U10="+str(self.phmeter.U3)+"V\n"+
            "coefficents de calibration actuels: a="+str(self.phmeter.a)+ "; b="+str(self.phmeter.b)+"\n\n")
            data+="pH\t"
            for k in range(self.N_mes):
                data+=str(self.pH_mes[k])+'\t'   
            data+='\n\nwavelengths (nm)\tabsorbance\n' 
            processed_formatted_data="\t"   #corrected from dilution
            for k in range(self.N_mes):
                processed_formatted_data+=str(self.pH_mes[k])+'\t'
            processed_formatted_data+="\n"
        else:
            metadata+="pH meter not connected\n\n"

        for k in range(self.N_mes):
            metadata+="mes"+str(k+1)+" : "+str(self.measure_times[k].strftime("%H:%M:%S"))+'\n'   
        metadata+='\n' 

        if self.spectro.state=='open':
            metadata+=("Spectrometer : "+str(self.spectro.model)+"\n"
            +"Integration time (ms) : "+str(self.spectro.t_int/1000)+"\n"
            +"Averaging : "+str(self.spectro.averaging)+"\n"
            +"Boxcar : "+str(self.spectro.boxcar)+"\n"
            +"Nonlinearity correction usage : "+str(self.spectro.device.get_nonlinearity_correction_usage())+"\n")
            if self.spectro.model!='OceanST':
                metadata+=("Electric dark correction usage : "+str(self.spectro.device.get_electric_dark_correction_usage())+"\n")
            else:
                metadata+=("Electric dark correction usage : not supported by device\n")
            metadata+="Absorbance formula : A = log10[(reference-background)/(sample-background)]\n"    
            
            #absorbance measured
            table = [self.spectro.wavelengths]+self.absorbance_spectra
            for l in range(self.spectro.N_lambda):  #spectres
                for c in range(self.N_mes):
                    #print(l,c)
                    data+=str(table[c][l])+'\t'
                data+=str(table[self.N_mes][l])+'\n'

            #absorbance corrected from dilution
            print(self.absorbance_spectra,self.dilution_factors,len(self.absorbance_spectra),len(self.dilution_factors))
            self.absorbance_spectra_cd=sp.correct_spectra_from_dilution(self.absorbance_spectra,self.dilution_factors[0:self.N_mes])
            #on ne prend que les dilutions factors pour lequels on a un spectre enregistré 
            table_formatted = [self.spectro.wavelengths]+self.absorbance_spectra_cd
            for l in range(self.spectro.N_lambda):  #spectres
                for c in range(self.N_mes):
                    processed_formatted_data+=str(table_formatted[c][l])+'\t'
                processed_formatted_data+=str(table_formatted[self.N_mes][l])+'\n'
            
            #background and reference spectra
            table2=[self.spectro.wavelengths,self.spectro.active_background_spectrum,self.spectro.active_ref_spectrum]
            metadata+="lambda(nm)\tbackground (unit count)\treference ('')\n"
            for l in range(self.spectro.N_lambda):
                for c in range(2):
                    metadata+=str(table2[c][l])+'\t'
                metadata+=str(table2[2][l])+'\n\n'
        else:
            metadata+="Spectrometer closed\n\n"
        
        output_name='test_saving_sequence'
        name_data = "seq_"+output_name+"_data_"+date_for_file
        name_metadata = "seq_"+output_name+"_metadata_"+date_for_file
        name_formatted_data = "seq_"+output_name+"_formatted_data_"+date_for_file

        f_formatted_data = open(self.saving_folder+'/'+name_formatted_data+'.txt','w')
        f_formatted_data.write(processed_formatted_data)
        f_formatted_data.close()

        f_data = open(self.saving_folder+'/'+name_data+'.txt','w') #création d'un fichier dans le répertoire
        f_data.write(data)
        f_data.close()

        f_metadata=open(self.saving_folder+'/'+name_metadata+'.txt','w')
        f_metadata.write(metadata)
        f_metadata.close()

    #DIRECT
    def refresh_pH(self,ch,voltage): #arguments immuables
        #print("pH change")
        #print("self=",self,"\nvoltage=",voltage)
        self.phmeter.currentVoltage=voltage        
        pH = volt2pH(self.phmeter.a,self.phmeter.b,voltage)
        self.phmeter.currentPH=pH #actualisation de l'attribut de la classe pHmeter
        self.window.direct_pH.display(pH)

if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    itf=IHM()
    win=WindowHandler()
    #ui.setupUi(MainWindow)
    #MainWindow.show()        
    #sys.exit(app.exec_())

    config=['nom','description','matière organique',1,'fibres','flowcell',50,'dispense mode', 10, 4, 9, "C:/Users/francois.ollitrault/Desktop"]
    sq=TitrationSequence(itf,win,config)        
    #pour visualisation du fichier de données
    sq.spectro.active_background_spectrum=[0 for k in range(sq.N_lambda)]
    sq.spectro.active_ref_spectrum=[1 for k in range(sq.N_lambda)]
    sq.cumulate_volumes=[k*100 for k in range(sq.N_mes)]
    sq.dilution_factors=[(50000+v)/50000 for v in sq.cumulate_volumes]
    #sq.absorbance_spectra_cd=sq.absorbance_spectra
    sq.absorbance_spectra_cd=sp.correct_spectra_from_dilution(sq.absorbance_spectra,sq.dilution_factors)
    print(sq.absorbance_spectra_cd,sq.absorbance_spectra)
    sq.createFullSequenceFiles()