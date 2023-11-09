# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../panneau_de_controle.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
from IHM import IHM
from expConfig import ExpConfig
from calBox import CalBox
from spectrumConfig import SpectrumConfigWindow
from savingConfig import SavingConfig

from pHmeter import *
from spectro.absorbanceMeasure import AbsorbanceMeasure
from syringePump import *
from peristalticPump import *

from Phidget22.Devices.VoltageInput import VoltageInput
from Phidget22.Devices.DigitalInput import DigitalInput
from Phidget22.Devices.DigitalOutput import DigitalOutput
from Phidget22.Devices.Stepper import Stepper
from oceandirect.OceanDirectAPI import Spectrometer as Sp, OceanDirectAPI
from oceandirect.od_logger import od_logger


class ControlPannel(object):
    #Pour instancier la classe ControlPannel on doit renseigner un attribut PHMeter et un Spectrometer
    def __init__(self, phm: PHMeter = None, spectro_unit: AbsorbanceMeasure = None, \
               syringe_pump: SyringePump = None, peristaltic_pump: PeristalticPump = None, ihm: IHM = None):
        print("initialisation du panneau de contrôle") 
        self.ihm=ihm #ihm passé de attribut 
        
        #Mesure du pH
        if phm != None:
            self.phmeter=phm
            self.calib_text = "Current calibration data:\n"+"date: "+str(self.phmeter.CALdate)+"\n"+"temperature: "+str(self.phmeter.CALtemperature)+"°C\npH buffers: "+str(self.phmeter.CALtype)+"\nRecorded voltages:\nU4="+str(self.phmeter.U1)+"V\nU7="+str(self.phmeter.U2)+"V\nU10="+str(self.phmeter.U3)+"V\ncoefficients U=a*pH+b\na="+str(self.phmeter.a)+"\nb="+str(self.phmeter.b)
            self.wrong=0 #mauvaise calibration
        else:
            self.phmeter=None

        #spectrometry
        if spectro_unit!=None:
            self.spectro_unit=spectro_unit
        else:
            self.spectro_unit=None

        #Pousse-seringue
        if syringe_pump!=None:
            self.syringe_pump=syringe_pump
            if self.syringe_pump.getIsOpen():
                self.base_level=500-self.syringe_pump.stepper.getPosition()
        else:
            self.syringe_pump=None
        
        #Peristaltic Pump
        if peristaltic_pump!=None:
            self.peristaltic_pump=peristaltic_pump
        else:
            self.peristaltic_pump=None

    ### Méthodes pour le pH mètre
    def displayDirectPH(self,ch,voltage): #arguments immuables
        self.phmeter.currentVoltage=voltage        
        pH = volt2pH(self.phmeter.a,self.phmeter.b,voltage)
        self.phmeter.currentPH=pH #actualisation de l'attribut de la classe pHmeter
        self.direct_pH.display(pH)
        #print("voltage change")

    def openCalibWindow(self):
        self.window1 = QtWidgets.QDialog()
        self.ui1 = CalBox(self.ihm.phmeter, self, self.ihm)
        self.ui1.setupUi(self.window1)
        self.window1.show()
    
    def onCalibrationChange(self):
        self.calib_text = "Current calibration data:\n"+"date: "+str(self.phmeter.CALdate)+"\n"+"temperature: "+str(self.phmeter.CALtemperature)+"°C\npH buffers: "+str(self.phmeter.CALtype)+"\nRecorded voltages:\nU4="+str(self.phmeter.U1)+"V\nU7="+str(self.phmeter.U2)+"V\nU10="+str(self.phmeter.U3)+"V\ncoefficients U=a*pH+b\na="+str(self.phmeter.a)+"\nb="+str(self.phmeter.b)
        #print(self.phmeter.CALtype)
        self.calText.clear()
        self.calText.appendPlainText(self.calib_text)
        if self.phmeter.a==0:
            self.wrong=1
            print("Calibration erronée")

### Méthodes pour le spectromètre
    def OnClick_reglage_spectro(self):
        if self.spectro_unit==None:
            self.ihm.connectSpectrometer()
            if self.ihm.spectro_unit.state=='open':
                self.spectro_unit=self.ihm.spectro_unit
                self.activate_spectro()
        self.openSpectroWindow()

    def openSpectroWindow(self):
        self.window2 = QtWidgets.QDialog()
        self.ui2 = SpectrumConfigWindow(self.spectro_unit,self.ihm)
        self.ui2.setupUi(self.window2)
        self.window2.show()
    
    def changeShutterState(self):
        #if self.spectro_unit.state=='open':
        self.spectro_unit.changeShutterState()
        self.shutter.setChecked(not(self.spectro_unit.adv.get_enable_lamp()))

    def updateSpectrum(self):
        if self.spectro_unit.current_absorbance_spectrum!=None:
            self.directSpectrum.setData(self.lambdas,self.spectro_unit.current_absorbance_spectrum)
    
    def activate_spectro(self):
        #mise sur timer
        self.ihm.timer3s.timeout.connect(self.updateSpectrum)            
        #état réel du shutter
        self.shutter.setChecked(not(self.spectro_unit.adv.get_enable_lamp()))
        self.shutter.clicked.connect(self.changeShutterState)
        #config de l'affichage du spectre courant
        self.lambdas=self.spectro_unit.wavelengths      
        self.directSpectrum=self.direct_Abs_widget.plot([0],[0])

#Méthodes pour l'enregistrement des données et configuration des séquences
    def openConfigWindow(self):
        self.window3 = QtWidgets.QDialog()
        self.ui3 = ExpConfig()
        self.ui3.setupUi(self.window3)
        self.window3.show()
    
    def openSavingConfigWindow(self):
        self.win4 = SavingConfig(self.ihm) #l'instance de IHM est passée en attribut
        self.win4.show()

### Méthodes pour le pousse-seringue
    def set_reference_position(self):
        self.syringe_pump.setReference()
        #maj levelbar
        self.base_level=500-round(self.syringe_pump.stepper.getPosition(),0)
        self.base_level_bar.setProperty("value", self.base_level)
        self.base_level_number.setText("%d uL" % self.base_level)

    def unload_base(self): #appelée lors de l'appui sur le bouton unload base
        vol=self.unload_base_box.value()
        self.syringe_pump.simple_dispense(vol,ev=0)
        #maj levelbar
        self.base_level=500-round(self.syringe_pump.stepper.getPosition(),0)
        self.base_level_bar.setProperty("value", self.base_level)
        self.base_level_number.setText("%d uL" % self.base_level)

    def reload_base(self): #lors de l'appui sur load_base_button
        vol=self.load_base_box.value()
        self.syringe_pump.simple_refill(vol)
        #maj levelbar
        self.base_level=500-round(self.syringe_pump.stepper.getPosition(),0)
        self.base_level_bar.setProperty("value", self.base_level)
        self.base_level_number.setText("%d uL" % self.base_level)
    
    def full_reload(self):
        self.syringe_pump.full_refill()
        #maj levelbar
        self.base_level=500-round(self.syringe_pump.stepper.getPosition(),0)
        self.base_level_bar.setProperty("value", self.base_level)
        self.base_level_number.setText("%d uL" % self.base_level)
    
    #Suppose que le pousse seringue soit ouvert
    def link_SyringePump2IHM(self):
        self.base_level=500-self.syringe_pump.stepper.getPosition()
        #reference
        self.make_ref_button.clicked.connect(self.set_reference_position)
        #action buttons
        self.unload_base_button.clicked.connect(self.unload_base)
        self.reload_base_button.clicked.connect(self.reload_base)
        self.full_reload_button.clicked.connect(self.full_reload)
        self.dispense_base_button.clicked.connect(self.dispense_base)
        self.added_acid.valueChanged.connect(self.actualize_counts_on_acid_value_change)
        self.reset_added_count.clicked.connect(self.reset_volume_count)
        #Display
        self.base_level_bar.setProperty("value", self.base_level)
        self.base_level_number.setText("%d uL" % self.base_level)
        self.added_base.setText("0")

    def dispense_base(self):
        vol=self.dispense_base_box.value()
        self.syringe_pump.simple_dispense(vol) #ev=1 default
        #maj levelbar
        self.base_level=500-round(self.syringe_pump.stepper.getPosition(),0)
        self.base_level_bar.setProperty("value", self.base_level)
        self.base_level_number.setText("%d uL" % self.base_level)
        #maj volume count
        self.added_base.setText("%d" %self.syringe_pump.added_base_uL)
        self.added_total.setText("%d" %self.syringe_pump.added_total_uL)
    
    def reset_volume_count(self):
        self.syringe_pump.added_acid_uL=0
        self.syringe_pump.added_base_uL=0
        self.syringe_pump.added_total_uL=0
        self.syringe_pump.acid_dispense_log=[]
        self.syringe_pump.base_dispense_log=[]
        self.added_acid.setValue(0)
        self.added_base.setText("0")
        self.added_total.setText("0" )

    def actualize_counts_on_acid_value_change(self):
        #modification de acid et total dans la classe syringe_pump
        self.syringe_pump.added_acid_uL=self.added_acid.value()
        self.syringe_pump.added_total_uL=self.syringe_pump.added_acid_uL+self.syringe_pump.added_base_uL
        #modif de l'affichage total count
        self.added_total.setText("%d" %self.syringe_pump.added_total_uL)
        self.syringe_pump.acid_dispense_log = self.syringe_pump.added_acid_uL
    
### Méthodes pour la pompe péristaltique
    def link_pump2IHM(self):
        #print("pompe péristaltique reliée au panneau de controle")
        self.start_pump.clicked.connect(self.peristaltic_pump.start)
        self.stop_pump.clicked.connect(self.peristaltic_pump.stop)
        self.change_dir.clicked.connect(self.peristaltic_pump.change_direction)
        self.pump_speed_rpm.valueChanged.connect(self.update_pump_speed)

    def update_pump_speed(self):
        self.peristaltic_pump.setVelocity_rpm(self.pump_speed_rpm.value())

### Définition et config des widgets
    def setupUi(self, MainWindow):
        #global
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1054, 825)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #labels   
        self.pH_label = QtWidgets.QLabel(self.centralwidget)
        self.pH_label.setGeometry(QtCore.QRect(680, 80, 51, 51))
        self.pH_label.setObjectName("pH_label")
        self.abs_label = QtWidgets.QLabel(self.centralwidget)
        self.abs_label.setGeometry(QtCore.QRect(10, 10, 421, 41))
        self.abs_label.setObjectName("abs_label")
        self.stability_label = QtWidgets.QLabel(self.centralwidget)
        self.stability_label.setGeometry(QtCore.QRect(640, 30, 81, 31))
        self.stability_label.setObjectName("stability_label")
        self.last_cal_label = QtWidgets.QLabel(self.centralwidget)
        self.last_cal_label.setGeometry(QtCore.QRect(530, 130, 191, 41))
        self.last_cal_label.setObjectName("last_cal_label")

        #Ph-mètre    
        self.connect_phmeter = QtWidgets.QPushButton(self.centralwidget)
        self.connect_phmeter.setGeometry(QtCore.QRect(540, 320, 150, 51))
        self.connect_phmeter.setObjectName("connect_phmeter")
        self.connect_phmeter.clicked.connect(self.ihm.connectPHMeter)
        self.connect_phmeter.clicked.connect(self.connectPHMeter)
        self.connect_phmeter.clicked.connect(self.onCalibrationChange)
        if self.phmeter!=None:
            if self.phmeter.state=='open':
                self.phmeter.voltagechannel.setOnVoltageChangeHandler(self.displayDirectPH)
                self.direct_pH.display(self.phmeter.currentPH)
        
        self.direct_pH = QtWidgets.QLCDNumber(self.centralwidget)
        self.direct_pH.setGeometry(QtCore.QRect(730, 80, 101, 51))
        self.direct_pH.setObjectName("direct_pH")
        self.direct_pH.setNumDigits(6)
        self.stabilisation_level = QtWidgets.QProgressBar(self.centralwidget)
        self.stabilisation_level.setGeometry(QtCore.QRect(730, 30, 101, 31))
        self.stabilisation_level.setMaximum(100)
        self.stabilisation_level.setProperty("value", 15)
        self.stabilisation_level.setTextVisible(True)
        self.stabilisation_level.setOrientation(QtCore.Qt.Horizontal)
        self.stabilisation_level.setObjectName("stabilisation_level")
        self.calText = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.calText.setGeometry(QtCore.QRect(700, 170, 300, 241))
        self.calText.setSizeIncrement(QtCore.QSize(0, 0))
        self.calText.setObjectName("calText")
        #calib_text = "Données de la calibration courante:\n"+"date et heure: "+str(self.phmeter.currentCALdate)+"\n"+"température: "+str(self.phmeter.currentCALtemperature)+"\nnombre de points: "+str(self.phmeter.currentCALtype)+"\nTensions mesurées: "+str(self.phmeter.currentU1)+" "+str(self.phmeter.currentU2)+" "+str(self.phmeter.currentU3)+"coefficents de calibration actuels: a="+str(self.phmeter.current_a)+", b="+str(self.phmeter.current_b)
        try: 
            self.calText.appendPlainText(self.calib_text)
        except:
            pass
        self.cal_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.openCalibWindow())
        self.cal_button.setGeometry(QtCore.QRect(890, 50, 121, 61))
        self.cal_button.setObjectName("cal_button")

        #Spectrométrie
        self.direct_Abs_widget = pg.PlotWidget(self.centralwidget)        
        self.direct_Abs_widget.setGeometry(QtCore.QRect(10, 50, 520, 430))
        self.direct_Abs_widget.setObjectName("direct_Abs_widget")        
        self.shutter = QtWidgets.QCheckBox(self.centralwidget) #clicked = lambda: self.changeShutterState())
        self.shutter.setGeometry(QtCore.QRect(250, 500, 111, 41))
        self.shutter.setObjectName("shutter")
        self.reglage_spectro = QtWidgets.QPushButton(self.centralwidget) #, )
        self.reglage_spectro.setGeometry(QtCore.QRect(380, 500, 140, 61))
        self.reglage_spectro.setObjectName("reglage_spectro")
        self.reglage_spectro.clicked.connect(self.OnClick_reglage_spectro)

        #Syringe Pump
        self.label_base_level = QtWidgets.QLabel(self.centralwidget)
        self.label_base_level.setGeometry(QtCore.QRect(560, 420, 301, 41))
        self.label_base_level.setAutoFillBackground(False)
        self.label_base_level.setObjectName("label_base_level")
        self.base_level_number = QtWidgets.QLabel(self.centralwidget)
        self.base_level_number.setGeometry(QtCore.QRect(550, 580, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.base_level_number.setFont(font)
        self.base_level_number.setObjectName("base_level_number")
        self.unload_base_button = QtWidgets.QPushButton(self.centralwidget)
        self.unload_base_button.setGeometry(QtCore.QRect(600, 530, 71, 41))
        self.unload_base_button.setObjectName("unload_base_button")
        self.unload_base_box = QtWidgets.QSpinBox(self.centralwidget)
        self.unload_base_box.setGeometry(QtCore.QRect(680, 530, 61, 41))
        self.unload_base_box.setObjectName("unload_base_box")
        self.unload_base_box.setRange(0,450)
        self.reload_base_button = QtWidgets.QPushButton(self.centralwidget)
        self.reload_base_button.setGeometry(QtCore.QRect(600, 470, 71, 41))
        self.reload_base_button.setObjectName("reload_base_button")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(710, 600, 311, 161))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(2, 2, 2, 2)
        self.gridLayout.setObjectName("gridLayout")
        self.added_acid = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.added_acid.setObjectName("added_acid")
        self.gridLayout.addWidget(self.added_acid, 1, 2, 1, 1)
        self.added_total_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.added_total_label.setAutoFillBackground(False)
        self.added_total_label.setObjectName("added_total_label")
        self.gridLayout.addWidget(self.added_total_label, 3, 1, 1, 1)
        self.added_volume_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.added_volume_label.setAutoFillBackground(False)
        self.added_volume_label.setObjectName("added_volume_label")
        self.gridLayout.addWidget(self.added_volume_label, 0, 2, 1, 1)
        self.reset_added_count = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.reset_added_count.setObjectName("reset_added_count")
        self.gridLayout.addWidget(self.reset_added_count, 4, 2, 1, 1)
        self.added_base_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.added_base_label.setAutoFillBackground(False)
        self.added_base_label.setObjectName("added_base_label")
        self.gridLayout.addWidget(self.added_base_label, 2, 1, 1, 1)
        self.added_acid_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.added_acid_label.setAutoFillBackground(False)
        self.added_acid_label.setObjectName("added_acid_label")
        self.gridLayout.addWidget(self.added_acid_label, 1, 1, 1, 1)
        self.added_base = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.added_base.setFont(font)
        self.added_base.setObjectName("added_base")
        self.gridLayout.addWidget(self.added_base, 2, 2, 1, 1)
        self.added_total = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.added_total.setFont(font)
        self.added_total.setObjectName("added_total")
        self.gridLayout.addWidget(self.added_total, 3, 2, 1, 1)
        self.base_level_bar = QtWidgets.QProgressBar(self.centralwidget)
        self.base_level_bar.setGeometry(QtCore.QRect(550, 470, 31, 101))
        self.base_level_bar.setMinimum(50)
        self.base_level_bar.setMaximum(500)
        self.base_level_bar.setTextVisible(True)
        self.base_level_bar.setOrientation(QtCore.Qt.Vertical)
        self.base_level_bar.setObjectName("base_level_bar")
        self.make_ref_button = QtWidgets.QPushButton(self.centralwidget)
        self.make_ref_button.setGeometry(QtCore.QRect(550, 620, 121, 61))
        self.make_ref_button.setObjectName("make_ref_button")
        self.load_base_box = QtWidgets.QSpinBox(self.centralwidget)
        self.load_base_box.setGeometry(QtCore.QRect(680, 470, 61, 41))
        self.load_base_box.setObjectName("load_base_box")
        self.load_base_box.setRange(0,450)
        self.full_reload_button = QtWidgets.QPushButton(self.centralwidget)
        self.full_reload_button.setGeometry(QtCore.QRect(750, 470, 91, 41))
        self.full_reload_button.setObjectName("full_reload_button")
        self.dispense_base_button = QtWidgets.QPushButton(self.centralwidget)
        self.dispense_base_button.setGeometry(QtCore.QRect(880, 530, 141, 41))
        self.dispense_base_button.setObjectName("dispense_base_button")
        self.dispense_base_box = QtWidgets.QSpinBox(self.centralwidget)
        self.dispense_base_box.setGeometry(QtCore.QRect(810, 530, 61, 41))
        self.dispense_base_box.setObjectName("dispense_base_box")
        self.dispense_base_box.setRange(0,450)
        #connexion du pousse seringue   #2 boutons possibles
        self.full_reload_button.clicked.connect(self.connectSyringePump)        
        self.reload_base_button.clicked.connect(self.connectSyringePump)

        #Peristaltic Pump
        self.connect_pump = QtWidgets.QPushButton(self.centralwidget)
        self.connect_pump.setGeometry(QtCore.QRect(400, 570, 120, 30))
        self.connect_pump.setObjectName("connect_pump")
        #self.connect_pump.clicked.connect(self.ihm.connectPeristalticPump)
        self.connect_pump.clicked.connect(self.connectPeristalticPump)   
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(260, 560, 221, 180))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.group_peristaltic_pump = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.group_peristaltic_pump.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.group_peristaltic_pump.setContentsMargins(0, 0, 0, 0)
        self.group_peristaltic_pump.setSpacing(0)
        self.group_peristaltic_pump.setObjectName("group_peristaltic_pump")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.group_peristaltic_pump.addWidget(self.label)
        self.start_pump = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.start_pump.setObjectName("start_pump")
        self.group_peristaltic_pump.addWidget(self.start_pump)
        self.stop_pump = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.stop_pump.setObjectName("stop_pump")
        self.group_peristaltic_pump.addWidget(self.stop_pump)
        self.change_dir = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.change_dir.setObjectName("change_dir")
        self.group_peristaltic_pump.addWidget(self.change_dir)
        self.pump_speed_rpm = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.pump_speed_rpm.setAccessibleName("")
        self.pump_speed_rpm.setMaximum(240)
        self.pump_speed_rpm.setSingleStep(10)
        self.pump_speed_rpm.setProperty("value", 60)
        self.pump_speed_rpm.setObjectName("pump_speed_rpm")
        self.group_peristaltic_pump.addWidget(self.pump_speed_rpm)

        #Tous les appareils
        self.close_all = QtWidgets.QPushButton(self.centralwidget)
        self.close_all.setGeometry(QtCore.QRect(560, 700, 101, 51))
        self.close_all.setObjectName("close_all") 
        self.close_all.clicked.connect(self.ihm.close_all_devices)

        #application
        self.titration_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.openConfigWindow())
        self.titration_button.setGeometry(QtCore.QRect(20, 700, 171, 51))
        self.titration_button.setObjectName("titration_button")
        self.saving_config = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.openSavingConfigWindow())
        self.saving_config.setGeometry(QtCore.QRect(20, 520, 171, 51))
        self.saving_config.setObjectName("saving_config")
        #self.saving_config.clicked.connect()
        self.save_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.ihm.createDirectMeasureFile())
        self.save_button.setGeometry(QtCore.QRect(20, 610, 171, 51))
        self.save_button.setObjectName("save_button")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1054, 18))
        self.menubar.setObjectName("menubar")
        self.menuPanneau_de_controle = QtWidgets.QMenu(self.menubar)
        self.menuPanneau_de_controle.setObjectName("menuPanneau_de_controle")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuPanneau_de_controle.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #activation de l'actualisation de la tension
        #self.phmeter.activatePHmeter()
        #Le setOnVoltageChangeHandler ne s'applique que sur la dernière fonction renseignée
        
        if self.phmeter!=None:
            if self.phmeter.state=='open':
                self.phmeter.voltagechannel.setOnVoltageChangeHandler(self.displayDirectPH)
                self.direct_pH.display(self.phmeter.currentPH)
        
        """#création d'un timer pour le renouvellement du spectre affiché
        #il pourrait servir dans les autres fenêtres!
        self.timer3s = QtCore.QTimer()
        self.timer3s.setInterval(3000)
        self.timer3s.start()"""
        
        #spectro connecté
        if self.spectro_unit!=None:
            if self.spectro_unit.state=='open':
                self.activate_spectro()

                """#mise sur timer
                self.ihm.timer3s.timeout.connect(self.updateSpectrum)            
                #état réel du shutter
                self.shutter.setChecked(not(self.spectro_unit.adv.get_enable_lamp()))
                self.shutter.clicked.connect(self.changeShutterState)
                #config de l'affichage du spectre courant
                self.lambdas=self.spectro_unit.wavelengths      
                self.directSpectrum=self.direct_Abs_widget.plot([0],[0])"""
        
        if self.syringe_pump!=None:
            if self.syringe_pump.getIsOpen():
                self.link_SyringePump2IHM()
                """#reference
                self.make_ref_button.clicked.connect(self.set_reference_position)
                #action buttons
                self.unload_base_button.clicked.connect(self.unload_base)
                self.reload_base_button.clicked.connect(self.reload_base)
                self.full_reload_button.clicked.connect(self.full_reload)
                self.dispense_base_button.clicked.connect(self.dispense_base)
                self.added_acid.valueChanged.connect(self.actualize_counts_on_acid_value_change)
                self.reset_added_count.clicked.connect(self.reset_volume_count)
                #Display
                self.base_level_bar.setProperty("value", self.base_level)
                self.base_level_number.setText("%d uL" % self.base_level)
                self.added_base.setText("0")"""
        
        if self.peristaltic_pump!=None:
            if self.peristaltic_pump.getIsOpen():
                self.connect_pump.clicked.connect(self.link_pump2IHM)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        #pH meter
        self.connect_phmeter.setText(_translate("MainWindow", "connect pH meter"))
        self.pH_label.setText(_translate("MainWindow", "pH"))
        self.stability_label.setText(_translate("MainWindow", "stability"))
        self.stabilisation_level.setFormat(_translate("MainWindow", "%p%"))
        self.cal_button.setText(_translate("MainWindow", "calibration"))

        #spectro
        self.abs_label.setText(_translate("MainWindow", "Absorbance direct et référence"))
        self.shutter.setText(_translate("MainWindow", "shutter"))
        self.reglage_spectro.setText(_translate("MainWindow", "réglages spectro"))
        
        #pousse seringue
        self.label_base_level.setText(_translate("MainWindow", "basic syringe level (50 - 500uL)"))
        self.base_level_number.setText(_translate("MainWindow", "100 uL"))
        self.unload_base_button.setText(_translate("MainWindow", "unload"))
        self.reload_base_button.setText(_translate("MainWindow", "load"))
        self.added_total_label.setText(_translate("MainWindow", "total"))
        self.added_volume_label.setText(_translate("MainWindow", "added volume (uL)"))
        self.reset_added_count.setText(_translate("MainWindow", "Reset"))
        self.added_base_label.setText(_translate("MainWindow", "NaOH 0.1M (base)"))
        self.added_acid_label.setText(_translate("MainWindow", "HCl 0.1M (acid)"))
        self.added_base.setText(_translate("MainWindow", "55 uL"))
        self.added_total.setText(_translate("MainWindow", "0 uL"))
        self.base_level_bar.setFormat(_translate("MainWindow", "%p%"))
        self.make_ref_button.setText(_translate("MainWindow", "make reference \n"
" on full syringe"))
        self.full_reload_button.setText(_translate("MainWindow", "Full reload"))
        self.dispense_base_button.setText(_translate("MainWindow", "Dispense base (uL)"))

        #Peristaltic Pump
        self.connect_pump.setText(_translate("MainWindow", "connect pump"))
        self.label.setText(_translate("MainWindow", "Peristaltic Pump"))
        self.start_pump.setText(_translate("MainWindow", "Start"))
        self.stop_pump.setText(_translate("MainWindow", "Stop"))
        self.change_dir.setText(_translate("MainWindow", "change Direction"))

        #application
        self.titration_button.setText(_translate("MainWindow", "lancement du titrage"))
        self.saving_config.setText(_translate("MainWindow", "Configure data saving"))
        self.save_button.setText(_translate("MainWindow", "Save current measure"))
        self.close_all.setText(_translate("MainWindow","close devices"))
        self.menuPanneau_de_controle.setTitle(_translate("MainWindow", "Panneau de contrôle"))

    def connectSpectrometer(self):
        self.spectro_unit=self.ihm.spectro_unit

    def connectPHMeter(self):
        self.phmeter = self.ihm.phmeter

    def connectSyringePump(self):
        #if self.syringe_pump==None:
        self.ihm.connectSyringePump()   #création de l'object SyringePump comme attribut de IHM
        self.syringe_pump = self.ihm.syringe_pump #mise en attribut de controlPannel aussi.
        if self.syringe_pump.getIsOpen(): 
            self.link_SyringePump2IHM()

    def connectPeristalticPump(self):
        self.ihm.connectPeristalticPump()
        self.peristaltic_pump=self.ihm.peristaltic_pump
        if self.peristaltic_pump.getIsOpen():
            self.link_pump2IHM()


#Idée : lancer l'interface. Gérer l'allumage et connexion de chaque appareil sur l'interface via des boutons
if __name__ == "__main__":
    """#Interface
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    itf = IHM()
    ui = ControlPannel(ihm=itf)
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())"""

    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    itf=IHM()
    ui = ControlPannel(ihm=itf)
    ui.setupUi(MainWindow)

    MainWindow.show()        
    sys.exit(app.exec_())
        