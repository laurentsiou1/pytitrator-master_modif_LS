"Classe de la fenêtre pour la prise de référence sur le spectro"
#En partie importée de PyQt
# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file '../spectro_param.ui'
# Created by: PyQt5 UI code generator 5.15.9
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg

from oceandirect.OceanDirectAPI import OceanDirectError, OceanDirectAPI, Spectrometer as Sp
from oceandirect.od_logger import od_logger

from spectro.absorbanceMeasure import AbsorbanceMeasure
import spectro.processing as proc

class SpectrumConfigWindow(object):
    def __init__(self, spectro_unit):
        self.spectro_unit=spectro_unit
        if spectro_unit.state=='open':
            self.shutter_state=not(self.spectro_unit.adv.get_enable_lamp())

    def changeShutterState(self):
        if self.spectro_unit.state=='open':
            self.spectro_unit.changeShutterState()
    
    def refresh_all_spectra_on_timer(self):
        if self.spectro_unit.active_dark_spectrum!=None:
            #dark spectrum
            self.refresh_displayed_dark_spectrum() #refresh du graphe
            #intensity_widget spectrum (corrected)
            self.timer.timeout.connect(self.refresh_displayed_intensity_spectrum) #mise sur timer
            if self.spectro_unit.active_ref_spectrum!=None:
                #ref spectrum
                self.refresh_displayed_ref_spectrum() #refresh
                #absorbance
                self.update_absorbance_spectrum()
                self.refresh_displayed_absorbance_spectrum()
    
    def update_dark_spectrum(self):
        self.spectro_unit.acquire_dark_spectrum()
    
    def update_intensity_spectrum(self):
        #spectre courant intensité
        #nécessite un spectre d'obscurité pour corriger
        cs=AbsorbanceMeasure.get_averaged_corrected_spectrum(self.spectro_unit)
        self.spectro_unit.current_spectrum=cs
        
    def update_ref_spectrum(self):
        self.spectro_unit.acquire_ref_spectrum()    

    def update_absorbance_spectrum(self):
        #cette fonction est appelée alors même qu'il n'y a pas de spectre de réf actif
        self.spectro_unit.current_Abs_spectrum=proc.intensity2absorbance(self.spectro_unit.current_spectrum,self.spectro_unit.active_ref_spectrum)

    def refresh_displayed_dark_spectrum(self):
        a=self.dark_widget.plot([0],[0],clear = True)
        self.dark_plot=a
        self.dark_plot.clear()
        self.dark_plot.setData(self.lambdas,self.spectro_unit.active_dark_spectrum)
        
    def refresh_displayed_intensity_spectrum(self):
        self.intensity_plot=self.intensity_widget.plot([0],[0],pen="r",clear = True)
        self.intensity_plot.setData(self.lambdas,self.spectro_unit.current_spectrum)
    
    def refresh_displayed_ref_spectrum(self):
        self.ref_plot=self.ref_widget.plot([0],[0],pen="g",clear = True)
        self.ref_plot.setData(self.lambdas,self.spectro_unit.active_ref_spectrum)  

    def refresh_displayed_absorbance_spectrum(self):
        self.abs_plot=self.abs_widget.plot([0],[0],pen="y",clear = True)
        self.abs_plot.setData(self.lambdas,self.spectro_unit.current_Abs_spectrum)  

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1263, 755)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(1010, 720, 241, 21))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        
        self.dark_widget = pg.PlotWidget(Dialog)
        self.dark_widget.setGeometry(QtCore.QRect(1000, 60, 251, 171))
        self.dark_widget.setObjectName("dark_widget")
        self.ref_widget = pg.PlotWidget(Dialog)
        self.ref_widget.setGeometry(QtCore.QRect(1000, 290, 251, 171))
        self.ref_widget.setObjectName("ref_widget")
        
        self.abs_widget = pg.PlotWidget(Dialog) 
        #self.absorbance_widget = QtWidgets.QGraphicsView(Dialog)
        self.abs_widget.setGeometry(QtCore.QRect(10, 40, 971, 621))
        self.abs_widget.setObjectName("abs_widget")
        self.intensity_widget = pg.PlotWidget(Dialog)
        self.intensity_widget.setGeometry(QtCore.QRect(1000, 520, 251, 171))
        self.intensity_widget.setObjectName("intensity_widget")
        
        self.label_dark = QtWidgets.QLabel(Dialog)
        self.label_dark.setGeometry(QtCore.QRect(1020, 20, 91, 31))
        self.label_dark.setObjectName("label_dark")
        self.label_ref = QtWidgets.QLabel(Dialog)
        self.label_ref.setGeometry(QtCore.QRect(1020, 250, 91, 31))
        self.label_ref.setObjectName("label_ref")
        self.label_intensity = QtWidgets.QLabel(Dialog)
        self.label_intensity.setGeometry(QtCore.QRect(1020, 480, 91, 31))
        self.label_intensity.setObjectName("label_intensity")
        self.label_abs = QtWidgets.QLabel(Dialog)
        self.label_abs.setGeometry(QtCore.QRect(20, 10, 91, 31))
        self.label_abs.setObjectName("label_abs")
        
        #boutons de mise à jour réf et dark
        self.refresh_dark_button = QtWidgets.QPushButton(Dialog)
        self.refresh_dark_button.setGeometry(QtCore.QRect(1140, 20, 81, 31))
        self.refresh_dark_button.setObjectName("refresh_dark_button")
        self.refresh_ref_button = QtWidgets.QPushButton(Dialog)
        self.refresh_ref_button.setGeometry(QtCore.QRect(1140, 250, 81, 31))
        self.refresh_ref_button.setObjectName("refresh_ref_button")
    

        self.Tint = QtWidgets.QSpinBox(Dialog)
        self.Tint.setGeometry(QtCore.QRect(30, 700, 71, 31))
        self.Tint.setMinimum(1)
        self.Tint.setMaximum(1000)
        self.Tint.setProperty("value", 10)
        self.Tint.setObjectName("Tint")
        self.label_tint = QtWidgets.QLabel(Dialog)
        self.label_tint.setGeometry(QtCore.QRect(50, 680, 51, 21))
        self.label_tint.setObjectName("label_tint")
        self.label_avg = QtWidgets.QLabel(Dialog)
        self.label_avg.setGeometry(QtCore.QRect(200, 680, 61, 21))
        self.label_avg.setObjectName("label_avg")
        self.avg = QtWidgets.QSpinBox(Dialog)
        self.avg.setGeometry(QtCore.QRect(180, 700, 71, 31))
        self.avg.setMinimum(1)
        self.avg.setMaximum(500)
        self.avg.setProperty("value", 1)
        self.avg.setObjectName("avg")
        self.shutter = QtWidgets.QCheckBox(Dialog, clicked = lambda: self.changeShutterState())
        self.shutter.setGeometry(QtCore.QRect(330, 700, 71, 31))
        self.shutter.setObjectName("shutter")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        #création d'un timer pour le renouvellement du spectre affiché
        #il pourrait servir dans les autres fenêtres!
        self.timer = QtCore.QTimer()
        self.timer.setInterval(5000)
        self.timer.start()

        #spectro connecté
        if self.spectro_unit.state=='open':
            self.shutter.setChecked(self.shutter_state)   
            
            self.lambdas=self.spectro_unit.wavelengths
            #connexion boutons à l'initialisation
            self.refresh_dark_button.clicked.connect(self.update_dark_spectrum) #dark spectrum

            #connexion des boutons
            self.timer.timeout.connect(self.update_intensity_spectrum) #intensity_widget spectrum (corrected)  
            self.refresh_ref_button.clicked.connect(self.update_ref_spectrum) #ref spectrum
            #actualisation des spectres périodiquement
            self.timer.timeout.connect(self.refresh_all_spectra_on_timer)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_dark.setText(_translate("Dialog", "Dark Spectrum"))
        self.label_ref.setText(_translate("Dialog", "Référence"))
        self.label_intensity.setText(_translate("Dialog", "Intensité"))
        self.label_abs.setText(_translate("Dialog", "Absorbance"))
        self.refresh_dark_button.setText(_translate("Dialog", "refresh"))
        self.refresh_ref_button.setText(_translate("Dialog", "refresh"))
        self.label_tint.setText(_translate("Dialog", "T int"))
        self.label_avg.setText(_translate("Dialog", "averaging"))
        self.shutter.setText(_translate("Dialog", "Shutter"))


if __name__ == "__main__":
    logger = od_logger()
    od = OceanDirectAPI()
    device_count = od.find_usb_devices() #nb d'appareils détectés
    device_ids = od.get_device_ids()
    if device_ids!=[]:
        id=device_ids[0]
        try:
            spectro = od.open_device(id) #crée une instance de la classe Spectrometer
            adv = Sp.Advanced(spectro)
            spectroIsConnected=True
            print("Spectro connecté")
        except:
            spectro=None #on crée dans tous les cas un objet Spectrometer
            adv = None
            spectroIsConnected=False
            print("Ne peut pas se connecter au spectro numéro ", id)
            pass
    else:
        spectro=None #on crée dans tous les cas un objet Spectrometer
        adv = None #Sp.Advanced(spectro)
        spectroIsConnected=False
        print("Spectro non connecté")
    print("Nombre d'appareils OceanDirect détectés : ", device_count)
    print("ID spectros: ", device_ids)

    spectrometry_unit=AbsorbanceMeasure(od, spectro)

    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = SpectrumConfigWindow(spectrometry_unit)
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
