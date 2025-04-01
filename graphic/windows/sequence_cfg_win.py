# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'graphic/ui_files/sequence_cfg.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_sequenceConfig(object):
    def setupUi(self, sequenceConfig):
        sequenceConfig.setObjectName("sequenceConfig")
        sequenceConfig.resize(770, 832)
        sequenceConfig.setSizeGripEnabled(False)
        self.dialogbox = QtWidgets.QDialogButtonBox(sequenceConfig)
        self.dialogbox.setGeometry(QtCore.QRect(440, 770, 311, 61))
        self.dialogbox.setOrientation(QtCore.Qt.Horizontal)
        self.dialogbox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.dialogbox.setObjectName("dialogbox")
        self.exp_name = QtWidgets.QPlainTextEdit(sequenceConfig)
        self.exp_name.setGeometry(QtCore.QRect(20, 40, 351, 41))
        self.exp_name.setPlainText("")
        self.exp_name.setObjectName("exp_name")
        self.exp_name_label = QtWidgets.QLabel(sequenceConfig)
        self.exp_name_label.setGeometry(QtCore.QRect(20, 0, 241, 41))
        self.exp_name_label.setObjectName("exp_name_label")
        self.description_label = QtWidgets.QLabel(sequenceConfig)
        self.description_label.setGeometry(QtCore.QRect(20, 90, 181, 41))
        self.description_label.setObjectName("description_label")
        self.description = QtWidgets.QPlainTextEdit(sequenceConfig)
        self.description.setGeometry(QtCore.QRect(20, 130, 351, 141))
        self.description.setPlainText("")
        self.description.setObjectName("description")
        self.Nmes = QtWidgets.QSpinBox(sequenceConfig)
        self.Nmes.setGeometry(QtCore.QRect(580, 490, 121, 41))
        self.Nmes.setMinimum(3)
        self.Nmes.setMaximum(30)
        self.Nmes.setProperty("value", 20)
        self.Nmes.setObjectName("Nmes")
        self.pH_init_label = QtWidgets.QLabel(sequenceConfig)
        self.pH_init_label.setGeometry(QtCore.QRect(410, 390, 111, 41))
        self.pH_init_label.setObjectName("pH_init_label")
        self.pH_fin_label = QtWidgets.QLabel(sequenceConfig)
        self.pH_fin_label.setGeometry(QtCore.QRect(410, 500, 121, 41))
        self.pH_fin_label.setObjectName("pH_fin_label")
        self.Nmes_label = QtWidgets.QLabel(sequenceConfig)
        self.Nmes_label.setGeometry(QtCore.QRect(580, 450, 121, 41))
        self.Nmes_label.setObjectName("Nmes_label")
        self.pH_init = QtWidgets.QDoubleSpinBox(sequenceConfig)
        self.pH_init.setGeometry(QtCore.QRect(410, 430, 121, 41))
        self.pH_init.setDecimals(1)
        self.pH_init.setMinimum(3.0)
        self.pH_init.setMaximum(5.0)
        self.pH_init.setSingleStep(0.1)
        self.pH_init.setProperty("value", 4.0)
        self.pH_init.setObjectName("pH_init")
        self.pH_fin = QtWidgets.QDoubleSpinBox(sequenceConfig)
        self.pH_fin.setGeometry(QtCore.QRect(410, 540, 121, 41))
        self.pH_fin.setDecimals(1)
        self.pH_fin.setMinimum(8.0)
        self.pH_fin.setMaximum(10.0)
        self.pH_fin.setSingleStep(0.1)
        self.pH_fin.setProperty("value", 10.0)
        self.pH_fin.setObjectName("pH_fin")
        self.dispense_mode = QtWidgets.QComboBox(sequenceConfig)
        self.dispense_mode.setGeometry(QtCore.QRect(20, 340, 281, 41))
        self.dispense_mode.setEditable(True)
        self.dispense_mode.setMaxVisibleItems(10)
        self.dispense_mode.setObjectName("dispense_mode")
        self.dispense_mode.addItem("")
        self.dispense_mode.addItem("")
        self.dispense_mode.addItem("")
        self.dispense_mode.addItem("")
        self.dispense_mode.addItem("")
        self.dispense_mode_label = QtWidgets.QLabel(sequenceConfig)
        self.dispense_mode_label.setGeometry(QtCore.QRect(20, 300, 261, 41))
        self.dispense_mode_label.setObjectName("dispense_mode_label")
        self.saving_folder_label = QtWidgets.QLabel(sequenceConfig)
        self.saving_folder_label.setGeometry(QtCore.QRect(30, 680, 351, 41))
        self.saving_folder_label.setObjectName("saving_folder_label")
        self.V_init = QtWidgets.QDoubleSpinBox(sequenceConfig)
        self.V_init.setEnabled(True)
        self.V_init.setGeometry(QtCore.QRect(500, 230, 121, 41))
        self.V_init.setAccessibleDescription("")
        self.V_init.setAutoFillBackground(False)
        self.V_init.setWrapping(False)
        self.V_init.setDecimals(3)
        self.V_init.setMinimum(0.0)
        self.V_init.setMaximum(2000.0)
        self.V_init.setSingleStep(0.01)
        self.V_init.setProperty("value", 0.0)
        self.V_init.setObjectName("V_init")
        self.Vinit_label = QtWidgets.QLabel(sequenceConfig)
        self.Vinit_label.setGeometry(QtCore.QRect(420, 190, 261, 41))
        self.Vinit_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Vinit_label.setObjectName("Vinit_label")
        self.flow_delay_label = QtWidgets.QLabel(sequenceConfig)
        self.flow_delay_label.setGeometry(QtCore.QRect(50, 500, 291, 41))
        self.flow_delay_label.setAlignment(QtCore.Qt.AlignCenter)
        self.flow_delay_label.setObjectName("flow_delay_label")
        self.fixed_delay_box = QtWidgets.QSpinBox(sequenceConfig)
        self.fixed_delay_box.setGeometry(QtCore.QRect(150, 540, 91, 41))
        self.fixed_delay_box.setMaximum(7200)
        self.fixed_delay_box.setProperty("value", 270)
        self.fixed_delay_box.setObjectName("fixed_delay_box")
        self.mixing_delay_label = QtWidgets.QLabel(sequenceConfig)
        self.mixing_delay_label.setGeometry(QtCore.QRect(110, 390, 171, 41))
        self.mixing_delay_label.setAlignment(QtCore.Qt.AlignCenter)
        self.mixing_delay_label.setObjectName("mixing_delay_label")
        self.agitation_delay_box = QtWidgets.QSpinBox(sequenceConfig)
        self.agitation_delay_box.setGeometry(QtCore.QRect(150, 430, 91, 41))
        self.agitation_delay_box.setMaximum(300)
        self.agitation_delay_box.setProperty("value", 30)
        self.agitation_delay_box.setObjectName("agitation_delay_box")
        self.browse = QtWidgets.QToolButton(sequenceConfig)
        self.browse.setEnabled(True)
        self.browse.setGeometry(QtCore.QRect(620, 720, 131, 41))
        self.browse.setCheckable(False)
        self.browse.setAutoRaise(False)
        self.browse.setObjectName("browse")
        self.saving_folder = QtWidgets.QLineEdit(sequenceConfig)
        self.saving_folder.setGeometry(QtCore.QRect(20, 720, 561, 41))
        self.saving_folder.setObjectName("saving_folder")
        self.sequence_config_file = QtWidgets.QLineEdit(sequenceConfig)
        self.sequence_config_file.setGeometry(QtCore.QRect(20, 630, 561, 41))
        self.sequence_config_file.setObjectName("sequence_config_file")
        self.browse1 = QtWidgets.QToolButton(sequenceConfig)
        self.browse1.setEnabled(True)
        self.browse1.setGeometry(QtCore.QRect(620, 630, 131, 41))
        self.browse1.setCheckable(False)
        self.browse1.setAutoRaise(False)
        self.browse1.setObjectName("browse1")
        self.sequence_config_label = QtWidgets.QLabel(sequenceConfig)
        self.sequence_config_label.setGeometry(QtCore.QRect(30, 590, 351, 41))
        self.sequence_config_label.setObjectName("sequence_config_label")
        self.atmosphere_label = QtWidgets.QLabel(sequenceConfig)
        self.atmosphere_label.setGeometry(QtCore.QRect(430, 30, 261, 41))
        self.atmosphere_label.setAlignment(QtCore.Qt.AlignCenter)
        self.atmosphere_label.setObjectName("atmosphere_label")
        self.atmosphere_box = QtWidgets.QComboBox(sequenceConfig)
        self.atmosphere_box.setGeometry(QtCore.QRect(500, 70, 121, 41))
        self.atmosphere_box.setObjectName("atmosphere_box")
        self.atmosphere_box.addItem("")
        self.atmosphere_box.addItem("")

        self.retranslateUi(sequenceConfig)
        self.dialogbox.accepted.connect(sequenceConfig.accept) # type: ignore
        self.dialogbox.rejected.connect(sequenceConfig.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(sequenceConfig)

    def retranslateUi(self, sequenceConfig):
        _translate = QtCore.QCoreApplication.translate
        sequenceConfig.setWindowTitle(_translate("sequenceConfig", "Sequence configuration"))
        self.exp_name_label.setText(_translate("sequenceConfig", "Experience name"))
        self.description_label.setText(_translate("sequenceConfig", "Description"))
        self.pH_init_label.setText(_translate("sequenceConfig", "initial pH"))
        self.pH_fin_label.setText(_translate("sequenceConfig", "final pH"))
        self.Nmes_label.setText(_translate("sequenceConfig", "N mesures"))
        self.dispense_mode.setCurrentText(_translate("sequenceConfig", "variable step"))
        self.dispense_mode.setItemText(0, _translate("sequenceConfig", "variable step"))
        self.dispense_mode.setItemText(1, _translate("sequenceConfig", "fixed step"))
        self.dispense_mode.setItemText(2, _translate("sequenceConfig", "with feedback"))
        self.dispense_mode.setItemText(3, _translate("sequenceConfig", "fixed volumes"))
        self.dispense_mode.setItemText(4, _translate("sequenceConfig", "from file"))
        self.dispense_mode_label.setText(_translate("sequenceConfig", "Dispense mode"))
        self.saving_folder_label.setText(_translate("sequenceConfig", "Saving folder"))
        self.Vinit_label.setText(_translate("sequenceConfig", "Initial Volume (mL)"))
        self.flow_delay_label.setText(_translate("sequenceConfig", "flow delay (seconds)"))
        self.mixing_delay_label.setText(_translate("sequenceConfig", "Mixing delay (seconds)"))
        self.browse.setText(_translate("sequenceConfig", "Browse"))
        self.browse1.setText(_translate("sequenceConfig", "Browse"))
        self.sequence_config_label.setText(_translate("sequenceConfig", "Sequence configuration file"))
        self.atmosphere_label.setText(_translate("sequenceConfig", "Ambiant atmosphere"))
        self.atmosphere_box.setItemText(0, _translate("sequenceConfig", "True"))
        self.atmosphere_box.setItemText(1, _translate("sequenceConfig", "False"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    sequenceConfig = QtWidgets.QDialog()
    ui = Ui_sequenceConfig()
    ui.setupUi(sequenceConfig)
    sequenceConfig.show()
    sys.exit(app.exec_())
