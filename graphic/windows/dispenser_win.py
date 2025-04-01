# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'graphic/ui_files/dispenser.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SyringePanel(object):
    def setupUi(self, SyringePanel):
        SyringePanel.setObjectName("SyringePanel")
        SyringePanel.resize(1071, 720)
        SyringePanel.setAccessibleName("")
        self.label_level = QtWidgets.QLabel(SyringePanel)
        self.label_level.setGeometry(QtCore.QRect(90, 300, 111, 71))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_level.setFont(font)
        self.label_level.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_level.setAutoFillBackground(False)
        self.label_level.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_level.setObjectName("label_level")
        self.levelA_uL = QtWidgets.QLabel(SyringePanel)
        self.levelA_uL.setGeometry(QtCore.QRect(390, 410, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.levelA_uL.setFont(font)
        self.levelA_uL.setAlignment(QtCore.Qt.AlignCenter)
        self.levelA_uL.setObjectName("levelA_uL")
        self.levelB_uL = QtWidgets.QLabel(SyringePanel)
        self.levelB_uL.setGeometry(QtCore.QRect(650, 400, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.levelB_uL.setFont(font)
        self.levelB_uL.setAlignment(QtCore.Qt.AlignCenter)
        self.levelB_uL.setObjectName("levelB_uL")
        self.levelbarB = QtWidgets.QProgressBar(SyringePanel)
        self.levelbarB.setGeometry(QtCore.QRect(690, 280, 41, 121))
        self.levelbarB.setMinimum(0)
        self.levelbarB.setMaximum(500)
        self.levelbarB.setProperty("value", -1)
        self.levelbarB.setTextVisible(False)
        self.levelbarB.setOrientation(QtCore.Qt.Vertical)
        self.levelbarB.setInvertedAppearance(False)
        self.levelbarB.setObjectName("levelbarB")
        self.levelC_uL = QtWidgets.QLabel(SyringePanel)
        self.levelC_uL.setGeometry(QtCore.QRect(910, 400, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.levelC_uL.setFont(font)
        self.levelC_uL.setAlignment(QtCore.Qt.AlignCenter)
        self.levelC_uL.setObjectName("levelC_uL")
        self.levelbarC = QtWidgets.QProgressBar(SyringePanel)
        self.levelbarC.setGeometry(QtCore.QRect(950, 280, 41, 121))
        self.levelbarC.setMinimum(0)
        self.levelbarC.setMaximum(500)
        self.levelbarC.setProperty("value", 0)
        self.levelbarC.setTextVisible(False)
        self.levelbarC.setOrientation(QtCore.Qt.Vertical)
        self.levelbarC.setInvertedAppearance(False)
        self.levelbarC.setObjectName("levelbarC")
        self.label_reagent = QtWidgets.QLabel(SyringePanel)
        self.label_reagent.setGeometry(QtCore.QRect(40, 80, 211, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_reagent.setFont(font)
        self.label_reagent.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_reagent.setObjectName("label_reagent")
        self.label_concentration = QtWidgets.QLabel(SyringePanel)
        self.label_concentration.setGeometry(QtCore.QRect(40, 140, 211, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_concentration.setFont(font)
        self.label_concentration.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_concentration.setObjectName("label_concentration")
        self.dispense_box_B = QtWidgets.QSpinBox(SyringePanel)
        self.dispense_box_B.setGeometry(QtCore.QRect(700, 590, 71, 31))
        self.dispense_box_B.setMaximum(500)
        self.dispense_box_B.setObjectName("dispense_box_B")
        self.dispense_button_B = QtWidgets.QPushButton(SyringePanel)
        self.dispense_button_B.setGeometry(QtCore.QRect(590, 590, 101, 31))
        self.dispense_button_B.setObjectName("dispense_button_B")
        self.unload_button_A = QtWidgets.QPushButton(SyringePanel)
        self.unload_button_A.setGeometry(QtCore.QRect(330, 550, 101, 31))
        self.unload_button_A.setObjectName("unload_button_A")
        self.unload_button_B = QtWidgets.QPushButton(SyringePanel)
        self.unload_button_B.setGeometry(QtCore.QRect(590, 550, 101, 31))
        self.unload_button_B.setObjectName("unload_button_B")
        self.make_ref_B = QtWidgets.QPushButton(SyringePanel)
        self.make_ref_B.setGeometry(QtCore.QRect(710, 470, 51, 31))
        self.make_ref_B.setObjectName("make_ref_B")
        self.dispense_box_C = QtWidgets.QSpinBox(SyringePanel)
        self.dispense_box_C.setGeometry(QtCore.QRect(960, 590, 71, 31))
        self.dispense_box_C.setMaximum(500)
        self.dispense_box_C.setObjectName("dispense_box_C")
        self.dispense_button_A = QtWidgets.QPushButton(SyringePanel)
        self.dispense_button_A.setGeometry(QtCore.QRect(330, 590, 101, 31))
        self.dispense_button_A.setObjectName("dispense_button_A")
        self.unload_box_A = QtWidgets.QSpinBox(SyringePanel)
        self.unload_box_A.setGeometry(QtCore.QRect(440, 550, 71, 31))
        self.unload_box_A.setMaximum(500)
        self.unload_box_A.setObjectName("unload_box_A")
        self.make_ref_C = QtWidgets.QPushButton(SyringePanel)
        self.make_ref_C.setGeometry(QtCore.QRect(970, 470, 51, 31))
        self.make_ref_C.setObjectName("make_ref_C")
        self.load_button_B = QtWidgets.QPushButton(SyringePanel)
        self.load_button_B.setGeometry(QtCore.QRect(590, 510, 101, 31))
        self.load_button_B.setObjectName("load_button_B")
        self.full_reload_button_B = QtWidgets.QPushButton(SyringePanel)
        self.full_reload_button_B.setGeometry(QtCore.QRect(590, 470, 101, 31))
        self.full_reload_button_B.setObjectName("full_reload_button_B")
        self.dispense_button_C = QtWidgets.QPushButton(SyringePanel)
        self.dispense_button_C.setGeometry(QtCore.QRect(850, 590, 101, 31))
        self.dispense_button_C.setObjectName("dispense_button_C")
        self.full_reload_button_C = QtWidgets.QPushButton(SyringePanel)
        self.full_reload_button_C.setGeometry(QtCore.QRect(850, 470, 101, 31))
        self.full_reload_button_C.setObjectName("full_reload_button_C")
        self.load_box_A = QtWidgets.QSpinBox(SyringePanel)
        self.load_box_A.setGeometry(QtCore.QRect(440, 510, 71, 31))
        self.load_box_A.setMaximum(500)
        self.load_box_A.setObjectName("load_box_A")
        self.load_box_B = QtWidgets.QSpinBox(SyringePanel)
        self.load_box_B.setGeometry(QtCore.QRect(700, 510, 71, 31))
        self.load_box_B.setMaximum(500)
        self.load_box_B.setObjectName("load_box_B")
        self.unload_box_C = QtWidgets.QSpinBox(SyringePanel)
        self.unload_box_C.setGeometry(QtCore.QRect(960, 550, 71, 31))
        self.unload_box_C.setMaximum(500)
        self.unload_box_C.setObjectName("unload_box_C")
        self.full_reload_button_A = QtWidgets.QPushButton(SyringePanel)
        self.full_reload_button_A.setGeometry(QtCore.QRect(330, 470, 101, 31))
        self.full_reload_button_A.setObjectName("full_reload_button_A")
        self.load_button_C = QtWidgets.QPushButton(SyringePanel)
        self.load_button_C.setGeometry(QtCore.QRect(850, 510, 101, 31))
        self.load_button_C.setObjectName("load_button_C")
        self.dispense_box_A = QtWidgets.QSpinBox(SyringePanel)
        self.dispense_box_A.setGeometry(QtCore.QRect(440, 590, 71, 31))
        self.dispense_box_A.setMaximum(500)
        self.dispense_box_A.setObjectName("dispense_box_A")
        self.make_ref_A = QtWidgets.QPushButton(SyringePanel)
        self.make_ref_A.setGeometry(QtCore.QRect(450, 470, 51, 31))
        self.make_ref_A.setObjectName("make_ref_A")
        self.unload_box_B = QtWidgets.QSpinBox(SyringePanel)
        self.unload_box_B.setGeometry(QtCore.QRect(700, 550, 71, 31))
        self.unload_box_B.setMaximum(500)
        self.unload_box_B.setObjectName("unload_box_B")
        self.load_box_C = QtWidgets.QSpinBox(SyringePanel)
        self.load_box_C.setGeometry(QtCore.QRect(960, 510, 71, 31))
        self.load_box_C.setMaximum(500)
        self.load_box_C.setObjectName("load_box_C")
        self.load_button_A = QtWidgets.QPushButton(SyringePanel)
        self.load_button_A.setGeometry(QtCore.QRect(330, 510, 101, 31))
        self.load_button_A.setObjectName("load_button_A")
        self.unload_button_C = QtWidgets.QPushButton(SyringePanel)
        self.unload_button_C.setGeometry(QtCore.QRect(850, 550, 101, 31))
        self.unload_button_C.setObjectName("unload_button_C")
        self.line = QtWidgets.QFrame(SyringePanel)
        self.line.setGeometry(QtCore.QRect(540, 30, 21, 591))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(SyringePanel)
        self.line_2.setGeometry(QtCore.QRect(800, 30, 21, 591))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(SyringePanel)
        self.line_3.setGeometry(QtCore.QRect(280, 30, 21, 371))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.stop = QtWidgets.QPushButton(SyringePanel)
        self.stop.setGeometry(QtCore.QRect(110, 500, 81, 81))
        self.stop.setObjectName("stop")
        self.added_B_uL = QtWidgets.QLabel(SyringePanel)
        self.added_B_uL.setGeometry(QtCore.QRect(630, 640, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.added_B_uL.setFont(font)
        self.added_B_uL.setAlignment(QtCore.Qt.AlignCenter)
        self.added_B_uL.setObjectName("added_B_uL")
        self.added_C_uL = QtWidgets.QLabel(SyringePanel)
        self.added_C_uL.setGeometry(QtCore.QRect(890, 640, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.added_C_uL.setFont(font)
        self.added_C_uL.setAlignment(QtCore.Qt.AlignCenter)
        self.added_C_uL.setObjectName("added_C_uL")
        self.added_A_uL = QtWidgets.QLabel(SyringePanel)
        self.added_A_uL.setGeometry(QtCore.QRect(370, 640, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.added_A_uL.setFont(font)
        self.added_A_uL.setAlignment(QtCore.Qt.AlignCenter)
        self.added_A_uL.setObjectName("added_A_uL")
        self.added_total = QtWidgets.QLabel(SyringePanel)
        self.added_total.setGeometry(QtCore.QRect(370, 670, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.added_total.setFont(font)
        self.added_total.setAlignment(QtCore.Qt.AlignCenter)
        self.added_total.setObjectName("added_total")
        self.line_8 = QtWidgets.QFrame(SyringePanel)
        self.line_8.setGeometry(QtCore.QRect(330, 630, 701, 21))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.label_added_volume = QtWidgets.QLabel(SyringePanel)
        self.label_added_volume.setGeometry(QtCore.QRect(110, 640, 191, 31))
        self.label_added_volume.setAutoFillBackground(False)
        self.label_added_volume.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_added_volume.setObjectName("label_added_volume")
        self.line_9 = QtWidgets.QFrame(SyringePanel)
        self.line_9.setGeometry(QtCore.QRect(330, 660, 701, 21))
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.label_total_volume = QtWidgets.QLabel(SyringePanel)
        self.label_total_volume.setGeometry(QtCore.QRect(110, 670, 191, 31))
        self.label_total_volume.setAutoFillBackground(False)
        self.label_total_volume.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_total_volume.setObjectName("label_total_volume")
        self.line_10 = QtWidgets.QFrame(SyringePanel)
        self.line_10.setGeometry(QtCore.QRect(330, 690, 701, 21))
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.reset = QtWidgets.QPushButton(SyringePanel)
        self.reset.setGeometry(QtCore.QRect(50, 650, 91, 41))
        self.reset.setObjectName("reset")
        self.reagentA = QtWidgets.QLabel(SyringePanel)
        self.reagentA.setGeometry(QtCore.QRect(330, 80, 181, 51))
        self.reagentA.setAlignment(QtCore.Qt.AlignCenter)
        self.reagentA.setObjectName("reagentA")
        self.reagentB = QtWidgets.QLabel(SyringePanel)
        self.reagentB.setGeometry(QtCore.QRect(590, 80, 181, 51))
        self.reagentB.setAlignment(QtCore.Qt.AlignCenter)
        self.reagentB.setObjectName("reagentB")
        self.reagentC = QtWidgets.QLabel(SyringePanel)
        self.reagentC.setGeometry(QtCore.QRect(850, 80, 181, 51))
        self.reagentC.setAlignment(QtCore.Qt.AlignCenter)
        self.reagentC.setObjectName("reagentC")
        self.syringeA = QtWidgets.QLabel(SyringePanel)
        self.syringeA.setGeometry(QtCore.QRect(370, 20, 101, 51))
        self.syringeA.setAlignment(QtCore.Qt.AlignCenter)
        self.syringeA.setObjectName("syringeA")
        self.syringeB = QtWidgets.QLabel(SyringePanel)
        self.syringeB.setGeometry(QtCore.QRect(630, 20, 101, 51))
        self.syringeB.setAlignment(QtCore.Qt.AlignCenter)
        self.syringeB.setObjectName("syringeB")
        self.syringeC = QtWidgets.QLabel(SyringePanel)
        self.syringeC.setGeometry(QtCore.QRect(890, 20, 101, 51))
        self.syringeC.setAlignment(QtCore.Qt.AlignCenter)
        self.syringeC.setObjectName("syringeC")
        self.Ca = QtWidgets.QLabel(SyringePanel)
        self.Ca.setGeometry(QtCore.QRect(330, 140, 181, 51))
        self.Ca.setAlignment(QtCore.Qt.AlignCenter)
        self.Ca.setObjectName("Ca")
        self.Cb = QtWidgets.QLabel(SyringePanel)
        self.Cb.setGeometry(QtCore.QRect(590, 140, 181, 51))
        self.Cb.setAlignment(QtCore.Qt.AlignCenter)
        self.Cb.setObjectName("Cb")
        self.Cc = QtWidgets.QLabel(SyringePanel)
        self.Cc.setGeometry(QtCore.QRect(850, 140, 181, 51))
        self.Cc.setAlignment(QtCore.Qt.AlignCenter)
        self.Cc.setObjectName("Cc")
        self.levelbarA = QtWidgets.QProgressBar(SyringePanel)
        self.levelbarA.setGeometry(QtCore.QRect(430, 280, 41, 121))
        self.levelbarA.setMinimum(0)
        self.levelbarA.setMaximum(500)
        self.levelbarA.setProperty("value", -1)
        self.levelbarA.setTextVisible(False)
        self.levelbarA.setOrientation(QtCore.Qt.Vertical)
        self.levelbarA.setInvertedAppearance(False)
        self.levelbarA.setObjectName("levelbarA")
        self.purge_A_button = QtWidgets.QPushButton(SyringePanel)
        self.purge_A_button.setGeometry(QtCore.QRect(310, 350, 71, 51))
        self.purge_A_button.setObjectName("purge_A_button")
        self.purge_C_button = QtWidgets.QPushButton(SyringePanel)
        self.purge_C_button.setGeometry(QtCore.QRect(830, 350, 71, 51))
        self.purge_C_button.setObjectName("purge_C_button")
        self.purge_B_button = QtWidgets.QPushButton(SyringePanel)
        self.purge_B_button.setGeometry(QtCore.QRect(570, 340, 71, 51))
        self.purge_B_button.setObjectName("purge_B_button")
        self.dismantle_A_button = QtWidgets.QPushButton(SyringePanel)
        self.dismantle_A_button.setGeometry(QtCore.QRect(300, 280, 91, 31))
        self.dismantle_A_button.setObjectName("dismantle_A_button")
        self.valve_state_A = QtWidgets.QPushButton(SyringePanel)
        self.valve_state_A.setGeometry(QtCore.QRect(380, 200, 81, 51))
        self.valve_state_A.setObjectName("valve_state_A")
        self.label_electrovalve = QtWidgets.QLabel(SyringePanel)
        self.label_electrovalve.setGeometry(QtCore.QRect(40, 200, 211, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_electrovalve.setFont(font)
        self.label_electrovalve.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_electrovalve.setObjectName("label_electrovalve")
        self.valve_state_C = QtWidgets.QPushButton(SyringePanel)
        self.valve_state_C.setGeometry(QtCore.QRect(900, 200, 81, 51))
        self.valve_state_C.setObjectName("valve_state_C")
        self.valve_state_B = QtWidgets.QPushButton(SyringePanel)
        self.valve_state_B.setGeometry(QtCore.QRect(640, 200, 81, 51))
        self.valve_state_B.setObjectName("valve_state_B")
        self.dismantle_C_button = QtWidgets.QPushButton(SyringePanel)
        self.dismantle_C_button.setGeometry(QtCore.QRect(820, 280, 91, 31))
        self.dismantle_C_button.setObjectName("dismantle_C_button")
        self.dismantle_B_button = QtWidgets.QPushButton(SyringePanel)
        self.dismantle_B_button.setGeometry(QtCore.QRect(560, 280, 91, 31))
        self.dismantle_B_button.setObjectName("dismantle_B_button")
        self.label_level_2 = QtWidgets.QLabel(SyringePanel)
        self.label_level_2.setGeometry(QtCore.QRect(120, 350, 111, 41))
        self.label_level_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_level_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_level_2.setAutoFillBackground(False)
        self.label_level_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_level_2.setObjectName("label_level_2")
        self.label_level.raise_()
        self.levelA_uL.raise_()
        self.levelB_uL.raise_()
        self.levelbarB.raise_()
        self.levelC_uL.raise_()
        self.levelbarC.raise_()
        self.label_reagent.raise_()
        self.label_concentration.raise_()
        self.dispense_box_B.raise_()
        self.dispense_button_B.raise_()
        self.unload_button_A.raise_()
        self.unload_button_B.raise_()
        self.make_ref_B.raise_()
        self.dispense_box_C.raise_()
        self.dispense_button_A.raise_()
        self.unload_box_A.raise_()
        self.make_ref_C.raise_()
        self.load_button_B.raise_()
        self.full_reload_button_B.raise_()
        self.dispense_button_C.raise_()
        self.full_reload_button_C.raise_()
        self.load_box_A.raise_()
        self.load_box_B.raise_()
        self.unload_box_C.raise_()
        self.full_reload_button_A.raise_()
        self.load_button_C.raise_()
        self.dispense_box_A.raise_()
        self.make_ref_A.raise_()
        self.unload_box_B.raise_()
        self.load_box_C.raise_()
        self.load_button_A.raise_()
        self.unload_button_C.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.line_3.raise_()
        self.stop.raise_()
        self.added_B_uL.raise_()
        self.added_C_uL.raise_()
        self.added_A_uL.raise_()
        self.added_total.raise_()
        self.line_8.raise_()
        self.label_added_volume.raise_()
        self.line_9.raise_()
        self.label_total_volume.raise_()
        self.line_10.raise_()
        self.reset.raise_()
        self.reagentA.raise_()
        self.reagentB.raise_()
        self.reagentC.raise_()
        self.syringeA.raise_()
        self.syringeB.raise_()
        self.syringeC.raise_()
        self.Ca.raise_()
        self.Cb.raise_()
        self.Cc.raise_()
        self.purge_A_button.raise_()
        self.purge_C_button.raise_()
        self.purge_B_button.raise_()
        self.dismantle_A_button.raise_()
        self.valve_state_A.raise_()
        self.label_electrovalve.raise_()
        self.valve_state_C.raise_()
        self.valve_state_B.raise_()
        self.dismantle_C_button.raise_()
        self.dismantle_B_button.raise_()
        self.levelbarA.raise_()
        self.label_level_2.raise_()

        self.retranslateUi(SyringePanel)
        QtCore.QMetaObject.connectSlotsByName(SyringePanel)

    def retranslateUi(self, SyringePanel):
        _translate = QtCore.QCoreApplication.translate
        SyringePanel.setWindowTitle(_translate("SyringePanel", "Syringe Panel"))
        self.label_level.setText(_translate("SyringePanel", "Dispensing range:"))
        self.levelA_uL.setText(_translate("SyringePanel", "0 uL"))
        self.levelB_uL.setText(_translate("SyringePanel", "0 uL"))
        self.levelbarB.setFormat(_translate("SyringePanel", "%p%"))
        self.levelC_uL.setText(_translate("SyringePanel", "0 uL"))
        self.levelbarC.setFormat(_translate("SyringePanel", "%p%"))
        self.label_reagent.setText(_translate("SyringePanel", "Reagent"))
        self.label_concentration.setText(_translate("SyringePanel", "Concentration (mol/L)"))
        self.dispense_button_B.setText(_translate("SyringePanel", "dispense"))
        self.unload_button_A.setText(_translate("SyringePanel", "unload"))
        self.unload_button_B.setText(_translate("SyringePanel", "unload"))
        self.make_ref_B.setText(_translate("SyringePanel", "ref"))
        self.dispense_button_A.setText(_translate("SyringePanel", "dispense"))
        self.make_ref_C.setText(_translate("SyringePanel", "ref"))
        self.load_button_B.setText(_translate("SyringePanel", "load"))
        self.full_reload_button_B.setText(_translate("SyringePanel", "full reload"))
        self.dispense_button_C.setText(_translate("SyringePanel", "dispense"))
        self.full_reload_button_C.setText(_translate("SyringePanel", "full reload"))
        self.full_reload_button_A.setText(_translate("SyringePanel", "full reload"))
        self.load_button_C.setText(_translate("SyringePanel", "load"))
        self.make_ref_A.setText(_translate("SyringePanel", "ref"))
        self.load_button_A.setText(_translate("SyringePanel", "load"))
        self.unload_button_C.setText(_translate("SyringePanel", "unload"))
        self.stop.setText(_translate("SyringePanel", "STOP"))
        self.added_B_uL.setText(_translate("SyringePanel", "0 uL"))
        self.added_C_uL.setText(_translate("SyringePanel", "0 uL"))
        self.added_A_uL.setText(_translate("SyringePanel", "0 uL"))
        self.added_total.setText(_translate("SyringePanel", "0 uL"))
        self.label_added_volume.setText(_translate("SyringePanel", "added volume (uL)"))
        self.label_total_volume.setText(_translate("SyringePanel", "total (uL)"))
        self.reset.setText(_translate("SyringePanel", "Reset"))
        self.reagentA.setText(_translate("SyringePanel", "Acid (HCl)"))
        self.reagentB.setText(_translate("SyringePanel", "Base (NaOH)"))
        self.reagentC.setText(_translate("SyringePanel", "Reagent unknown"))
        self.syringeA.setText(_translate("SyringePanel", "Syringe A"))
        self.syringeB.setText(_translate("SyringePanel", "Syringe B"))
        self.syringeC.setText(_translate("SyringePanel", "Syringe C"))
        self.Ca.setText(_translate("SyringePanel", "0.001"))
        self.Cb.setText(_translate("SyringePanel", "0.01"))
        self.Cc.setText(_translate("SyringePanel", "1"))
        self.levelbarA.setFormat(_translate("SyringePanel", "%p%"))
        self.purge_A_button.setText(_translate("SyringePanel", "auto\n"
"purge"))
        self.purge_C_button.setText(_translate("SyringePanel", "auto\n"
"purge"))
        self.purge_B_button.setText(_translate("SyringePanel", "auto\n"
"purge"))
        self.dismantle_A_button.setText(_translate("SyringePanel", "dismantle"))
        self.valve_state_A.setText(_translate("SyringePanel", "OFF"))
        self.label_electrovalve.setText(_translate("SyringePanel", "valve state"))
        self.valve_state_C.setText(_translate("SyringePanel", "OFF"))
        self.valve_state_B.setText(_translate("SyringePanel", "OFF"))
        self.dismantle_C_button.setText(_translate("SyringePanel", "dismantle"))
        self.dismantle_B_button.setText(_translate("SyringePanel", "dismantle"))
        self.label_level_2.setText(_translate("SyringePanel", "Automatic: 0–400 µL\n"
"\n"
"Manual: 0–500 µL"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SyringePanel = QtWidgets.QWidget()
    ui = Ui_SyringePanel()
    ui.setupUi(SyringePanel)
    SyringePanel.show()
    sys.exit(app.exec_())
