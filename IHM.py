"""Classe IHM qui contient des attributs communs à toutes les fenêtres PyQt"""

from PyQt5 import QtCore

from configparser import ConfigParser
import os
from pathlib import Path
from datetime import datetime

from Phidget22.Phidget import *
from Phidget22.Devices.VoltageInput import *
from lib.oceandirect.OceanDirectAPI import Spectrometer as Sp, OceanDirectAPI
from lib.oceandirect.od_logger import od_logger

#Instruments
from subsystems.pHmeter import PHMeter
from subsystems.absorbanceMeasure import AbsorbanceMeasure
from subsystems.syringePump import Dispenser, PhidgetStepperPump
from subsystems.peristalticPump import PeristalticPump

#Windows
from windows.main_window import MainWindow
from windows.expConfig import ExpConfig
from windows.calBox import CalBox
from windows.custom_sequence_window import CustomSequenceWindow
from windows.spectrumConfig import SpectrumConfigWindow
from windows.savingConfig import SavingConfig
from windows.syringe_window import SyringeWindow

path = Path(__file__)
ROOT_DIR = path.parent.absolute()
#app_config_path = os.path.join(ROOT_DIR, "config\\app_config.ini")

class IHM:

    app_default_settings = os.path.join(ROOT_DIR, "config/app_default_settings.ini")
    #Sous sytèmes 
    #On créée les instances de chaque sous système ici. L'état est 'closed' par défaut
    spectro_unit=AbsorbanceMeasure()
    phmeter=PHMeter()
    dispenser=Dispenser()
    #syringe_pump=PhidgetStepperPump()
    peristaltic_pump=PeristalticPump()

    background=None
    reference=None

    #constantes de paramétrage de l'application
    #FIXED_DELAY_SEC = 75 #temps en secondes pour que le liquide parcourt l'ensemble du circuit
    #75secondes à vitesse minimale
    #MIXING_DELAY_SEC = 10 #temps de mélange pour que la solution soit homogène après un ajout

    def __init__(self):
        #Config for savings
        parser = ConfigParser()
        parser.read(self.app_default_settings)
        self.saving_folder=parser.get('saving_parameters', 'folder')
        self.save_absorbance=parser.get('saving_parameters', 'save_absorbance')   
        self.save_pH=parser.get('saving_parameters', 'save_pH')
        self.save_titration_data=parser.get('saving_parameters', 'save_titration_data')
        self.create_detailed_param_file=parser.get('saving_parameters', 'create_detailed_param_file')
        self.compatible_format=parser.get('saving_parameters', 'compatible_format')         
  
        #Configs for Automatic sequence
        self.experience_name=None
        self.description=None
        self.OM_type=None #type of organic matter
        self.concentration=None
        self.fibers=None
        self.flowcell=None
        self.N_mes=None #number of pH/spectra measures
        self.dispense_mode=parser.get('sequence', 'dispense_mode')  

        #classic
        self.initial_pH=None
        self.final_pH=None

        #custom
        self.sequence_config_file=parser.get('custom sequence', 'sequence_file') 

        #création d'un timer pour le renouvellement du pH sur calBox 
        self.timer1s = QtCore.QTimer()
        self.timer1s.setInterval(1000)
        self.timer1s.start() 
    
    def close_all_devices(self):
        print("Closing all device")
        self.timer1s.stop()

        if self.spectro_unit.state=='open':
            self.spectro_unit.close(self.spectro_unit.id)
        if self.phmeter.state=='open':
            self.phmeter.close()
        if self.syringe_pump.state=='open':
            self.syringe_pump.close()
        if self.peristaltic_pump.state=='open':
            self.peristaltic_pump.close()
              
    def updateSettings(self):
        parser = ConfigParser()
        parser.read(self.app_default_settings)
        file = open(self.app_default_settings,'r+')
        parser.set('saving_parameters', 'folder', str(self.saving_folder)) 
        parser.set('saving_parameters', 'save_absorbance', str(self.save_absorbance)) 
        parser.set('saving_parameters', 'save_pH', str(self.save_pH)) 
        parser.set('saving_parameters', 'save_titration_data', str(self.save_titration_data)) 
        parser.set('saving_parameters', 'create_detailed_param_file', str(self.create_detailed_param_file)) 
        parser.set('saving_parameters', 'compatible_format', str(self.compatible_format)) 
        parser.write(file) 
        file.close()
        print("update saving configuration")
    
    def updateSettings(self, window):
        if window=='expConfig':
            parser = ConfigParser()
            parser.read(self.app_default_settings)
            file = open(self.app_default_settings,'r+')
            parser.set('custom sequence', 'sequence_file', str(self.sequence_config_file))
            parser.set('sequence','dispense_mode',str(self.dispense_mode))
            parser.write(file)
            file.close()

    def createDirectMeasureFile(self):
        set = {}
        dt = datetime.now()
        date_text=dt.strftime("%m/%d/%Y %H:%M:%S")
        date_time=dt.strftime("%m-%d-%Y_%Hh%Mmin%Ss")
        name = "mes_"
        header = "Mesure sur Pytitrator\n"+"date et heure : "+str(date_text)+"\n\n"
        data = ""
        print("saving instant measure - ")
        if self.save_pH: #saving pH measure
            if self.phmeter.state=='open':
                name+="pH-"
                
                header+=("Données de la calibration courante\n"+"date et heure: "+self.phmeter.CALdate+"\n"+
                "température: "+str(self.phmeter.CALtemperature)+"\n"+"nombre de points: "+str(self.phmeter.CALtype)+"\n"+
                "Tensions mesurées: U4="+str(self.phmeter.U1)+"V; U7="+str(self.phmeter.U2)+"V; U10="+str(self.phmeter.U3)+"V\n"+
                "coefficents de calibration actuels: a="+str(self.phmeter.a)+ "; b="+str(self.phmeter.b)+"\n\n"
                )
                pH = self.phmeter.currentPH
                V = self.phmeter.currentVoltage
                data+="pH = "+str(pH)+"; U = "+str(V)+"V\n\n"
            else:
                header+="pH meter not connected\n\n"

        if self.save_titration_data: #saving dispensed volumes
            if self.syringe_pump.state=='open':
                name+="titr-"
                header+=("Syringe Pump : "+str(self.syringe_pump.model)+"\n"
                +"Syringe : "+str("500uL Trajan gas tight syringe\n"))
                data+=("Fluid dispense log \n"
                       +"acid : "+str(self.syringe_pump.acid_dispense_log)+"uL\n"
                       +"base : "+str(self.syringe_pump.base_dispense_log)+"uL\n"
                +"Added acid : "+str(self.syringe_pump.added_acid_uL)+"uL\n"
                +"added base : "+str(self.syringe_pump.added_base_uL)+"uL\n"
                +"total added : "+str(self.syringe_pump.added_total_uL)+"uL\n")
            else:
                header+="Syringe pump not connected\n\n"

        if self.save_absorbance: #saving absorbance
            if self.spectro_unit.state=='open':
                name+="Abs_"
                header+=("Spectrometer : "+str(self.spectro_unit.model)+"\n"
                +"Integration time (ms) : "+str(self.spectro_unit.t_int/1000)+"\n"
                +"Averaging : "+str(self.spectro_unit.averaging)+"\n"
                +"Boxcar : "+str(self.spectro_unit.boxcar)+"\n"
                +"Nonlinearity correction usage : "+str(self.spectro_unit.device.get_nonlinearity_correction_usage())+"\n")
                if self.spectro_unit.model!='OceanST':
                    header+=("Electric dark correction usage : "+str(self.spectro_unit.device.get_electric_dark_correction_usage())+"\n")
                else:
                    header+=("Electric dark correction usage : not supported by device\n")
                header+="Absorbance formula : A = log10[(reference-background)/(sample-background)]\n"    

                background = self.spectro_unit.active_background_spectrum
                ref = self.spectro_unit.active_ref_spectrum
                sample = self.spectro_unit.current_intensity_spectrum
                absorbance = self.spectro_unit.current_absorbance_spectrum
                wl = self.spectro_unit.wavelengths
                spectra=[wl,background,ref,sample,absorbance]
                Nc=len(spectra)-1
                if background==None or ref==None: #pas de calcul d'absorbance possible
                    data+="lambda(nm)\tsample (unit count)\n"
                    for l in range(self.spectro_unit.N_lambda):
                        data+=str(spectra[0][l])+'\t'
                        data+=str(spectra[3][l])+'\n'
                else:
                    data+="lambda(nm)\tbackground (unit count)\treference ('')\tsample ('')\tabsorbance (abs unit)\n"
                    for l in range(self.spectro_unit.N_lambda):
                        for c in range(Nc):
                            data+=str(spectra[c][l])+'\t'
                        data+=str(spectra[Nc][l])+'\n'
            else:
                header+="Spectrometer closed\n"

        name+=str(date_time)
        output=header+"\n\n"+data
        f_out = open(self.saving_folder+'/'+name+'.txt','w') #création d'un fichier dans le répertoire
        f_out.write(output)
        f_out.close()    
    

    ### Gestionnaire des fenêtres ###

    def openControlPanel(self):
        self.controlPanel=MainWindow(self)
        self.controlPanel.show()

    def openSavingConfigWindow(self):
        self.win1 = SavingConfig(self)
        self.win1.show()

    def openConfigWindow(self):
        self.expConfig = ExpConfig(self)
        self.expConfig.show()

    def openSpectroWindow(self):
        self.spectroWindow = SpectrumConfigWindow(self)
        self.spectroWindow.show()

    def openCalibWindow(self):
        self.calib_window = CalBox(self)
        self.calib_window.show()

    def openSyringePanel(self):
        self.syringePanel = SyringeWindow(self)
        self.syringePanel.show()

if __name__=="main":
    interface = IHM()
    print(interface.saving_folder)