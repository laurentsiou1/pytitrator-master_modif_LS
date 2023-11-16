# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../exp_params.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from IHM import IHM
from automatic_sequences import TitrationSequence

from windowHandler import WindowHandler
from titrationWindow import TitrationWindow


class ExpConfig(object):

    def __init__(self, ihm:IHM, win:WindowHandler):
        self.ihm=ihm
        self.window_handler=win

    def launchTitration(self):
        #Normalement On doit régler le spectro avant la séquence auto. 
        #Le pH mètre est calibré manuellement aussi 
        #Le pousse seringue doit être mis sur la position zéro ? 
        #On a donc déjà des attributs qui sont open pour les sous systèmes. 
        #Devoir connecter les sous-sytèmes est un signe de non ou mauvais réglage. 

        #arrêt des timers pour consacrer toute la mémoire sur la séquence
        self.ihm.timer1s.stop()
        self.ihm.timer3s.stop()
        #self.ihm.timer_spectra.stop() celui ci continue

        nc=0
        if self.ihm.spectro_unit.state=='closed':
            self.ihm.spectro_unit.connect()
            nc+=1
        if self.ihm.phmeter.state=='closed':
            self.ihm.phmeter.connect()
            nc+=1
        if self.ihm.syringe_pump.state=='closed':
            self.ihm.syringe_pump.connect()
        if self.ihm.peristaltic_pump.state=='closed':
            self.ihm.peristaltic_pump.connect()

        #vérification que tout est connecté
        if nc==0:
            print("\ntous les instruments sont configurés\n\n    ### Lancement de la séquence de titrage automatique ###\n\n")
                #experiment parameters
        
        self.ihm.titration_sequence=TitrationSequence(self.ihm,self.window_handler) #création de l'objet dans l'IHM        

        self.ihm.titration_sequence.experience_name=self.experience_name.toPlainText()
        self.ihm.titration_sequence.description=self.description.toPlainText()
        self.ihm.titration_sequence.OM_type=self.OM_type.currentText() #type of organic matter
        self.ihm.titration_sequence.concentration=self.concentration.value()
        self.ihm.titration_sequence.fibers=self.fibers.currentText()
        self.ihm.titration_sequence.flowcell=self.flowcell.currentText()
        self.ihm.titration_sequence.initial_pH=self.pH_init.value()
        self.ihm.titration_sequence.final_pH=self.pH_fin.value()
        self.ihm.titration_sequence.N_mes=self.N_mes.value() #number of pH/spectra measures
        
        #affichage des données pour la séquence auto
        print("\nNom de l'expérience : ",self.ihm.titration_sequence.experience_name,\
        "\nDescription : ",self.ihm.titration_sequence.description,\
        "\nType de matière organique : ",self.ihm.titration_sequence.OM_type,\
        "\nConcentration : ",self.ihm.titration_sequence.concentration,\
        "\nFibres : ",self.ihm.titration_sequence.fibers,\
        "\nFlowcell : ",self.ihm.titration_sequence.flowcell,\
        "\npH initial : ",self.ihm.titration_sequence.initial_pH,\
        "\npH final : ",self.ihm.titration_sequence.final_pH,\
        "\nNombre de mesures : ",self.ihm.titration_sequence.N_mes)

        #création de la fenêtre
        self.window_handler.titration_window0=QtWidgets.QMainWindow()
        self.window_handler.titration_window0.show()
        self.window_handler.titration_window1 = TitrationWindow(self.ihm)
        self.window_handler.titration_window1.graphical_setup(self.window_handler.titration_window0)
        self.window_handler.titration_window1.param_init() 

        self.ihm.titration_sequence.configure()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(726, 682)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(480, 50, 221, 61))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.accepted.connect(self.launchTitration)
        self.description = QtWidgets.QPlainTextEdit(Dialog)
        self.description.setGeometry(QtCore.QRect(10, 50, 451, 81))
        self.description.setPlainText("")
        self.description.setObjectName("description")
        self.flowcell = QtWidgets.QComboBox(Dialog)
        self.flowcell.setGeometry(QtCore.QRect(10, 600, 351, 71))
        self.flowcell.setObjectName("flowcell")
        self.flowcell.addItem("")
        self.flowcell.addItem("")
        self.flowcell.addItem("")
        self.fibers = QtWidgets.QComboBox(Dialog)
        self.fibers.setGeometry(QtCore.QRect(10, 480, 351, 71))
        self.fibers.setObjectName("fibers")
        self.fibers.addItem("")
        self.fibers.addItem("")
        self.fibers.addItem("")
        self.label_name = QtWidgets.QLabel(Dialog)
        self.label_name.setGeometry(QtCore.QRect(10, 10, 241, 41))
        self.label_name.setObjectName("label_name")
        self.label_OM = QtWidgets.QLabel(Dialog)
        self.label_OM.setGeometry(QtCore.QRect(10, 350, 161, 41))
        self.label_OM.setObjectName("label_OM")
        self.label_concentration = QtWidgets.QLabel(Dialog)
        self.label_concentration.setGeometry(QtCore.QRect(190, 350, 151, 41))
        self.label_concentration.setObjectName("label_concentration")
        self.label_description = QtWidgets.QLabel(Dialog)
        self.label_description.setGeometry(QtCore.QRect(10, 150, 181, 41))
        self.label_description.setObjectName("label_description")
        self.experience_name = QtWidgets.QPlainTextEdit(Dialog)
        self.experience_name.setGeometry(QtCore.QRect(10, 190, 701, 161))
        self.experience_name.setPlainText("")
        self.experience_name.setObjectName("experience_name")
        self.OM_type = QtWidgets.QComboBox(Dialog)
        self.OM_type.setGeometry(QtCore.QRect(10, 390, 151, 41))
        self.OM_type.setEditable(True)
        self.OM_type.setMaxVisibleItems(10)
        self.OM_type.setObjectName("OM_type")
        self.OM_type.addItem("")
        self.OM_type.addItem("")
        self.concentration = QtWidgets.QDoubleSpinBox(Dialog)
        self.concentration.setGeometry(QtCore.QRect(190, 390, 171, 41))
        self.concentration.setDecimals(1)
        self.concentration.setMinimum(0.1)
        self.concentration.setSingleStep(0.1)
        self.concentration.setProperty("value", 1.0)
        self.concentration.setObjectName("concentration")
        self.label_fiber = QtWidgets.QLabel(Dialog)
        self.label_fiber.setGeometry(QtCore.QRect(10, 440, 351, 41))
        self.label_fiber.setObjectName("label_fiber")
        self.label_flowcell = QtWidgets.QLabel(Dialog)
        self.label_flowcell.setGeometry(QtCore.QRect(10, 560, 351, 41))
        self.label_flowcell.setObjectName("label_flowcell")
        self.N_mes = QtWidgets.QSpinBox(Dialog)
        self.N_mes.setGeometry(QtCore.QRect(570, 590, 131, 61))
        self.N_mes.setMinimum(3)
        self.N_mes.setMaximum(20)
        self.N_mes.setProperty("value", 10)
        self.N_mes.setObjectName("N_mes")
        self.label_pHinit = QtWidgets.QLabel(Dialog)
        self.label_pHinit.setGeometry(QtCore.QRect(430, 390, 111, 41))
        self.label_pHinit.setObjectName("label_pHinit")
        self.label_pHfin = QtWidgets.QLabel(Dialog)
        self.label_pHfin.setGeometry(QtCore.QRect(590, 390, 121, 41))
        self.label_pHfin.setObjectName("label_pHfin")
        self.label_Nmes = QtWidgets.QLabel(Dialog)
        self.label_Nmes.setGeometry(QtCore.QRect(430, 590, 131, 61))
        self.label_Nmes.setObjectName("label_Nmes")
        self.pH_init = QtWidgets.QDoubleSpinBox(Dialog)
        self.pH_init.setGeometry(QtCore.QRect(420, 450, 121, 61))
        self.pH_init.setDecimals(1)
        self.pH_init.setMinimum(3.0)
        self.pH_init.setMaximum(5.0)
        self.pH_init.setSingleStep(0.1)
        self.pH_init.setProperty("value", 4.0)
        self.pH_init.setObjectName("pH_init")
        self.pH_fin = QtWidgets.QDoubleSpinBox(Dialog)
        self.pH_fin.setGeometry(QtCore.QRect(590, 450, 111, 61))
        self.pH_fin.setDecimals(1)
        self.pH_fin.setMinimum(8.0)
        self.pH_fin.setMaximum(10.0)
        self.pH_fin.setSingleStep(0.1)
        self.pH_fin.setProperty("value", 9.0)
        self.pH_fin.setObjectName("pH_fin")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.flowcell.setItemText(0, _translate("Dialog", "FIA Zcell 50mm"))
        self.flowcell.setItemText(1, _translate("Dialog", "CUV 50mm"))
        self.flowcell.setItemText(2, _translate("Dialog", "CUV 10mm"))
        self.fibers.setItemText(0, _translate("Dialog", "QP-600-1-SR-BX & QP600-025-SR"))
        self.fibers.setItemText(1, _translate("Dialog", "300um"))
        self.fibers.setItemText(2, _translate("Dialog", "200um"))
        self.label_name.setText(_translate("Dialog", "Nom de l\'expérience"))
        self.label_OM.setText(_translate("Dialog", "Type de matière organique"))
        self.label_concentration.setText(_translate("Dialog", "Concentration (ppmC)"))
        self.label_description.setText(_translate("Dialog", "Description"))
        self.OM_type.setCurrentText(_translate("Dialog", "LHA"))
        self.OM_type.setItemText(0, _translate("Dialog", "LHA"))
        self.OM_type.setItemText(1, _translate("Dialog", "SRNOM"))
        self.label_fiber.setText(_translate("Dialog", "fibres"))
        self.label_flowcell.setText(_translate("Dialog", "cellule"))
        self.label_pHinit.setText(_translate("Dialog", "pH initial"))
        self.label_pHfin.setText(_translate("Dialog", "pH final"))
        self.label_Nmes.setText(_translate("Dialog", "N mesures"))

#Lancement direct du programme avec run
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ihm=IHM()
    win=WindowHandler()
    ui = ExpConfig(ihm,win)
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
