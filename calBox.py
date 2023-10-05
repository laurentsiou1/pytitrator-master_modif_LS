"fenêtre de calibration du pH mètre"
# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file '../fenetre_calibration.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets

from pHmeter import *
from datetime import datetime

class CalBox(object):
    def __init__(self, phm, control_pannel):
        self.phmeter=phm
        self.motherWindow=control_pannel
        self.U4=0
        self.U7=0
        self.U10=0
        self.used_pH_buffers=set()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(440, 290)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(190, 220, 231, 51))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok|QtWidgets.QDialogButtonBox.Cancel)
        self.buttonBox.setObjectName("buttonBox")
        #print("passage!")

        self.direct_voltage = QtWidgets.QLCDNumber(Dialog)
        self.direct_voltage.setGeometry(QtCore.QRect(210, 80, 211, 131))
        self.direct_voltage.setObjectName("direct_voltage")
        self.direct_voltage.setNumDigits(5)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(260, 40, 131, 41))
        self.label.setObjectName("label")
        self.lcdNumber_pH4 = QtWidgets.QLCDNumber(Dialog)
        self.lcdNumber_pH4.setGeometry(QtCore.QRect(30, 50, 71, 51))
        self.lcdNumber_pH4.setObjectName("lcdNumber_pH4")
        self.lcdNumber_pH4.setNumDigits(6)
        self.lcdNumber_pH7 = QtWidgets.QLCDNumber(Dialog)
        self.lcdNumber_pH7.setGeometry(QtCore.QRect(30, 130, 71, 51))
        self.lcdNumber_pH7.setObjectName("lcdNumber_pH7")
        self.lcdNumber_pH7.setNumDigits(6)
        self.lcdNumber_pH10 = QtWidgets.QLCDNumber(Dialog)
        self.lcdNumber_pH10.setGeometry(QtCore.QRect(30, 210, 71, 51))
        self.lcdNumber_pH10.setObjectName("lcdNumber_pH10")
        self.lcdNumber_pH10.setNumDigits(6)
        self.pushButton_pH4 = QtWidgets.QPushButton(Dialog, clicked = lambda: self.saveAndShowVoltage(self.lcdNumber_pH4))
        self.pushButton_pH4.setGeometry(QtCore.QRect(130, 50, 51, 51))
        self.pushButton_pH4.setObjectName("pushButton_pH4")
        self.pushButton_pH7 = QtWidgets.QPushButton(Dialog, clicked = lambda: self.saveAndShowVoltage(self.lcdNumber_pH7))
        self.pushButton_pH7.setGeometry(QtCore.QRect(130, 130, 51, 51))
        self.pushButton_pH7.setObjectName("pushButton_pH7")
        self.pushButton_pH10 = QtWidgets.QPushButton(Dialog, clicked = lambda: self.saveAndShowVoltage(self.lcdNumber_pH10))
        self.pushButton_pH10.setGeometry(QtCore.QRect(130, 210, 51, 51))
        self.pushButton_pH10.setObjectName("pushButton_pH10")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 10, 151, 31))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)

        self.buttonBox.accepted.connect(self.validateCal) #lorsqu'on clique sur valider, la calibration est enregsitrée
        self.buttonBox.accepted.connect(self.phmeter.onCalibrationChange)        
        self.buttonBox.accepted.connect(self.motherWindow.onCalibrationChange)        
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        self.buttonBox.clicked.connect(self.motherWindow.setOnDirectPH) # type: ignore
        #QtCore.QMetaObject.connectSlotsByName(Dialog)

        
        #activation de l'actualisation de la tension
        self.phmeter.voltagechannel.setOnVoltageChangeHandler(self.setOnDirectVoltage)
        #affichage de la tension déjà affichée sur le panneau de contrôle
        #if self.phmeter.getIsOpen():
            #U=self.phmeter.voltagechannel.getVoltage()  #valeur actuelle de tension
            #self.direct_voltage.display(U)
    
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "tension (mV) en direct"))
        self.pushButton_pH10.setText(_translate("Dialog", "pH10"))
        self.pushButton_pH7.setText(_translate("Dialog", "pH7"))
        self.pushButton_pH4.setText(_translate("Dialog", "pH4"))
        self.label_2.setText(_translate("Dialog", "Tensions enregistrées"))

    def setOnDirectVoltage(self, ch, voltage):
        self.phmeter.currentVoltage=voltage    
        self.direct_voltage.display(voltage)

    def saveAndShowVoltage(self, screen): #sreen est un objet QLCDNumber
        U=self.phmeter.currentVoltage
        print("save voltage")
        if screen==self.lcdNumber_pH4:
            self.U4=U
            self.used_pH_buffers.add(4)
        if screen==self.lcdNumber_pH7:
            self.U7=U
            self.used_pH_buffers.add(7)
        if screen==self.lcdNumber_pH10:
            self.U10=U
            self.used_pH_buffers.add(10)
        print("voltage=",U)
        screen.display(U)

    def validateCal(self): #pH_buffers est un tuple contenant les valeurs de pH des tampons
        pH_buffers=sorted(list(self.used_pH_buffers))
        self.used_pH_buffers = pH_buffers
        #print("pH buffers : ",type(pH_buffers),pH_buffers)
        dt = datetime.now()
        T = 22 #22°C pour l'instant non modifiable
        if pH_buffers == [4]:
            u_cal = [self.U4]
        elif pH_buffers == [7]:
            u_cal = [self.U7]
        elif pH_buffers == [4,7]:
            u_cal = [self.U4, self.U7]
            print("calib 2 pts")
        elif pH_buffers == [4,7,10]:
            u_cal = [self.U4, self.U7, self.U10]
            print("calib 3 pts")
        else:
            print("This type of calibration is not suppported")
        (a,b)=PHMeter.computeCalCoefs(self.phmeter,u_cal,pH_buffers) #calcul des coefficients de calib
        PHMeter.saveCalData(self.phmeter, dt, 22, pH_buffers, u_cal, (a,b)) #enregistrer dans le fichier

"""
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = CalBox()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
"""

"""
# boucle pour tester ce programme uniquement
if __name__ == "__main__":
    from controlPannel import ControlPannel
    try: #si le pH mètre est connecté
        ch = VoltageInput()
        ch.setDeviceSerialNumber(432846)
        ch.setChannel(0)
        ch.openWaitForAttachment(1000)
        ch.setOnVoltageChangeHandler(PHMeter.doOnVoltageChange)

        phm = PHMeter(ch)
        phm.configure_pHmeter()
        print("pH mètre connecté")
    except: #pH mètre non connecté
        phm = 'pH mètre'
        print("pH mètre non connecté")
    finally:    
        import sys
        app = QtWidgets.QApplication(sys.argv)
        Dialog = QtWidgets.QDialog()
        mwindow = ControlPannel()
        ui = CalBox(phm, mwindow)
        ui.setupUi(Dialog)
    try:
        #connection de la fenêtre avec le pH-mètre
        ui.phmeter.voltagechannel.setOnVoltageChangeHandler(ui.setOnDirectPH)
    except:
        pass
    finally:
        Dialog.show()        
        #print("show")
        sys.exit(app.exec_())
"""

if __name__ == "__main__":
    
    #spectro
    od = OceanDirectAPI()
    device_count = od.find_usb_devices() # 1 si appareils détectés
    device_ids = od.get_device_ids()
    #device_count = len(device_ids)
    id=device_ids[0]
    spectro = od.open_device(id) #crée une instance de la classe Spectrometer
    adv = Spectrometer.Advanced(spectro)
    spectro_unit=AbsorbanceMeasure(od,spectro)

    #pHmètre
    U_pH = VoltageInput()
    ph_meter = PHMeter(U_pH)

    #Interface
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    cp = ControlPannel(ph_meter,spectro_unit)
    ui = CalBox(ph_meter, cp)
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
