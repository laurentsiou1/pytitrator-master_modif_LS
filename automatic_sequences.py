"""Classes des séquences de titrage
Elles gèrent toutes les actions propres aux séquences
"""

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QTimer
from datetime import datetime, timedelta

from windows.classic_sequence_window import ClassicSequenceWindow
from windows.custom_sequence_window import CustomSequenceWindow

from subsystems.pHmeter import *
from subsystems.syringePump import *
import subsystems.processing as sp

import file_manager as fm

class AutomaticSequence:
    
    DISPLAY_DELAY_MS = 5000 #for letting the screen display once the measure in taken
    ALGO_TEST_PH = [4,4.5,5,5.5,6,6.5,7,7.5,8,8.5,9,9.5,10] #pour tester l'algo

    def __init__(self, ihm):
        self.ihm=ihm
        self.spectro=ihm.spectro_unit
        self.phmeter=ihm.phmeter
        self.dispenser=ihm.dispenser
        self.pump=ihm.peristaltic_pump
    
    def update_stab_time(self):
        self.phmeter.stab_time=self.window.stab_time.value()
    
    def update_stab_step(self):
        self.phmeter.stab_step=self.window.stab_step.value()
    
    #DIRECT
    def refresh_pH(self,ch,voltage): #arguments immuables
        self.phmeter.currentVoltage=voltage        
        pH = volt2pH(self.phmeter.a,self.phmeter.b,voltage)
        self.phmeter.currentPH=pH #actualisation de l'attribut de la classe pHmeter
        self.window.direct_pH.display(pH)

class ClassicSequence(AutomaticSequence):

    MAXIMUM_DELTA_PH = 0.8  #for dispense mode 'varibale step'
    TOLERANCE_ON_FINAL_PH = 0.2 #pH.  #if pH>final_pH-gap then sequence is finished and data is saved

    def __init__(self, ihm, config):
        #super(ClassicSequence,self).__init__(self,ihm)
        self.ihm=ihm
        self.spectro=ihm.spectro_unit
        self.phmeter=ihm.phmeter
        self.syringe_B=ihm.dispenser.syringe_B
        self.pump=ihm.peristaltic_pump

        self.pause_timer = QTimer()    #for interface refreshing
        self.measure_timer = QTimer()   #chemical equilibrum and fluid circulation

        #Données de config
        [self.experience_name,self.description,self.OM_type,self.concentration,self.oxygen,self.fibers,\
        self.flowcell,self.v_init_mL,self.dispense_mode,self.N_mes,self.pH_start,self.pH_end,\
        self.fixed_delay_sec,self.mixing_delay_sec,self.saving_folder]=config

        self.delay_mes=self.fixed_delay_sec+self.mixing_delay_sec
        self.V_init = 1000*self.v_init_mL   #valeur en uL

        self.update_infos()
        print(self.infos)   #données de séquence
        
        if self.dispense_mode=='fixed step':
            self.target_pH_list=[4+5*k/(self.N_mes-1) for k in range(self.N_mes)]
        elif self.dispense_mode=='variable step':
            [self.A1,self.m1,self.lK1,self.A2,self.m2,self.lK2,self.pH0]=dispense_data.absorbance_model_26_01_2024
            self.max_delta=self.MAXIMUM_DELTA_PH
        elif self.dispense_mode=='fixed volumes':
            self.target_volumes_list=[10,10,20,30,50] #pour test interface
            self.N_mes=len(self.target_volumes_list)+1  #bon nombre 11 #10 dispenses de base : 11 mesures
        else: #cas d'une dispense adaptée sur le pH initial. 
            self.target_pH_list=[self.pH_start+(self.pH_end-self.pH_start)*k/(self.N_mes-1) for k in range(self.N_mes)]
            #print("target pH list = ", self.target_pH_list)
            self.target_acid=50

        #connexion des appareils
        print("\n\n### Lancement de la séquence de titrage automatique ###\n\n")

        if self.spectro.state=='open':
            self.lambdas=self.spectro.wavelengths
            self.N_lambda=len(self.lambdas)
        self.absorbance_spectra = []
        self.absorbance_spectra_cd = [] #corrected from dilution

        #ref initial
        self.backgroundSpectrum_init=[]
        self.referenceSpectrum_init=[]
        #ref fin
        self.backgroundSpectrum_end=[]
        self.referenceSpectrum_end=[]

        #tableaux à compléter pendant la séquence. Variable locales
        self.pH_mes=[]
        self.absorbance_spectrum1 = None
        self.added_acid_uL = 0
        self.added_base_uL = [0 for k in range(self.N_mes)]
        self.added_volumes = [0 for k in range(self.N_mes)]
        self.total_added_base_uL=0
        self.total_added_volume = 0
        self.cumulate_base_uL = []
        self.cumulate_volumes = []
        self.dilution_factors = []
        dt=datetime.now()
        self.measure_times=[]     #[dt for k in range(self.N_mes)]
        self.measure_delays=[]
        self.stability_param=[]    #liste de tuples (epsilon, dt) pour le pH-mètres
        
        #itération
        self.current_measure = 1
    
    def update_infos(self):
        self.infos="\nExperience name : "+self.experience_name+"\nDescription : ",self.description+"\nType of natural organic matter : "+self.OM_type\
        +"\nConcentration : "+str(self.concentration)+"\nPresence of oxygen : "+str(self.oxygen)+"\nFibers : "+self.fibers+"\nFlowcell : "+self.flowcell\
        +"\nDispense mode : "+self.dispense_mode+"\nInitial volume : "+str(self.V_init)+"uL"+"\nInitial pH : "+str(self.pH_start)\
        +"\nfinal pH : "+str(self.pH_end)+"\nNUmber of mesures : "+str(self.N_mes)+"\nFixed delay between measures : "+str(self.fixed_delay_sec//60)+"minutes, "+str(self.fixed_delay_sec%60)+"secondes\n\n"\
        +"Pump pause delay : "+str(self.mixing_delay_sec//60)+"minutes, "+str(self.mixing_delay_sec%60)+"secondes\n\n"+"\nTitration saving folder : "+self.saving_folder
        print(self.infos)

    def configure(self):
        #Normalement On doit régler le spectro avant la séquence auto. 
        #Le pH mètre est calibré manuellement aussi 
        #Le pousse seringue doit être mis sur la position zéro ? 
        #On a donc déjà des attributs qui sont open pour les sous systèmes. 
        #Devoir connecter les sous-sytèmes est un signe de non ou mauvais réglage. 
        
        #création de la fenêtre graphique comme attribut de ihm.
        self.ihm.openSequenceWindow('classic')
        self.window=self.ihm.sequenceWindow

        #actualisation sur le pH mètre
        if self.phmeter.state=='open':
            self.phmeter.U_pH.setOnVoltageChangeHandler(self.refresh_pH)
            self.phmeter.activateStabilityLevel()
            self.phmeter.stab_timer.timeout.connect(self.window.refresh_stability_level)
        
        #Pousses seringue
        if self.syringe_B.state=='open':
            if (self.syringe_B.level_uL-self.syringe_B.size)>=10: #uL
                self.syringe_B.full_refill()
            else:
                pass
            self.window.base_level_number.setText("%d uL" %self.syringe_B.level_uL)
            self.window.base_level_bar.setProperty("value", self.syringe_B.level_uL)
        else:
            pass
        
        self.window.ajout_ok.clicked.connect(self.acid_added)   #permet de déclencher la séquence auto
        #proprement dite
    
    def waitFixedDelay(self):
        self.pump.start()
        self.measure_timer.singleShot(1000*self.fixed_delay_sec,self.waitForPhStability)
    
    def waitForPhStability(self):
        if self.phmeter.stable==True: #cas déjà stable
            #On fait la mesure
            if self.current_measure>1:
                self.measureN()
            else:
                self.mesure1_acid()  
        else: #pas stable, mise en attente de stabilité
            #connection signal/slot
            if self.current_measure>1:
                self.phmeter.signals.stability_reached.connect(self.measureN) 
            else:
                self.phmeter.signals.stability_reached.connect(self.mesure1_acid)

    def acid_added(self): #déclenchée lorsque l'on a ajouté l'acide et cliqué sur OK
        self.acid_added_time=datetime.now()
        #modif et affichage volume
        vol=self.window.added_acid.value()
        self.added_acid_uL=vol
        self.added_base_uL[0]=0
        self.added_volumes[0]=vol
        self.total_added_base_uL+=self.added_base_uL[0]
        self.total_added_volume+=vol
        self.cumulate_base_uL.append(self.total_added_base_uL)
        self.cumulate_volumes.append(self.total_added_volume)
        self.dilution_factors.append((vol+self.V_init)/self.V_init)
        self.window.append_vol_in_table(1,vol)

        ### Connexion à la mesure 1
        try:
            self.phmeter.signals.stability_reached.disconnect() #disconnect s'applique sur les QObjects
            #permet de déconnecter la laison dans le cas où on clique plusieurs fois sur le bouton
        except:
            pass
        self.pause_timer.singleShot(1000*self.mixing_delay_sec,self.waitFixedDelay)

    def mesure1_acid(self): 
        #la fonction s'execute une fois après un clic sur OK, lorsque le pH est stabilisé

        ## 1) Mesure
        #self.measure_times[0]=datetime.now()
        dt=datetime.now()
        self.measure_times.append(dt)
        self.measure_delays.append(dt-self.acid_added_time)
        
        spec=self.spectro.current_absorbance_spectrum
        pH=self.phmeter.currentPH
        self.stability_param.append((self.phmeter.stab_step, self.phmeter.stab_time))
        
        #ajout dans les tableaux
        self.absorbance_spectrum1=spec
        self.window.absorbance_spectrum1=spec
        self.absorbance_spectra.append(spec)
        self.pH_mes.append(pH)

        #affichage pH
        self.window.append_pH_in_table(1,pH)
        
        #graphe en delta
        self.window.current_delta_abs_curve=self.window.delta_all_abs.plot([0],[0])
        self.window.current_abs_curve=self.window.all_abs.plot([0],[0])
        self.window.timer_display.timeout.connect(self.window.update_spectra) #direct
        
        #temps d'afficher à l'écran les mesures faites
        self.pause_timer.singleShot(self.DISPLAY_DELAY_MS,self.dispenseN)
    
    def dispenseN(self):
        self.current_measure+=1
        #deconnexion
        try:
            self.phmeter.signals.stability_reached.disconnect()
        except:
            pass
        self.add_base()
        self.pause_timer.singleShot(1000*self.mixing_delay_sec,self.waitFixedDelay)  
    
    #for N>=2
    def measureN(self):
        
        try: #On déconnecte le slot d'actualisation de valeur du pH
            self.phmeter.signals.stability_reached.disconnect() #le signal de stabilité 
            #de l'electrode ne pourra enclencher la fonction  
        except:
            pass

        print("passage dans measureN avec N = ", self.current_measure)
        
        #mesure
        N=self.current_measure
        dt=datetime.now()
        self.time_mes_last=dt
        self.measure_times.append(dt)
        self.measure_delays.append(dt-self.measure_times[N-2])  #N>=2
        #self.measure_times[N-1]=datetime.now()
        spec=self.spectro.current_absorbance_spectrum
        pH=self.phmeter.currentPH
        self.stability_param.append((self.phmeter.stab_step, self.phmeter.stab_time))
        
        #ajout dans les tableaux
        self.pH_mes.append(pH)
        self.absorbance_spectra.append(spec)
        delta=[spec[k]-self.absorbance_spectrum1[k] for k in range(self.N_lambda)]

        #affichage pH
        self.window.append_pH_in_table(N,pH) #N numéro de la mesure

        #graphe en delta
        self.window.append_abs_spectra(N,spec,delta)

        #actu des données
        self.window.append_total_vol_in_table(self.total_added_volume)  #effacer la valeur précédente
        
        ##Mesure suivante 
        if N!=self.N_mes and pH<=self.pH_end-self.TOLERANCE_ON_FINAL_PH:
            #temps d'affichage avant de relancer le stepper
            self.pause_timer.singleShot(self.DISPLAY_DELAY_MS,self.dispenseN)
        else: #dernière mesure
            #actions à réaliser à la fin du titrage
            fm.createFullSequenceFiles(self)    
    
    #Séquence pour ajouter la base
    def add_base(self):
        N=self.current_measure
        
        self.pump.stop()    #arrêt de la pompe pour laisser le temps de mélanger
        vol=self.dispenseFromModel(N)
        
        #ajout sur le tableau
        self.added_base_uL[N-1]=vol
        self.added_volumes[N-1]=vol
        self.total_added_base_uL+=vol
        self.total_added_volume+=vol
        self.cumulate_base_uL.append(self.total_added_base_uL)
        self.cumulate_volumes.append(self.total_added_volume)
        self.dilution_factors.append((self.total_added_volume+self.V_init)/self.V_init)

        #niveau de la seringue
        self.window.base_level_bar.setProperty("value", self.syringe_B.level_uL)
        self.window.base_level_number.setText("%d uL" % self.syringe_B.level_uL)

    def dispenseFromModel(self,N):
        if self.dispense_mode=='fixed volumes':
            vol=self.target_volumes_list[N-2]
            self.window.append_vol_in_table(N,vol) #affichage sur l'ecran avant dispense
            time.sleep(1)
            self.syringe_B.dispense(vol)  #lancement stepper
        elif self.dispense_mode=='fixed step':
            current=self.pH_mes[N-2] #lors de la mesure 1 de base, le pH est pH_mes[0]
            target=self.target_pH_list[N-1]
            n=N
            while target <= current and n<=self.N_mes-1:    #dans le cas où le pH monte trop vite accidentelement    
                target=self.target_pH_list[n]   #on remonte dans le liste des pH cibles
                n+=1
            #vol=volumeToAdd_uL(current, target, model='5th order polynomial fit on dommino 23/01/2024', oxygen=self.oxygen)
            vol=int(dispense_data.get_volume_to_dispense_uL(current,target,self.oxygen,C_NaOH=self.syringe_B.concentration,volume=self.v_init_mL))
            self.window.append_vol_in_table(N,vol) #affichage sur l'ecran avant dispense
            self.syringe_B.dispense(vol) #lancement du stepper       
        elif self.dispense_mode=='variable step':
            current=self.pH_mes[N-2]
            target=current+dispense_data.delta_pH(self.A1,self.m1,self.lK1,self.A2,self.m2,self.lK2,current,self.pH0,self.max_delta)
            #vol=volumeToAdd_uL(current, target, model='5th order polynomial fit on dommino 23/01/2024', oxygen=self.oxygen)
            vol=int(dispense_data.get_volume_to_dispense_uL(current,target,self.oxygen,C_NaOH=self.syringe_B.concentration,volume=self.v_init_mL))
            self.window.append_vol_in_table(N,vol)
            self.syringe_B.dispense(vol) #lancement du stepper 
        return vol

class CustomSequence(AutomaticSequence):    

    def __init__(self, ihm, config):
        
        # Create a QTimer object
        self.pause_timer = QTimer()    #for interface refreshing
        self.measure_timer = QTimer()   #chemical equilibrum and fluid circulation
        self.is_running=True    #flag indicating the running/pause state of sequence

        self.ihm=ihm
        self.spectro=ihm.spectro_unit
        self.phmeter=ihm.phmeter
        self.dispenser=ihm.dispenser
        self.pump=ihm.peristaltic_pump
        self.syringe_B=ihm.dispenser.syringe_B
        
        #Données de config      #comme titration sequence mais avec le fichier de config
        [self.experience_name,self.description,self.OM_type,self.concentration,self.oxygen,self.fibers,\
        self.flowcell,self.v_init_mL,self.dispense_mode,self.sequence_config_file,self.saving_folder]=config
        self.param=config
        self.V_init=int(1000*self.v_init_mL) #volumes in microliters are integers
        
        t_start=datetime.now()
        self.start_date=str(t_start.strftime("%m/%d/%Y %H:%M:%S"))
        #Récupération des données du tableau d'instructions de la séquence
        self.syringes_to_use, self.instruction_table = fm.readSequenceInstructions(self.sequence_config_file)
        self.N_mes=len(self.instruction_table)

        self.update_infos() 
        print(self.infos)   #données de séquence sur mesure

        #Données à compléter pendant la séquence
        self.pH_mes = [] #[0 for k in range(self.N_mes)]
        if self.spectro.state=='open':
            self.lambdas=self.spectro.wavelengths
            self.N_lambda=len(self.lambdas)
        self.absorbance_spectra = []
        self.absorbance_spectra_cd = [] #corrected from dilution
        self.absorbance_spectrum1 = None #première mesure de spectre
        self.added_volumes = [[0,0,0] for i in range(self.N_mes)]   #table of volumes on 3 syringes 
        self.cumulate_volume = 0
        self.cumulate_volumes = []
        self.dilution_factors = []
        self.measure_times=[]     #[dt for k in range(self.N_mes)]
        self.measure_delays=[]
        self.stability_param=[] 

    def update_infos(self):
        print(self.experience_name,self.description)
        self.infos="\nExperience name : "+self.experience_name+"\nDescription : "+self.description\
        +"\nDate and time of start : "+self.start_date+"\nType of natural organic matter : "+self.OM_type\
        +"\nConcentration : "+str(self.concentration)+"\nPresence of oxygen : "+str(self.oxygen)+"\nFibers : "+self.fibers+"\nFlowcell : "+self.flowcell\
        +"\nDispense mode : "+self.dispense_mode+"\nInitial volume : "+str(self.V_init)+"uL"\
        +"\nNumber of mesures : "+str(self.N_mes)+"\nSequence config file : "+self.sequence_config_file+"\nTitration saving folder : "+self.saving_folder

    def configure(self):
        
        #Création de la fenêtre graphique comme attribut de IHM
        self.ihm.openSequenceWindow('custom')
        self.window=self.ihm.sequenceWindow

        """#live pH
        if self.phmeter.state=='open':
            self.phmeter.U_pH.setOnVoltageChangeHandler(self.refresh_pH)
            self.phmeter.activateStabilityLevel()
            self.phmeter.stab_timer.timeout.connect(self.window.refresh_phmeter)"""
        
        #Pousses seringue
        for k in range(3):
            if self.dispenser.state[k]=='closed':
                print("syringe pump "+identifier(k)+" not ready for use")
        self.dispenser.refill_empty_syringes()     

        #verification que tous les instruments nécessaires sont connectés. 
        #Doit on avoir tous les instruments connectés pour lancer séquence ?
        #On veut pouvoir aussi lancer pour tester, quelque soit les instrucments connectés. 
        #Mais il faut savoir si un instrument nécessaire à l'éxecution n'est pas connecté.
    
    def run_sequence(self):
        self.measure_index=0
        self.pause_timer.singleShot(self.DISPLAY_DELAY_MS,self.goToNextInstruction)

    def goToNextInstruction(self):
        if self.is_running:
            self.measure_index+=1
            self.execute_instruction(self.instruction_table[self.measure_index-1])
        else:
            pass
    
    def execute_instruction(self, line):
        print("executing instruction ", self.measure_index, ":", line)
        syringe_id=line[0]  #'A' or 'B'
        dispense_type=line[1]   #'DISP_ON_PH' or 'DISP_VOL_UL'
        value=line[2]   #50uL or pH4.5 ...
        delay_stop=line[3]  #30sec
        self.delay_mes=line[4]   #300sec
        self.delay_run=self.delay_mes-delay_stop
        print("durée de pompage", self.delay_run,"seconds")
        print("delay stop =",delay_stop,"seconds")
        
        if self.pump.state=='open': #arrêt pompe
            self.pump.stop()    
        
        num=identifier(syringe_id)
        self.syringe=self.dispenser.syringes[num]
        if self.syringe.state=='open':   #dispense
            self.dispense(num,dispense_type,value)
        
        self.pause_timer.singleShot(1000*delay_stop,self.waitForMeasure) #mise en attente avant mesure

    def waitForMeasure(self):
        self.pump.start()
        self.measure_timer.singleShot(1000*(self.delay_run),self.measure)
    
    def measure(self):
        print("taking measure\n")
        N=self.measure_index
        tm=datetime.now()
        tm=tm.replace(microsecond=0)
        self.measure_times.append(tm)
        if N<1:
            dt=tm-tm
        else: #N>=1
            dt=tm-self.measure_times[N-1]
        self.measure_delays.append(dt)
        self.window.append_time_in_table(N,dt)  #time
        self.time_mes_last=tm

        if self.phmeter.state=='open':
            pH=self.phmeter.currentPH
            self.pH_mes.append(pH)  #ajout dans les tableaux
            self.stability_param.append((self.phmeter.stab_step, self.phmeter.stab_time))
            self.window.append_pH_in_table(N,pH)    #affichage
        
        if self.spectro.state=='open':
            spec=self.spectro.current_absorbance_spectrum
            if self.absorbance_spectrum1==None:
                self.absorbance_spectrum1=spec  #premier spectre
            self.absorbance_spectra.append(spec)
            delta=[spec[k]-self.absorbance_spectrum1[k] for k in range(self.N_lambda)]
            self.window.append_abs_spectra(N,spec,delta)    #ajout du spectre
        
        ##Mesure suivante
        if self.measure_index==self.N_mes: #dernière mesure
            fm.createFullSequenceFiles(self)
        else:
            self.measure_timer.singleShot(self.DISPLAY_DELAY_MS,self.goToNextInstruction)

    def dispense(self,num,dispense_type,value):
        #num : index of syringe
        if dispense_type=='DISP_ON_PH':
            target=value    #pH value
            
            #simulation pH
            """current=self.ALGO_TEST_PH[self.measure_index-1]
            vol=int(dispense_data.get_volume_to_dispense_uL(float(self.ALGO_TEST_PH[self.measure_index-1]),target,self.oxygen))
            self.syringe.dispense(int(vol/10))  #division par 10 pour rapidité"""

            #real pH
            current=self.phmeter.currentPH
            vol=int(dispense_data.get_volume_to_dispense_uL(current,target,self.oxygen,C_NaOH=self.syringe_B.concentration,volume=self.v_init_mL))    #positive or null
            self.syringe.dispense(vol)
            
            print("measure index = ",self.measure_index)  
            print("current pH = ", current)
            print("target=",target)          
            print("vol=",vol)
            
            self.window.append_vol_in_table(self.measure_index,vol)
        elif dispense_type=='DISP_VOL_UL':
            vol=int(value)
            self.syringe.dispense(vol)    #volume value
            self.window.append_vol_in_table(self.measure_index,vol)
        
        self.added_volumes[self.measure_index-1][num] = vol
        print("num=",num,"self.added_volumes=",self.added_volumes)
        self.cumulate_volume += vol
        self.cumulate_volumes.append(self.cumulate_volume)
        self.dilution_factors.append((self.cumulate_volume+self.V_init)/self.V_init)
    
    def pause_resume(self):
        if self.is_running:
            self.window.pause()
            self.pause()
        else:
            self.resume()
            self.window.resume()

    def pause(self):
        self.is_running=False
        print("sequence on pause. current instruction finishing")

    def resume(self):
        self.is_running=True
        self.pause_timer.singleShot(self.DISPLAY_DELAY_MS,self.goToNextInstruction)
        print("running again")

    def close_sequence(self):
        self.pause()
        self.pump.stop
        self.syringe.stop
        del self    #Suppression de l'objet"""

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
    sq=AutomaticSequence(itf,win,config)        
    #pour visualisation du fichier de données
    sq.spectro.active_background_spectrum=[0 for k in range(sq.N_lambda)]
    sq.spectro.active_ref_spectrum=[1 for k in range(sq.N_lambda)]
    sq.cumulate_volumes=[k*100 for k in range(sq.N_mes)]
    sq.dilution_factors=[(50000+v)/50000 for v in sq.cumulate_volumes]
    #sq.absorbance_spectra_cd=sq.absorbance_spectra
    sq.absorbance_spectra_cd=sp.correct_spectra_from_dilution(sq.absorbance_spectra,sq.dilution_factors)
    #print(sq.absorbance_spectra_cd,sq.absorbance_spectra)
    fm.createFullSequenceFiles(sq)