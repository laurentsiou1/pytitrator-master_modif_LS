# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../exp_params.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QDialog

from IHM import IHM
from automatic_sequences import TitrationSequence

from windowHandler import WindowHandler
from titrationWindow import TitrationWindow


class ExpConfig(QDialog): #(object)

    def __init__(self, ihm:IHM, win:WindowHandler, parent=None):
        super().__init__(parent)
        self.ihm=ihm
        self.window_handler=win
        self.V0=50000   #volume initial uL

    def launchTitration(self):
        
        config=[self.experience_name.toPlainText(),\
            self.description.toPlainText(),\
            self.OM_type.currentText(),\
            self.concentration.value(),\
            self.fibers.currentText(),\
            self.flowcell.currentText(),\
            self.V0,\
            self.dispense_mode.currentText(),\
            self.Nmes.value(),\
            self.pH_init.value(),\
            self.pH_fin.value(),\
            self.saving_folder.text()]    

        
        self.ihm.titration_sequence=TitrationSequence(self.ihm,self.window_handler,config) #création de l'objet dans l'IHM
        self.ihm.titration_sequence.configure()
        
        #affichage des données pour la séquence auto
        print("\nNom de l'expérience : ",self.ihm.titration_sequence.experience_name,\
        "\nDescription : ",self.ihm.titration_sequence.description,\
        "\nType de matière organique : ",self.ihm.titration_sequence.OM_type,\
        "\nConcentration : ",self.ihm.titration_sequence.concentration,\
        "\nFibres : ",self.ihm.titration_sequence.fibers,\
        "\nFlowcell : ",self.ihm.titration_sequence.flowcell,\
        "\nVolume initial : ", self.V0,\
        "\nMode de dispense : ",self.ihm.titration_sequence.dispense_mode,\
        "\npH initial : ",self.ihm.titration_sequence.pH_start,\
        "\npH final : ",self.ihm.titration_sequence.pH_end,\
        "\nNombre de mesures : ",self.ihm.titration_sequence.N_mes,\
        "\nDossier de sauvegarde du titrage : ",self.ihm.titration_sequence.saving_folder)



    def browsefolder(self):
        folderpath = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder', "H:/A Nouvelle arbo/DOCUMENTS TECHNIQUES/Projets Collaboratifs/DOMMINO/MESURES")
        self.saving_folder.setText(folderpath) #affichage du chemin de dossier
        #self.ihm.saving_folder=folderpath #mis à jour du nouveau répertoire dans IHM 

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(721, 731)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(480, 50, 221, 41))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.accepted.connect(self.launchTitration)
        self.experience_name = QtWidgets.QPlainTextEdit(Dialog)
        self.experience_name.setGeometry(QtCore.QRect(10, 50, 450, 41))
        self.experience_name.setPlainText("")
        self.experience_name.setObjectName("experience_name")
        self.description = QtWidgets.QPlainTextEdit(Dialog)
        self.description.setGeometry(QtCore.QRect(10, 140, 701, 161))
        self.description.setPlainText("")
        self.description.setObjectName("description")
        self.flowcell = QtWidgets.QComboBox(Dialog)
        self.flowcell.setGeometry(QtCore.QRect(20, 530, 351, 41))
        self.flowcell.setObjectName("flowcell")
        self.flowcell.addItem("")
        self.flowcell.addItem("")
        self.flowcell.addItem("")
        self.fibers = QtWidgets.QComboBox(Dialog)
        self.fibers.setGeometry(QtCore.QRect(20, 440, 351, 41))
        self.fibers.setObjectName("fibers")
        self.fibers.addItem("")
        self.fibers.addItem("")
        self.fibers.addItem("")
        self.label_name = QtWidgets.QLabel(Dialog)
        self.label_name.setGeometry(QtCore.QRect(10, 10, 241, 41))
        self.label_name.setObjectName("label_name")
        self.label_OM = QtWidgets.QLabel(Dialog)
        self.label_OM.setGeometry(QtCore.QRect(20, 310, 161, 41))
        self.label_OM.setObjectName("label_OM")
        self.label_concentration = QtWidgets.QLabel(Dialog)
        self.label_concentration.setGeometry(QtCore.QRect(200, 310, 151, 41))
        self.label_concentration.setObjectName("label_concentration")
        self.label_description = QtWidgets.QLabel(Dialog)
        self.label_description.setGeometry(QtCore.QRect(10, 100, 181, 41))
        self.label_description.setObjectName("label_description")

        self.OM_type = QtWidgets.QComboBox(Dialog)
        self.OM_type.setGeometry(QtCore.QRect(20, 350, 151, 41))
        self.OM_type.setEditable(True)
        self.OM_type.setMaxVisibleItems(10)
        self.OM_type.setObjectName("OM_type")
        self.OM_type.addItem("")
        self.OM_type.addItem("")
        self.concentration = QtWidgets.QDoubleSpinBox(Dialog)
        self.concentration.setGeometry(QtCore.QRect(200, 350, 171, 41))
        self.concentration.setDecimals(1)
        self.concentration.setMinimum(0.1)
        self.concentration.setSingleStep(0.1)
        self.concentration.setProperty("value", 1.0)
        self.concentration.setObjectName("concentration")
        self.label_fiber = QtWidgets.QLabel(Dialog)
        self.label_fiber.setGeometry(QtCore.QRect(20, 400, 351, 41))
        self.label_fiber.setObjectName("label_fiber")
        self.label_flowcell = QtWidgets.QLabel(Dialog)
        self.label_flowcell.setGeometry(QtCore.QRect(20, 490, 351, 41))
        self.label_flowcell.setObjectName("label_flowcell")
        
        self.Nmes = QtWidgets.QSpinBox(Dialog)
        self.Nmes.setGeometry(QtCore.QRect(580, 530, 121, 41))
        self.Nmes.setMinimum(3)
        self.Nmes.setMaximum(20)
        self.Nmes.setProperty("value", 10)
        self.Nmes.setObjectName("Nmes")
        self.pH_init_label = QtWidgets.QLabel(Dialog)
        self.pH_init_label.setGeometry(QtCore.QRect(420, 400, 111, 41))
        self.pH_init_label.setObjectName("pH_init_label")
        self.pH_fin_label = QtWidgets.QLabel(Dialog)
        self.pH_fin_label.setGeometry(QtCore.QRect(580, 400, 121, 41))
        self.pH_fin_label.setObjectName("pH_fin_label")
        self.Nmes_label = QtWidgets.QLabel(Dialog)
        self.Nmes_label.setGeometry(QtCore.QRect(450, 530, 131, 41))
        self.Nmes_label.setObjectName("Nmes_label")
        self.pH_init = QtWidgets.QDoubleSpinBox(Dialog)
        self.pH_init.setGeometry(QtCore.QRect(420, 440, 121, 41))
        self.pH_init.setDecimals(1)
        self.pH_init.setMinimum(3.0)
        self.pH_init.setMaximum(5.0)
        self.pH_init.setSingleStep(0.1)
        self.pH_init.setProperty("value", 4.0)
        self.pH_init.setObjectName("pH_init")
        self.pH_fin = QtWidgets.QDoubleSpinBox(Dialog)
        self.pH_fin.setGeometry(QtCore.QRect(580, 440, 121, 41))
        self.pH_fin.setDecimals(1)
        self.pH_fin.setMinimum(8.0)
        self.pH_fin.setMaximum(10.0)
        self.pH_fin.setSingleStep(0.1)
        self.pH_fin.setProperty("value", 9.0)
        self.pH_fin.setObjectName("pH_fin")
        self.dispense_mode = QtWidgets.QComboBox(Dialog)
        self.dispense_mode.setGeometry(QtCore.QRect(420, 350, 281, 41))
        self.dispense_mode.setEditable(True)
        self.dispense_mode.setMaxVisibleItems(10)
        self.dispense_mode.setObjectName("dispense_mode")
        self.dispense_mode.addItem("fixed volumes")
        self.dispense_mode.addItem("fit on 5/05/2023")
        self.dispense_mode.addItem("complete processing")
        self.dispense_mode_label = QtWidgets.QLabel(Dialog)
        self.dispense_mode_label.setGeometry(QtCore.QRect(420, 310, 261, 41))
        self.dispense_mode_label.setObjectName("dispense_mode_label")
        self.saving_folder = QtWidgets.QLineEdit(Dialog)
        self.saving_folder.setGeometry(QtCore.QRect(20, 660, 681, 41))
        self.saving_folder.setText(self.ihm.saving_folder)
        self.saving_folder.setObjectName("saving_folder")
        self.saving_folder_label = QtWidgets.QLabel(Dialog)
        self.saving_folder_label.setGeometry(QtCore.QRect(20, 620, 351, 41))
        self.saving_folder_label.setObjectName("saving_folder_label")
        self.browse = QtWidgets.QToolButton(Dialog)
        self.browse.setGeometry(QtCore.QRect(230, 610, 161, 41))
        self.browse.setObjectName("browse")
        self.browse.clicked.connect(self.browsefolder) #browse folder

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
        self.pH_init_label.setText(_translate("Dialog", "pH initial"))
        self.pH_fin_label.setText(_translate("Dialog", "pH final"))
        self.Nmes_label.setText(_translate("Dialog", "N mesures"))
        self.saving_folder_label.setText(_translate("Dialog", "Saving folder"))
        self.browse.setText(_translate("Dialog", "browse"))

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
