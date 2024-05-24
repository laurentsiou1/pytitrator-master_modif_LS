# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files/syringe_panel.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SyringePanel(object):
    def setupUi(self, SyringePanel):
        SyringePanel.setObjectName("SyringePanel")
        SyringePanel.resize(640, 480)
        SyringePanel.setAccessibleName("")
        self.levelbar1 = QtWidgets.QProgressBar(SyringePanel)
        self.levelbar1.setGeometry(QtCore.QRect(190, 290, 41, 101))
        self.levelbar1.setMinimum(0)
        self.levelbar1.setMaximum(500)
        self.levelbar1.setProperty("value", 50)
        self.levelbar1.setTextVisible(False)
        self.levelbar1.setOrientation(QtCore.Qt.Vertical)
        self.levelbar1.setInvertedAppearance(False)
        self.levelbar1.setObjectName("levelbar1")
        self.label_base_level = QtWidgets.QLabel(SyringePanel)
        self.label_base_level.setGeometry(QtCore.QRect(20, 400, 251, 41))
        self.label_base_level.setAutoFillBackground(False)
        self.label_base_level.setObjectName("label_base_level")
        self.level1_uL = QtWidgets.QLabel(SyringePanel)
        self.level1_uL.setGeometry(QtCore.QRect(150, 400, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.level1_uL.setFont(font)
        self.level1_uL.setAlignment(QtCore.Qt.AlignCenter)
        self.level1_uL.setObjectName("level1_uL")
        self.label_syringe1 = QtWidgets.QLabel(SyringePanel)
        self.label_syringe1.setGeometry(QtCore.QRect(160, 10, 101, 31))
        self.label_syringe1.setAutoFillBackground(False)
        self.label_syringe1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_syringe1.setObjectName("label_syringe1")
        self.label_syringe2 = QtWidgets.QLabel(SyringePanel)
        self.label_syringe2.setGeometry(QtCore.QRect(330, 10, 101, 31))
        self.label_syringe2.setAutoFillBackground(False)
        self.label_syringe2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_syringe2.setObjectName("label_syringe2")
        self.label_syringe3 = QtWidgets.QLabel(SyringePanel)
        self.label_syringe3.setGeometry(QtCore.QRect(500, 10, 101, 31))
        self.label_syringe3.setAutoFillBackground(False)
        self.label_syringe3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_syringe3.setObjectName("label_syringe3")
        self.level2_uL = QtWidgets.QLabel(SyringePanel)
        self.level2_uL.setGeometry(QtCore.QRect(320, 400, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.level2_uL.setFont(font)
        self.level2_uL.setAlignment(QtCore.Qt.AlignCenter)
        self.level2_uL.setObjectName("level2_uL")
        self.levelbar2 = QtWidgets.QProgressBar(SyringePanel)
        self.levelbar2.setGeometry(QtCore.QRect(360, 290, 41, 101))
        self.levelbar2.setMinimum(0)
        self.levelbar2.setMaximum(500)
        self.levelbar2.setProperty("value", 500)
        self.levelbar2.setTextVisible(False)
        self.levelbar2.setOrientation(QtCore.Qt.Vertical)
        self.levelbar2.setInvertedAppearance(False)
        self.levelbar2.setObjectName("levelbar2")
        self.level3_uL = QtWidgets.QLabel(SyringePanel)
        self.level3_uL.setGeometry(QtCore.QRect(490, 400, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.level3_uL.setFont(font)
        self.level3_uL.setAlignment(QtCore.Qt.AlignCenter)
        self.level3_uL.setObjectName("level3_uL")
        self.levelbar3 = QtWidgets.QProgressBar(SyringePanel)
        self.levelbar3.setGeometry(QtCore.QRect(530, 290, 41, 101))
        self.levelbar3.setMinimum(0)
        self.levelbar3.setMaximum(500)
        self.levelbar3.setProperty("value", 100)
        self.levelbar3.setTextVisible(False)
        self.levelbar3.setOrientation(QtCore.Qt.Vertical)
        self.levelbar3.setInvertedAppearance(False)
        self.levelbar3.setObjectName("levelbar3")
        self.C1_M = QtWidgets.QDoubleSpinBox(SyringePanel)
        self.C1_M.setGeometry(QtCore.QRect(160, 190, 101, 51))
        self.C1_M.setDecimals(6)
        self.C1_M.setMinimum(1e-06)
        self.C1_M.setMaximum(10.0)
        self.C1_M.setSingleStep(1e-06)
        self.C1_M.setProperty("value", 0.1)
        self.C1_M.setObjectName("C1_M")
        self.C2_M = QtWidgets.QDoubleSpinBox(SyringePanel)
        self.C2_M.setGeometry(QtCore.QRect(330, 190, 101, 51))
        self.C2_M.setDecimals(6)
        self.C2_M.setMinimum(1e-06)
        self.C2_M.setMaximum(10.0)
        self.C2_M.setSingleStep(1e-06)
        self.C2_M.setProperty("value", 0.01)
        self.C2_M.setObjectName("C2_M")
        self.C3_M = QtWidgets.QDoubleSpinBox(SyringePanel)
        self.C3_M.setGeometry(QtCore.QRect(500, 190, 101, 51))
        self.C3_M.setDecimals(6)
        self.C3_M.setMinimum(1e-06)
        self.C3_M.setMaximum(10.0)
        self.C3_M.setSingleStep(1e-06)
        self.C3_M.setProperty("value", 0.001)
        self.C3_M.setObjectName("C3_M")
        self.reagant1 = QtWidgets.QTextEdit(SyringePanel)
        self.reagant1.setGeometry(QtCore.QRect(160, 80, 104, 64))
        self.reagant1.setObjectName("reagant1")
        self.reagent2 = QtWidgets.QTextEdit(SyringePanel)
        self.reagent2.setGeometry(QtCore.QRect(330, 80, 104, 64))
        self.reagent2.setObjectName("reagent2")
        self.reagent3 = QtWidgets.QTextEdit(SyringePanel)
        self.reagent3.setGeometry(QtCore.QRect(500, 80, 104, 64))
        self.reagent3.setObjectName("reagent3")
        self.label = QtWidgets.QLabel(SyringePanel)
        self.label.setGeometry(QtCore.QRect(20, 80, 131, 61))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(SyringePanel)
        self.label_2.setGeometry(QtCore.QRect(20, 190, 131, 51))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(SyringePanel)
        QtCore.QMetaObject.connectSlotsByName(SyringePanel)

    def retranslateUi(self, SyringePanel):
        _translate = QtCore.QCoreApplication.translate
        SyringePanel.setWindowTitle(_translate("SyringePanel", "Syringe Panel"))
        self.levelbar1.setFormat(_translate("SyringePanel", "%p%"))
        self.label_base_level.setText(_translate("SyringePanel", "levels (0 - 500uL)"))
        self.level1_uL.setText(_translate("SyringePanel", "0 uL"))
        self.label_syringe1.setText(_translate("SyringePanel", "Syringe 1"))
        self.label_syringe2.setText(_translate("SyringePanel", "Syringe 2"))
        self.label_syringe3.setText(_translate("SyringePanel", "Syringe 3"))
        self.level2_uL.setText(_translate("SyringePanel", "0 uL"))
        self.levelbar2.setFormat(_translate("SyringePanel", "%p%"))
        self.level3_uL.setText(_translate("SyringePanel", "0 uL"))
        self.levelbar3.setFormat(_translate("SyringePanel", "%p%"))
        self.reagant1.setHtml(_translate("SyringePanel", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Acid (Hcl)</p></body></html>"))
        self.reagent2.setHtml(_translate("SyringePanel", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Base (NaOH)</p></body></html>"))
        self.reagent3.setHtml(_translate("SyringePanel", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Reagent 3 (Unknown)</p></body></html>"))
        self.label.setText(_translate("SyringePanel", "Reagents"))
        self.label_2.setText(_translate("SyringePanel", "Concentrations"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SyringePanel = QtWidgets.QWidget()
    ui = Ui_SyringePanel()
    ui.setupUi(SyringePanel)
    SyringePanel.show()
    sys.exit(app.exec_())
