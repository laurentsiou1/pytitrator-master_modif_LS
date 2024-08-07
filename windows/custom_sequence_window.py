"""fenêtre de séquence sur mesure"""

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMainWindow, QApplication
from ui.custom_sequence import Ui_CustomSequenceWindow

import pyqtgraph as pg
from windows.spectrumConfig import SpectrumConfigWindow
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

import file_manager as fm

ICON_PLAY="windows/play_icon.png"
ICON_PAUSE="windows/pause_icon.png"

class CustomSequenceWindow(QMainWindow,Ui_CustomSequenceWindow):
    
    absorbance_spectrum1=None

    def __init__(self, ihm, parent=None):   #win:WindowHandler
        super(CustomSequenceWindow,self).__init__(parent)
        self.setupUi(self)
        self.ihm=ihm
        self.seq=self.ihm.seq
        
        #Spectra tabs
        size=self.spectra_tabs.size()
        rect=QtCore.QRect(QtCore.QPoint(0,0),size)
        self.delta_all_abs = pg.PlotWidget(self.tab1)
        self.delta_all_abs.setGeometry(rect)  #.geometry() #meme dimension que le contenant
        #mais position sur l'origine car le repère est relatif
        self.delta_all_abs.setObjectName("delta_all_abs")
        self.all_abs = pg.PlotWidget(self.tab2)
        self.all_abs.setGeometry(rect)
        self.all_abs.setObjectName("all_abs")
        self.direct_intensity = pg.PlotWidget(self.tab3)
        self.direct_intensity.setGeometry(rect) 
        self.direct_intensity.setObjectName("direct_intensity")
        self.spectra_tabs.addTab(self.tab1, "delta") 
        self.spectra_tabs.addTab(self.tab2, "raw abs")
        self.spectra_tabs.addTab(self.tab3, "intensity")

        #spectre en direct
        self.delta_all_abs_plot=self.delta_all_abs.plot([0],[0])
        self.all_abs_plot=self.all_abs.plot([0],[0])
        self.direct_intensity_plot=self.direct_intensity.plot([0],[0])
        
        #connexions
        self.spectrometry.clicked.connect(self.ihm.openSpectroWindow)
        self.syringes.clicked.connect(self.ihm.openSyringePanel)
        self.pause_resume_button.clicked.connect(self.seq.pause_resume)
        #saving
        #print(seq)
        self.actionsave.triggered.connect(lambda : fm.createFullSequenceFiles(seq)) 
        #la fonction ne s'applique pas sur le self, d'où le lambda ?
        self.pump_speed_volt.valueChanged.connect(self.update_pump_speed)
        
        ##Initialisation en fonction de la config 
        seq=self.seq
        self.N_mes=seq.N_mes
        
        #Paramètres d'expérience
        self.experiment_parameters.setPlainText("\nNom de l'expérience : "+str(seq.experience_name)\
        +"\nDescription : "+str(seq.description)\
        +"\nType de matière organique : "+str(seq.OM_type)\
        +"\nConcentration : "+str(seq.concentration)\
        +"\nFibres : "+str(seq.fibers)\
        +"\nFlowcell : "+str(seq.flowcell)\
        +"\nDispense mode : "+str(seq.dispense_mode))

        #Spectro
        if ihm.spectro_unit.state=='open':
            self.lambdas=self.ihm.spectro_unit.wavelengths 
            self.N_lambda=len(self.lambdas)

        #Display current spectra
        self.ihm.spectro_unit.timer.timeout.connect(self.refresh_direct_spectra)

        #display timer
        self.ihm.timer_display.timeout.connect(self.refresh_screen)

        #graphique
        #colormap for plots
        cmap = plt.get_cmap('tab10')
        aa = [cmap(i) for i in np.linspace(0, 1, self.N_mes)]
        self.colors = [(int(r * 255), int(g * 255), int(b * 255)) for r, g, b, _ in aa]
        #PNG for pause/resume button
        self.pixmap_play=QtGui.QPixmap(ICON_PLAY)
        self.pixmap_pause=QtGui.QPixmap(ICON_PAUSE)
        self.pause_resume_button.setIcon(QtGui.QIcon(ICON_PAUSE))
        
        #Matrix for instructions
        for j in range(self.N_mes): 
            self.tab_jk = QtWidgets.QLabel(self.gridLayoutWidget_2)
            self.tab_jk.setAlignment(QtCore.Qt.AlignCenter)
            self.grid_instructions.addWidget(self.tab_jk, j+1, 0, 1, 1)
            self.tab_jk.setText(str(j+1))
            for k in range(5):
                self.tab_jk = QtWidgets.QLabel(self.gridLayoutWidget_2)
                self.tab_jk.setAlignment(QtCore.Qt.AlignCenter)
                self.grid_instructions.addWidget(self.tab_jk, j+1, k+1, 1, 1)
                self.tab_jk.setText(str(seq.instruction_table[j][k]))
        
        #matrix for dispensed volume, pH and measure times  #3columns and N_mes lines
        self.table_vol_pH=[[QtWidgets.QLabel(self.gridLayoutWidget),QtWidgets.QLabel(self.gridLayoutWidget),QtWidgets.QLabel(self.gridLayoutWidget)] for k in range(self.N_mes)]
        #Tableau volume dispensé/pH mesuré, temps de mesure
        #Mise en forme. A compléter par la suite
        for j in range(self.N_mes+1):
            for k in range(3):
                self.mes_jk = QtWidgets.QLabel(self.gridLayoutWidget)
                self.mes_jk.setAlignment(QtCore.Qt.AlignCenter)
                self.grid_mes_pH_vol.addWidget(self.mes_jk, j, k, 1, 1)
                self.mes_jk.setText("")

        #peristaltic pump
        if seq.pump.state=='open':
            self.pump_speed_volt.setProperty("value", seq.pump.mean_voltage)           

        #pH meter
        self.stab_time.setProperty("value", seq.phmeter.stab_time)
        self.stab_time.valueChanged.connect(self.update_stab_time)
        self.stab_step.setProperty("value", seq.phmeter.stab_step)
        self.stab_step.valueChanged.connect(self.update_stab_step)

        self.direct_pH.display(self.ihm.phmeter.currentPH) #pH instantané

    #DIRECT
    def refresh_screen(self):
        #Countdown
        try:
            tm=datetime.now()
            tm=tm.replace(microsecond=0)
            elapsed=tm-self.seq.time_mes_last
            elapsed_sec = elapsed.total_seconds() #convert to seconds
            remaining = int(max(0,self.seq.delay_mes-elapsed_sec))
            #print("remaining time : ", remaining)
            self.countdown.setProperty("value", remaining)
        except:
            pass
        #PhMeter
        if self.ihm.phmeter.state=='open':
            self.direct_pH.display(self.ihm.phmeter.currentPH)
            self.stab_time.setProperty("value", self.ihm.phmeter.stab_time)
            self.stab_step.setProperty("value", self.ihm.phmeter.stab_step)
            self.stabilisation_level.setProperty("value", self.ihm.phmeter.stab_purcent)
            self.label_stability.setText(str(self.ihm.phmeter.stab_purcent)+"%")
        #Peristaltic pump
        if self.ihm.peristaltic_pump.state=='open':
            self.pump_speed_volt.setProperty("value", self.ihm.peristaltic_pump.mean_voltage)

    #Displaying current spectra
    def refresh_direct_spectra(self):
        #print("passage dans update spectra")
        if self.ihm.spectro_unit.state=='open': #Intensity live
            self.direct_intensity_plot.setData(self.lambdas,self.ihm.spectro_unit.current_intensity_spectrum)
        if self.ihm.spectro_unit.current_absorbance_spectrum!=None: #Absorbance live
            self.all_abs_plot.setData(self.lambdas,self.ihm.spectro_unit.current_absorbance_spectrum)
            if self.ihm.spectro_unit.absorbance_spectrum1!=None:    #Delta Abs live
                print("dans le delta abs")
                self.current_delta_abs=[self.ihm.spectro_unit.current_absorbance_spectrum[k]-self.absorbance_spectrum1[k] for k in range(self.N_lambda)]
                self.delta_all_abs_plot.setData(self.lambdas,self.current_delta_abs)

    #MODIF SUR LES INSTRUMENTS
    def update_pump_speed(self):
        self.ihm.peristaltic_pump.setSpeed_voltage(self.pump_speed_volt.value())
    def update_stab_time(self):
        self.ihm.phmeter.stab_time=self.stab_time.value()
    def update_stab_step(self):
        self.ihm.phmeter.stab_step=self.stab_step.value()
    
    #ENREGISTREMENT

    #Spectres d'absorbance
    def append_abs_spectra(self,N,spec,delta):
        print(spec[300:310],delta[300:310])
        #delta
        a=self.delta_all_abs.plot([0],[0],pen=pg.mkPen(color=self.colors[N-1])) #pen='g'
        a.setData(self.lambdas,delta)
        #abs
        b=self.all_abs.plot([0],[0],pen=pg.mkPen(color=self.colors[N-1]))
        b.setData(self.lambdas,spec)
    
    #volume, pH and times
    def append_vol_in_table(self,nb,vol): #nb numero de mesure 1 à Nmes
        self.table_vol_pH[nb-1][0].setObjectName("vol"+str(nb))
        self.table_vol_pH[nb-1][0].setAlignment(QtCore.Qt.AlignCenter)
        self.grid_mes_pH_vol.addWidget(self.table_vol_pH[nb-1][0], nb, 0, 1, 1)
        self.table_vol_pH[nb-1][0].clear()
        self.table_vol_pH[nb-1][0].setText(str(vol))
    def append_pH_in_table(self,nb,pH): #nb=numero de la mesure 1 à Nmes
        self.table_vol_pH[nb-1][1].setObjectName("pH"+str(nb))
        self.table_vol_pH[nb-1][1].setAlignment(QtCore.Qt.AlignCenter)
        self.grid_mes_pH_vol.addWidget(self.table_vol_pH[nb-1][1], nb, 1, 1, 1)
        self.table_vol_pH[nb-1][1].clear()
        self.table_vol_pH[nb-1][1].setText(str(pH))
    def append_time_in_table(self,nb,dt):
        self.table_vol_pH[nb-1][2].setObjectName("dt"+str(nb))
        self.table_vol_pH[nb-1][2].setAlignment(QtCore.Qt.AlignCenter)
        self.grid_mes_pH_vol.addWidget(self.table_vol_pH[nb-1][2], nb, 2, 1, 1)
        self.table_vol_pH[nb-1][2].clear()
        self.table_vol_pH[nb-1][2].setText(str(dt))

    def pause(self):
        self.pause_resume_button.setIcon(QtGui.QIcon(ICON_PLAY))

    def resume(self):
        self.pause_resume_button.setIcon(QtGui.QIcon(ICON_PAUSE))

    def closeEvent(self, event):
        print("User has clicked the red x on the custom sequence window")
        event.accept()
        self.ihm.dispenser.stop()
        self.ihm.updateDefaultParam()
    
