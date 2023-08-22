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
        self.cal_method=3 #3 points pH=4,7,10 #ou pH=4,7 

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(440, 290)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(190, 220, 231, 51))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Apply|QtWidgets.QDialogButtonBox.Cancel)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.clicked.connect(self.validateCal) #lorsqu'on clique sur valider, la calibration est enregsitrée
        self.buttonBox.clicked.connect(self.phmeter.onCalibrationChange)        
        self.buttonBox.clicked.connect(self.motherWindow.onCalibrationChange)
        self.direct_pH = QtWidgets.QLCDNumber(Dialog)
        self.direct_pH.setGeometry(QtCore.QRect(210, 80, 211, 131))
        self.direct_pH.setObjectName("direct_pH")
        self.direct_pH.setNumDigits(6)
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
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        #activation de l'actualisation de la tension
        self.phmeter.voltagechannel.setOnVoltageChangeHandler(self.setOnDirectVoltage)
        #affichage de la tension déjà affichée sur le panneau de contrôle
        if self.phmeter.getIsOpen():
            U=self.phmeter.voltagechannel.getVoltage()  #valeur actuelle de tension
            self.direct_pH.display(U)
    
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "tension (mV) en direct"))
        self.pushButton_pH10.setText(_translate("Dialog", "pH10"))
        self.pushButton_pH7.setText(_translate("Dialog", "pH7"))
        self.pushButton_pH4.setText(_translate("Dialog", "pH4"))
        self.label_2.setText(_translate("Dialog", "Tensions enregistrées"))

    def setOnDirectVoltage(self, ch, voltage):
        #print(self, ch, voltage)
        #pH = volt2pH(2,4,voltage)
        self.direct_pH.display(voltage)

    def saveAndShowVoltage(self, screen): #sreen est un objet QLCDNumber
        U=self.phmeter.voltagechannel.getVoltage()
        if screen==self.lcdNumber_pH4:
            self.U4=U
        if screen==self.lcdNumber_pH7:
            self.U7=U
        if screen==self.lcdNumber_pH10:
            self.U10=U
        #pH=volt2pH(2,4,U)
        screen.display(U)

    def validateCal(self): #method est un entier 2 ou 3 selon le type de calibration voulu
        method = self.cal_method
        print(method)
        dt = datetime.now()
        T = 22 #22°C pour l'instant non modifiable
        #plus tard, implémenter un bouton sur l'interface pour sélectionner le type de calibration
        if method == 2:
            u_cal = [self.U4, self.U7]
        if method == 3:
            u_cal = [self.U4, self.U7, self.U10]
        (a,b)=PHMeter.computeCalCoefs(self.phmeter,u_cal,method) #calcul des coefficients de calib
        PHMeter.saveCalData(self.phmeter, dt, 22, method, u_cal, (a,b)) #enregistrer dans le fichier

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
