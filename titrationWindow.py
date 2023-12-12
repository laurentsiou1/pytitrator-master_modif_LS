from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg
from spectrumConfig import SpectrumConfigWindow
import numpy as np

from IHM import IHM

class TitrationWindow(object):
    
    def __init__(self, ihm : IHM):
        self.ihm=ihm
        self.titration_sequence=ihm.titration_sequence

        self.spectro_unit=ihm.spectro_unit
        self.phmeter=ihm.phmeter
        self.peristaltic_pump=ihm.peristaltic_pump
        self.syringe_pump=ihm.syringe_pump

        self.lambdas=self.spectro_unit.wavelengths 
        self.N_lambda=len(self.lambdas)   
        self.N_mes=self.titration_sequence.N_mes

        #timer pour renouvellement de l'affichage
        self.timer_display = QtCore.QTimer()
        self.timer_display.setInterval(1000) #10 secondes
        self.timer_display.start()


    
    #DIRECT
    def refresh_stability_level(self):
        self.stabilisation_level.setProperty("value", self.phmeter.stab_purcent)
        self.label_stability.setText(str(self.phmeter.stab_purcent)+"%")

    def refreshDirectSpectrum(self):
        if self.spectro_unit.current_absorbance_spectrum!=None:
            self.directSpectrum.setData(self.lambdas,self.spectro_unit.current_absorbance_spectrum)

    #spectre courant sur le graphe en delta 
    def updateCurrentSpectrum_delta(self): #il y a déjà un spectre enregistré
        if self.spectro_unit.current_absorbance_spectrum!=None:
            #le spectre en delta est une donnée graphique, pas une donnée fondamentale
            self.current_absorbance_spectrum_delta=[self.spectro_unit.current_absorbance_spectrum[k]-self.titration_sequence.absorbance_spectrum1[k] for k in range(self.N_lambda)]
            self.current_delta_abs_curve.setData(self.lambdas,self.current_absorbance_spectrum_delta)
            print("update current spectra",np.shape(self.lambdas),np.shape(self.current_absorbance_spectrum_delta))
            #superposition sur le graphe, voir spectrumconfig pour les couleurs

    #ENREGISTREMENT

    #Spectres en delta
    def append_spectra_in_delta(self):
        self.spectra_j=self.delta_all_abs.plot(self.lambdas,self.spectro_unit.current_absorbance_spectrum)
    
    def append_vol_in_table(self,nb,vol): #nb numero de mesure 1 à Nmes
        self.table_vol_pH[0][nb-1].setObjectName("vol"+str(nb))
        self.grid_all_pH_vol.addWidget(self.table_vol_pH[0][nb-1], 1, nb, 1, 1)
        self.table_vol_pH[0][nb-1].clear()
        self.table_vol_pH[0][nb-1].setText(str(vol))
    
    #pH et volume
    def append_pH_in_table(self,nb,pH): #nb=numero de la mesure 1 à Nmes
        self.table_vol_pH[1][nb-1].setObjectName("pH"+str(nb))
        self.grid_all_pH_vol.addWidget(self.table_vol_pH[1][nb-1], 2, nb, 1, 1)
        self.table_vol_pH[1][nb-1].clear()
        self.table_vol_pH[1][nb-1].setText(str(pH))

    def append_total_vol_in_table(self,tot):
        #self.total_volume.
        self.grid_all_pH_vol.addWidget(self.table_vol_pH[0][self.N_mes], 1, self.N_mes+1, 1, 1)
        self.total_volume.clear()
        self.total_volume.setText(str(tot))
    
    #INITIALISATION
    def param_init(self):

        #Paramètres d'expérience
        self.experiment_parameters.setPlainText("\nNom de l'expérience : "+str(self.titration_sequence.experience_name)\
        +"\nDescription : "+str(self.titration_sequence.description)\
        +"\nType de matière organique : "+str(self.titration_sequence.OM_type)\
        +"\nConcentration : "+str(self.titration_sequence.concentration)\
        +"\nFibres : "+str(self.titration_sequence.fibers)\
        +"\nFlowcell : "+str(self.titration_sequence.flowcell)\
        +"\nDispense mode : "+str(self.titration_sequence.dispense_mode)\
        +"\nNombre de mesures : "+str(self.titration_sequence.N_mes)\
        +"\npH initial : "+str(self.titration_sequence.pH_start)\
        +"\npH final : "+str(self.titration_sequence.pH_end))

        #Spectro


        #tableau pH,volume
        self.grid_all_pH_vol.addWidget(self.label_total_volume, 0, self.N_mes+1, 1, 1)
        self.grid_all_pH_vol.addWidget(self.total_volume, 1, self.N_mes+1, 1, 1)  
        
        #tableau de données QLabels à compléter au fil de l'expérience
        self.table_vol_pH=[[QtWidgets.QLabel(self.grid0) for k in range(self.N_mes+1)], \
                         [QtWidgets.QLabel(self.grid0) for k in range(self.N_mes)]]
        
        for j in range(1,self.N_mes+1): #1ère ligne : numeros de mesures
            #mes_j="mes"+str(j)
            self.mes_j = QtWidgets.QLabel(self.grid0)
            #self.mes_j.setObjectName(mes_j)
            self.grid_all_pH_vol.addWidget(self.mes_j, 0, j, 1, 1)
            self.mes_j.setText(str(j))

        #pompe
        self.pump_speed_rpm.setProperty("value", 60.0)
    
    #configuration du spectro
    def openSpectroWindow(self):
        self.window2 = QtWidgets.QDialog()
        self.ui2 = SpectrumConfigWindow(self.spectro_unit,self.ihm)
        self.ui2.setupUi(self.window2)
        self.window2.show()

    def graphical_setup(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1759, 932)
        MainWindow.setTabletTracking(False)
        MainWindow.setIconSize(QtCore.QSize(18, 27))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #Experiment parameters
        self.experiment_parameters = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.experiment_parameters.setGeometry(QtCore.QRect(320, 460, 291, 411))
        self.experiment_parameters.setObjectName("experiment_parameters")
        
        #pH-meter
        self.direct_pH = QtWidgets.QLCDNumber(self.centralwidget)
        self.direct_pH.setGeometry(QtCore.QRect(30, 480, 101, 41))
        self.direct_pH.setObjectName("direct_pH")
        self.stabilisation_level = QtWidgets.QProgressBar(self.centralwidget)
        self.stabilisation_level.setGeometry(QtCore.QRect(170, 480, 101, 41))
        self.stabilisation_level.setMaximum(100)
        self.stabilisation_level.setProperty("value", 15)
        self.stabilisation_level.setTextVisible(False)
        self.stabilisation_level.setOrientation(QtCore.Qt.Horizontal)
        self.stabilisation_level.setObjectName("stabilisation_level")
        self.label_pH = QtWidgets.QLabel(self.centralwidget)
        self.label_pH.setGeometry(QtCore.QRect(50, 440, 61, 41))
        self.label_pH.setObjectName("label_pH")        
        self.label_stability = QtWidgets.QLabel(self.centralwidget)
        self.label_stability.setGeometry(QtCore.QRect(190, 440, 71, 41))
        self.label_stability.setObjectName("label_stability")

        #Spectro
        self.direct_abs = pg.PlotWidget(self.centralwidget)
        self.direct_abs.setGeometry(QtCore.QRect(10, 70, 601, 351))
        self.direct_abs.setObjectName("direct_abs")
        self.label_direct_abs = QtWidgets.QLabel(self.centralwidget)
        self.label_direct_abs.setGeometry(QtCore.QRect(10, 10, 171, 41))
        self.label_direct_abs.setObjectName("label_direct_abs")
        self.background_and_reference = QtWidgets.QPushButton(self.centralwidget)
        self.background_and_reference.setGeometry(QtCore.QRect(330, 20, 201, 41))
        self.background_and_reference.setObjectName("background_and_reference")
        self.background_and_reference.clicked.connect(self.openSpectroWindow)
        self.delta_all_abs = pg.PlotWidget(self.centralwidget)
        self.delta_all_abs.setGeometry(QtCore.QRect(650, 50, 1081, 701))
        self.delta_all_abs.setObjectName("delta_all_abs")
        self.current_delta_abs_curve=self.delta_all_abs.plot([0],[0]) 
        self.label_delta_abs = QtWidgets.QLabel(self.centralwidget)
        self.label_delta_abs.setGeometry(QtCore.QRect(650, 10, 371, 41))
        self.label_delta_abs.setObjectName("label_delta_abs")

        #spectre en direct
        #Display current spectrum
        self.directSpectrum=self.direct_abs.plot([0],[0])
        self.timer_display.timeout.connect(self.refreshDirectSpectrum) #abs in direct
        
        #graphe en delta
        self.SpectraDelta=self.delta_all_abs.plot([0],[0])
        
        #Dispense
        self.added_acid_label = QtWidgets.QLabel(self.centralwidget)
        self.added_acid_label.setGeometry(QtCore.QRect(70, 550, 211, 41))
        self.added_acid_label.setAutoFillBackground(False)
        self.added_acid_label.setObjectName("added_acid_label")
        self.added_acid = QtWidgets.QSpinBox(self.centralwidget)
        self.added_acid.setGeometry(QtCore.QRect(70, 590, 61, 41))
        self.added_acid.setObjectName("added_acid")
        self.ajout_ok = QtWidgets.QPushButton(self.centralwidget)
        self.ajout_ok.setGeometry(QtCore.QRect(140, 590, 61, 41))
        self.ajout_ok.setObjectName("ajout_ok")
        self.label_base_level = QtWidgets.QLabel(self.centralwidget)
        self.label_base_level.setGeometry(QtCore.QRect(50, 680, 251, 41))
        self.label_base_level.setAutoFillBackground(False)
        self.label_base_level.setObjectName("label_base_level")
        self.base_level_number = QtWidgets.QLabel(self.centralwidget)
        self.base_level_number.setGeometry(QtCore.QRect(50, 710, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.base_level_number.setFont(font)
        self.base_level_number.setObjectName("base_level_number")
        self.base_level_bar = QtWidgets.QProgressBar(self.centralwidget)
        self.base_level_bar.setGeometry(QtCore.QRect(50, 750, 201, 41))
        self.base_level_bar.setMinimum(0)
        self.base_level_bar.setMaximum(400)
        self.base_level_bar.setProperty("value", 100)
        self.base_level_bar.setTextVisible(False)
        self.base_level_bar.setOrientation(QtCore.Qt.Horizontal)
        self.base_level_bar.setInvertedAppearance(True)
        self.base_level_bar.setObjectName("base_level_bar")

        #Pump
        self.label_pump_speed = QtWidgets.QLabel(self.centralwidget)
        self.label_pump_speed.setGeometry(QtCore.QRect(30, 830, 171, 41))
        self.label_pump_speed.setObjectName("label_pump_speed")
        self.pump_speed_rpm = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.pump_speed_rpm.setGeometry(QtCore.QRect(170, 830, 81, 41))
        self.pump_speed_rpm.setAccessibleName("")
        self.pump_speed_rpm.setDecimals(0)
        self.pump_speed_rpm.setMaximum(240.0)
        self.pump_speed_rpm.setSingleStep(0.0)
        self.pump_speed_rpm.setObjectName("pump_speed_rpm")

        #Afichage tous pH et volumes
        self.grid0 = QtWidgets.QWidget(self.centralwidget)
        self.grid0.setGeometry(QtCore.QRect(650, 770, 1081, 101))
        self.grid0.setObjectName("grid0")
        self.grid_all_pH_vol = QtWidgets.QGridLayout(self.grid0)
        self.grid_all_pH_vol.setContentsMargins(0, 0, 0, 0)
        self.grid_all_pH_vol.setObjectName("grid_all_pH_vol")        
        #titre des lignes du tableau
        self.label_measure_number = QtWidgets.QLabel(self.grid0)
        self.label_measure_number.setObjectName("label_measure_number")
        self.label_measure_number.setText("measure N°") 
        self.grid_all_pH_vol.addWidget(self.label_measure_number, 0, 0, 1, 1) 
        self.label_vol = QtWidgets.QLabel(self.grid0)
        self.label_vol.setObjectName("label_vol")
        self.label_vol.setText("Volume (uL)")
        self.grid_all_pH_vol.addWidget(self.label_vol, 1, 0, 1, 1)
        self.label_pH_mes = QtWidgets.QLabel(self.grid0)
        self.label_pH_mes.setObjectName("label_pH_mes")
        self.label_pH_mes.setText("pH measure")
        self.grid_all_pH_vol.addWidget(self.label_pH_mes, 2, 0, 1, 1)
        #dernière colonne
        self.label_total_volume = QtWidgets.QLabel(self.grid0)
        self.label_total_volume.setObjectName("label_total_volume")
        self.label_total_volume.setText("total volume (uL)")
        self.total_volume = QtWidgets.QLabel(self.grid0)
        self.total_volume.setObjectName("total_volume")      

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1759, 18))
        self.menubar.setObjectName("menubar")
        self.panneau_de_titration = QtWidgets.QMenu(self.menubar)
        self.panneau_de_titration.setObjectName("panneau_de_titration")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionTitration_window = QtWidgets.QAction(MainWindow)
        self.actionTitration_window.setObjectName("actionTitration_window")
        self.menubar.addAction(self.panneau_de_titration.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.stabilisation_level.setFormat(_translate("MainWindow", "%p%"))
        self.label_pH.setText(_translate("MainWindow", "pH"))
        self.label_direct_abs.setText(_translate("MainWindow", "Absorbance direct"))
        self.label_stability.setText(_translate("MainWindow", "stability"))
        self.ajout_ok.setText(_translate("MainWindow", "Ok"))
        self.label_base_level.setText(_translate("MainWindow", "base syringe level (0-400uL)"))
        self.base_level_number.setText(_translate("MainWindow", "100 uL"))
        self.base_level_bar.setFormat(_translate("MainWindow", "%p%"))
        self.label_pump_speed.setText(_translate("MainWindow", "pump speed rpm"))
        self.background_and_reference.setText(_translate("MainWindow", "Spectro parameters"))
        self.label_delta_abs.setText(_translate("MainWindow", "Absorbance spectra (Delta)"))
        self.added_acid_label.setText(_translate("MainWindow", "added acid (HCl 0.1M) uL"))
        self.panneau_de_titration.setTitle(_translate("MainWindow", "Titration window"))
        self.actionTitration_window.setText(_translate("MainWindow", "Titration window"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ihm=IHM()
    ui = TitrationWindow(ihm)
    ui.graphic_setup(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
