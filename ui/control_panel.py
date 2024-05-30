# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files/control_panel.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ControlPanel(object):
    def setupUi(self, ControlPanel):
        ControlPanel.setObjectName("ControlPanel")
        ControlPanel.resize(1262, 967)
        ControlPanel.setTabletTracking(False)
        ControlPanel.setIconSize(QtCore.QSize(18, 27))
        self.centralwidget = QtWidgets.QWidget(ControlPanel)
        self.centralwidget.setObjectName("centralwidget")
        self.direct_pH = QtWidgets.QLCDNumber(self.centralwidget)
        self.direct_pH.setGeometry(QtCore.QRect(630, 220, 101, 51))
        self.direct_pH.setObjectName("direct_pH")
        self.stabilisation_level = QtWidgets.QProgressBar(self.centralwidget)
        self.stabilisation_level.setGeometry(QtCore.QRect(630, 180, 101, 31))
        self.stabilisation_level.setMaximum(100)
        self.stabilisation_level.setProperty("value", 0)
        self.stabilisation_level.setTextVisible(True)
        self.stabilisation_level.setOrientation(QtCore.Qt.Horizontal)
        self.stabilisation_level.setObjectName("stabilisation_level")
        self.pH_label = QtWidgets.QLabel(self.centralwidget)
        self.pH_label.setGeometry(QtCore.QRect(590, 220, 41, 51))
        self.pH_label.setObjectName("pH_label")
        self.abs_label = QtWidgets.QLabel(self.centralwidget)
        self.abs_label.setGeometry(QtCore.QRect(10, 10, 271, 41))
        self.abs_label.setObjectName("abs_label")
        self.stability_label = QtWidgets.QLabel(self.centralwidget)
        self.stability_label.setGeometry(QtCore.QRect(630, 150, 101, 31))
        self.stability_label.setObjectName("stability_label")
        self.shutter = QtWidgets.QCheckBox(self.centralwidget)
        self.shutter.setGeometry(QtCore.QRect(20, 510, 111, 41))
        self.shutter.setObjectName("shutter")
        self.last_cal_label = QtWidgets.QLabel(self.centralwidget)
        self.last_cal_label.setGeometry(QtCore.QRect(750, 60, 191, 41))
        self.last_cal_label.setObjectName("last_cal_label")
        self.titration_button = QtWidgets.QPushButton(self.centralwidget)
        self.titration_button.setGeometry(QtCore.QRect(20, 720, 171, 41))
        self.titration_button.setObjectName("titration_button")
        self.cal_button = QtWidgets.QPushButton(self.centralwidget)
        self.cal_button.setGeometry(QtCore.QRect(630, 290, 101, 51))
        self.cal_button.setObjectName("cal_button")
        self.reglage_spectro = QtWidgets.QPushButton(self.centralwidget)
        self.reglage_spectro.setGeometry(QtCore.QRect(120, 510, 171, 41))
        self.reglage_spectro.setObjectName("reglage_spectro")
        self.saving_config = QtWidgets.QPushButton(self.centralwidget)
        self.saving_config.setGeometry(QtCore.QRect(20, 600, 171, 41))
        self.saving_config.setObjectName("saving_config")
        self.save_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_button.setGeometry(QtCore.QRect(20, 660, 171, 41))
        self.save_button.setObjectName("save_button")
        self.label_level = QtWidgets.QLabel(self.centralwidget)
        self.label_level.setGeometry(QtCore.QRect(590, 650, 161, 31))
        self.label_level.setAutoFillBackground(False)
        self.label_level.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_level.setObjectName("label_level")
        self.level_number_A = QtWidgets.QLabel(self.centralwidget)
        self.level_number_A.setGeometry(QtCore.QRect(750, 650, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.level_number_A.setFont(font)
        self.level_number_A.setAlignment(QtCore.Qt.AlignCenter)
        self.level_number_A.setObjectName("level_number_A")
        self.make_ref_A = QtWidgets.QPushButton(self.centralwidget)
        self.make_ref_A.setGeometry(QtCore.QRect(770, 690, 51, 31))
        self.make_ref_A.setObjectName("make_ref_A")
        self.connect_phmeter = QtWidgets.QPushButton(self.centralwidget)
        self.connect_phmeter.setGeometry(QtCore.QRect(580, 360, 151, 51))
        self.connect_phmeter.setObjectName("connect_phmeter")
        self.connect_pump = QtWidgets.QPushButton(self.centralwidget)
        self.connect_pump.setGeometry(QtCore.QRect(240, 670, 141, 31))
        self.connect_pump.setObjectName("connect_pump")
        self.stop_syringe = QtWidgets.QPushButton(self.centralwidget)
        self.stop_syringe.setGeometry(QtCore.QRect(560, 580, 81, 31))
        self.stop_syringe.setObjectName("stop_syringe")
        self.connect_syringe_pump = QtWidgets.QPushButton(self.centralwidget)
        self.connect_syringe_pump.setGeometry(QtCore.QRect(560, 450, 121, 51))
        self.connect_syringe_pump.setObjectName("connect_syringe_pump")
        self.graphic_tabs = QtWidgets.QTabWidget(self.centralwidget)
        self.graphic_tabs.setGeometry(QtCore.QRect(10, 50, 511, 441))
        self.graphic_tabs.setObjectName("graphic_tabs")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        self.Abs_direct = QtWidgets.QGraphicsView(self.tab1)
        self.Abs_direct.setGeometry(QtCore.QRect(0, 0, 511, 431))
        self.Abs_direct.setObjectName("Abs_direct")
        self.graphic_tabs.addTab(self.tab1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.Spectrum_direct = QtWidgets.QGraphicsView(self.tab_2)
        self.Spectrum_direct.setGeometry(QtCore.QRect(10, 50, 421, 281))
        self.Spectrum_direct.setObjectName("Spectrum_direct")
        self.graphic_tabs.addTab(self.tab_2, "")
        self.stab_time = QtWidgets.QSpinBox(self.centralwidget)
        self.stab_time.setGeometry(QtCore.QRect(680, 120, 51, 31))
        self.stab_time.setMaximum(600)
        self.stab_time.setProperty("value", 15)
        self.stab_time.setObjectName("stab_time")
        self.calib_text_box = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.calib_text_box.setGeometry(QtCore.QRect(750, 100, 331, 311))
        self.calib_text_box.setObjectName("calib_text_box")
        self.start_pump = QtWidgets.QPushButton(self.centralwidget)
        self.start_pump.setGeometry(QtCore.QRect(410, 620, 91, 31))
        self.start_pump.setObjectName("start_pump")
        self.label_pump = QtWidgets.QLabel(self.centralwidget)
        self.label_pump.setGeometry(QtCore.QRect(240, 620, 231, 31))
        self.label_pump.setObjectName("label_pump")
        self.stop_pump = QtWidgets.QPushButton(self.centralwidget)
        self.stop_pump.setGeometry(QtCore.QRect(410, 670, 91, 31))
        self.stop_pump.setObjectName("stop_pump")
        self.pump_speed_volt = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.pump_speed_volt.setGeometry(QtCore.QRect(430, 720, 71, 31))
        self.pump_speed_volt.setAccessibleName("")
        self.pump_speed_volt.setDecimals(1)
        self.pump_speed_volt.setMinimum(3.0)
        self.pump_speed_volt.setMaximum(12.0)
        self.pump_speed_volt.setSingleStep(0.1)
        self.pump_speed_volt.setProperty("value", 4.0)
        self.pump_speed_volt.setObjectName("pump_speed_volt")
        self.change_dir = QtWidgets.QPushButton(self.centralwidget)
        self.change_dir.setGeometry(QtCore.QRect(240, 720, 171, 31))
        self.change_dir.setObjectName("change_dir")
        self.stab_step = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.stab_step.setGeometry(QtCore.QRect(610, 120, 51, 31))
        self.stab_step.setMinimum(0.01)
        self.stab_step.setMaximum(0.3)
        self.stab_step.setSingleStep(0.01)
        self.stab_step.setObjectName("stab_step")
        self.phmeter_selection_box = QtWidgets.QComboBox(self.centralwidget)
        self.phmeter_selection_box.setGeometry(QtCore.QRect(560, 20, 171, 31))
        self.phmeter_selection_box.setEditable(True)
        self.phmeter_selection_box.setObjectName("phmeter_selection_box")
        self.phmeter_selection_box.addItem("")
        self.phmeter_selection_box.addItem("")
        self.phmeter_selection_box.addItem("")
        self.phmeter_selection_box.addItem("")
        self.phmeter_selection_box.addItem("")
        self.electrode_selection_box = QtWidgets.QComboBox(self.centralwidget)
        self.electrode_selection_box.setGeometry(QtCore.QRect(580, 70, 151, 31))
        self.electrode_selection_box.setObjectName("electrode_selection_box")
        self.electrode_selection_box.addItem("")
        self.electrode_selection_box.addItem("")
        self.electrode_selection_box.addItem("")
        self.electrode_selection_box.addItem("")
        self.electrode_selection_box.addItem("")
        self.load_calibration_button = QtWidgets.QPushButton(self.centralwidget)
        self.load_calibration_button.setGeometry(QtCore.QRect(750, 20, 331, 31))
        self.load_calibration_button.setObjectName("load_calibration_button")
        self.label_device = QtWidgets.QLabel(self.centralwidget)
        self.label_device.setGeometry(QtCore.QRect(320, 510, 221, 41))
        self.label_device.setObjectName("label_device")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(230, 600, 281, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(230, 750, 281, 21))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(220, 610, 21, 151))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(500, 610, 21, 151))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(530, 10, 21, 901))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(10, 550, 521, 21))
        self.line_6.setLineWidth(1)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(550, 420, 691, 21))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.label_syringeA = QtWidgets.QLabel(self.centralwidget)
        self.label_syringeA.setGeometry(QtCore.QRect(710, 440, 171, 51))
        self.label_syringeA.setAutoFillBackground(False)
        self.label_syringeA.setAlignment(QtCore.Qt.AlignCenter)
        self.label_syringeA.setObjectName("label_syringeA")
        self.levelbarA = QtWidgets.QProgressBar(self.centralwidget)
        self.levelbarA.setGeometry(QtCore.QRect(770, 500, 51, 141))
        self.levelbarA.setMinimum(0)
        self.levelbarA.setMaximum(500)
        self.levelbarA.setProperty("value", 100)
        self.levelbarA.setTextVisible(True)
        self.levelbarA.setOrientation(QtCore.Qt.Vertical)
        self.levelbarA.setInvertedAppearance(False)
        self.levelbarA.setObjectName("levelbarA")
        self.full_reload_A = QtWidgets.QPushButton(self.centralwidget)
        self.full_reload_A.setGeometry(QtCore.QRect(650, 690, 101, 31))
        self.full_reload_A.setObjectName("full_reload_A")
        self.load_button_A = QtWidgets.QPushButton(self.centralwidget)
        self.load_button_A.setGeometry(QtCore.QRect(650, 730, 101, 31))
        self.load_button_A.setObjectName("load_button_A")
        self.unload_button_A = QtWidgets.QPushButton(self.centralwidget)
        self.unload_button_A.setGeometry(QtCore.QRect(650, 770, 101, 31))
        self.unload_button_A.setObjectName("unload_button_A")
        self.dispense_button_A = QtWidgets.QPushButton(self.centralwidget)
        self.dispense_button_A.setGeometry(QtCore.QRect(650, 810, 101, 31))
        self.dispense_button_A.setObjectName("dispense_button_A")
        self.load_box_A = QtWidgets.QSpinBox(self.centralwidget)
        self.load_box_A.setGeometry(QtCore.QRect(760, 730, 71, 31))
        self.load_box_A.setMaximum(500)
        self.load_box_A.setObjectName("load_box_A")
        self.unload_box_A = QtWidgets.QSpinBox(self.centralwidget)
        self.unload_box_A.setGeometry(QtCore.QRect(760, 770, 71, 31))
        self.unload_box_A.setMaximum(400)
        self.unload_box_A.setObjectName("unload_box_A")
        self.dispense_box_A = QtWidgets.QSpinBox(self.centralwidget)
        self.dispense_box_A.setGeometry(QtCore.QRect(760, 810, 71, 31))
        self.dispense_box_A.setMaximum(400)
        self.dispense_box_A.setObjectName("dispense_box_A")
        self.label_added_volume = QtWidgets.QLabel(self.centralwidget)
        self.label_added_volume.setGeometry(QtCore.QRect(550, 850, 191, 31))
        self.label_added_volume.setAutoFillBackground(False)
        self.label_added_volume.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_added_volume.setObjectName("label_added_volume")
        self.added_A_uL = QtWidgets.QLabel(self.centralwidget)
        self.added_A_uL.setGeometry(QtCore.QRect(750, 850, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.added_A_uL.setFont(font)
        self.added_A_uL.setAlignment(QtCore.Qt.AlignCenter)
        self.added_A_uL.setObjectName("added_A_uL")
        self.level_number_B = QtWidgets.QLabel(self.centralwidget)
        self.level_number_B.setGeometry(QtCore.QRect(950, 650, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.level_number_B.setFont(font)
        self.level_number_B.setAlignment(QtCore.Qt.AlignCenter)
        self.level_number_B.setObjectName("level_number_B")
        self.label_syringeB = QtWidgets.QLabel(self.centralwidget)
        self.label_syringeB.setGeometry(QtCore.QRect(920, 440, 151, 51))
        self.label_syringeB.setAutoFillBackground(False)
        self.label_syringeB.setAlignment(QtCore.Qt.AlignCenter)
        self.label_syringeB.setObjectName("label_syringeB")
        self.levelbarB = QtWidgets.QProgressBar(self.centralwidget)
        self.levelbarB.setGeometry(QtCore.QRect(970, 500, 51, 141))
        self.levelbarB.setMinimum(0)
        self.levelbarB.setMaximum(500)
        self.levelbarB.setProperty("value", 400)
        self.levelbarB.setTextVisible(True)
        self.levelbarB.setOrientation(QtCore.Qt.Vertical)
        self.levelbarB.setInvertedAppearance(False)
        self.levelbarB.setObjectName("levelbarB")
        self.level_number_C = QtWidgets.QLabel(self.centralwidget)
        self.level_number_C.setGeometry(QtCore.QRect(1150, 650, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.level_number_C.setFont(font)
        self.level_number_C.setAlignment(QtCore.Qt.AlignCenter)
        self.level_number_C.setObjectName("level_number_C")
        self.label_syringeC = QtWidgets.QLabel(self.centralwidget)
        self.label_syringeC.setGeometry(QtCore.QRect(1070, 440, 151, 51))
        self.label_syringeC.setAutoFillBackground(False)
        self.label_syringeC.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_syringeC.setObjectName("label_syringeC")
        self.levelbarC = QtWidgets.QProgressBar(self.centralwidget)
        self.levelbarC.setGeometry(QtCore.QRect(1170, 500, 51, 141))
        self.levelbarC.setMinimum(0)
        self.levelbarC.setMaximum(500)
        self.levelbarC.setProperty("value", 50)
        self.levelbarC.setTextVisible(True)
        self.levelbarC.setOrientation(QtCore.Qt.Vertical)
        self.levelbarC.setInvertedAppearance(False)
        self.levelbarC.setObjectName("levelbarC")
        self.added_B_uL = QtWidgets.QLabel(self.centralwidget)
        self.added_B_uL.setGeometry(QtCore.QRect(950, 850, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.added_B_uL.setFont(font)
        self.added_B_uL.setAlignment(QtCore.Qt.AlignCenter)
        self.added_B_uL.setObjectName("added_B_uL")
        self.added_C_uL = QtWidgets.QLabel(self.centralwidget)
        self.added_C_uL.setGeometry(QtCore.QRect(1150, 850, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.added_C_uL.setFont(font)
        self.added_C_uL.setAlignment(QtCore.Qt.AlignCenter)
        self.added_C_uL.setObjectName("added_C_uL")
        self.label_total_volume = QtWidgets.QLabel(self.centralwidget)
        self.label_total_volume.setGeometry(QtCore.QRect(550, 880, 191, 31))
        self.label_total_volume.setAutoFillBackground(False)
        self.label_total_volume.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_total_volume.setObjectName("label_total_volume")
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setGeometry(QtCore.QRect(580, 840, 661, 21))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.line_9 = QtWidgets.QFrame(self.centralwidget)
        self.line_9.setGeometry(QtCore.QRect(580, 870, 661, 21))
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.line_10 = QtWidgets.QFrame(self.centralwidget)
        self.line_10.setGeometry(QtCore.QRect(580, 900, 661, 21))
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.added_total = QtWidgets.QLabel(self.centralwidget)
        self.added_total.setGeometry(QtCore.QRect(750, 880, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.added_total.setFont(font)
        self.added_total.setAlignment(QtCore.Qt.AlignCenter)
        self.added_total.setObjectName("added_total")
        self.open_syringe_panel = QtWidgets.QPushButton(self.centralwidget)
        self.open_syringe_panel.setGeometry(QtCore.QRect(560, 520, 161, 41))
        self.open_syringe_panel.setObjectName("open_syringe_panel")
        self.line_12 = QtWidgets.QFrame(self.centralwidget)
        self.line_12.setGeometry(QtCore.QRect(580, 640, 661, 21))
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.close_all = QtWidgets.QPushButton(self.centralwidget)
        self.close_all.setGeometry(QtCore.QRect(20, 860, 171, 41))
        self.close_all.setObjectName("close_all")
        self.connect_all_devices = QtWidgets.QPushButton(self.centralwidget)
        self.connect_all_devices.setGeometry(QtCore.QRect(20, 810, 171, 41))
        self.connect_all_devices.setObjectName("connect_all_devices")
        self.unload_button_B = QtWidgets.QPushButton(self.centralwidget)
        self.unload_button_B.setGeometry(QtCore.QRect(850, 770, 101, 31))
        self.unload_button_B.setObjectName("unload_button_B")
        self.full_reload_B = QtWidgets.QPushButton(self.centralwidget)
        self.full_reload_B.setGeometry(QtCore.QRect(850, 690, 101, 31))
        self.full_reload_B.setObjectName("full_reload_B")
        self.dispense_box_B = QtWidgets.QSpinBox(self.centralwidget)
        self.dispense_box_B.setGeometry(QtCore.QRect(960, 810, 71, 31))
        self.dispense_box_B.setMaximum(400)
        self.dispense_box_B.setObjectName("dispense_box_B")
        self.dispense_button_B = QtWidgets.QPushButton(self.centralwidget)
        self.dispense_button_B.setGeometry(QtCore.QRect(850, 810, 101, 31))
        self.dispense_button_B.setObjectName("dispense_button_B")
        self.unload_box_B = QtWidgets.QSpinBox(self.centralwidget)
        self.unload_box_B.setGeometry(QtCore.QRect(960, 770, 71, 31))
        self.unload_box_B.setMaximum(400)
        self.unload_box_B.setObjectName("unload_box_B")
        self.load_box_B = QtWidgets.QSpinBox(self.centralwidget)
        self.load_box_B.setGeometry(QtCore.QRect(960, 730, 71, 31))
        self.load_box_B.setMaximum(500)
        self.load_box_B.setObjectName("load_box_B")
        self.load_button_B = QtWidgets.QPushButton(self.centralwidget)
        self.load_button_B.setGeometry(QtCore.QRect(850, 730, 101, 31))
        self.load_button_B.setObjectName("load_button_B")
        self.make_ref_B = QtWidgets.QPushButton(self.centralwidget)
        self.make_ref_B.setGeometry(QtCore.QRect(970, 690, 51, 31))
        self.make_ref_B.setObjectName("make_ref_B")
        self.unload_button_C = QtWidgets.QPushButton(self.centralwidget)
        self.unload_button_C.setGeometry(QtCore.QRect(1050, 770, 101, 31))
        self.unload_button_C.setObjectName("unload_button_C")
        self.full_reload_C = QtWidgets.QPushButton(self.centralwidget)
        self.full_reload_C.setGeometry(QtCore.QRect(1050, 690, 101, 31))
        self.full_reload_C.setObjectName("full_reload_C")
        self.dispense_box_C = QtWidgets.QSpinBox(self.centralwidget)
        self.dispense_box_C.setGeometry(QtCore.QRect(1160, 810, 71, 31))
        self.dispense_box_C.setMaximum(400)
        self.dispense_box_C.setObjectName("dispense_box_C")
        self.dispense_button_C = QtWidgets.QPushButton(self.centralwidget)
        self.dispense_button_C.setGeometry(QtCore.QRect(1050, 810, 101, 31))
        self.dispense_button_C.setObjectName("dispense_button_C")
        self.unload_box_C = QtWidgets.QSpinBox(self.centralwidget)
        self.unload_box_C.setGeometry(QtCore.QRect(1160, 770, 71, 31))
        self.unload_box_C.setMaximum(400)
        self.unload_box_C.setObjectName("unload_box_C")
        self.load_box_C = QtWidgets.QSpinBox(self.centralwidget)
        self.load_box_C.setGeometry(QtCore.QRect(1160, 730, 71, 31))
        self.load_box_C.setMaximum(500)
        self.load_box_C.setObjectName("load_box_C")
        self.load_button_C = QtWidgets.QPushButton(self.centralwidget)
        self.load_button_C.setGeometry(QtCore.QRect(1050, 730, 101, 31))
        self.load_button_C.setObjectName("load_button_C")
        self.make_ref_C = QtWidgets.QPushButton(self.centralwidget)
        self.make_ref_C.setGeometry(QtCore.QRect(1170, 690, 51, 31))
        self.make_ref_C.setObjectName("make_ref_C")
        ControlPanel.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ControlPanel)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1262, 18))
        self.menubar.setObjectName("menubar")
        self.menuPanneau_de_controle = QtWidgets.QMenu(self.menubar)
        self.menuPanneau_de_controle.setObjectName("menuPanneau_de_controle")
        self.menuedit = QtWidgets.QMenu(self.menubar)
        self.menuedit.setObjectName("menuedit")
        self.menuhelp = QtWidgets.QMenu(self.menubar)
        self.menuhelp.setObjectName("menuhelp")
        self.menuparameters = QtWidgets.QMenu(self.menubar)
        self.menuparameters.setObjectName("menuparameters")
        ControlPanel.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ControlPanel)
        self.statusbar.setObjectName("statusbar")
        ControlPanel.setStatusBar(self.statusbar)
        self.actionget_help = QtWidgets.QAction(ControlPanel)
        self.actionget_help.setObjectName("actionget_help")
        self.actionsave = QtWidgets.QAction(ControlPanel)
        self.actionsave.setObjectName("actionsave")
        self.actionchange_folder = QtWidgets.QAction(ControlPanel)
        self.actionchange_folder.setObjectName("actionchange_folder")
        self.actionSyringes_parameters = QtWidgets.QAction(ControlPanel)
        self.actionSyringes_parameters.setObjectName("actionSyringes_parameters")
        self.menuPanneau_de_controle.addSeparator()
        self.menuPanneau_de_controle.addSeparator()
        self.menuPanneau_de_controle.addAction(self.actionsave)
        self.menuPanneau_de_controle.addAction(self.actionchange_folder)
        self.menuhelp.addSeparator()
        self.menuhelp.addAction(self.actionget_help)
        self.menuparameters.addAction(self.actionSyringes_parameters)
        self.menubar.addAction(self.menuPanneau_de_controle.menuAction())
        self.menubar.addAction(self.menuedit.menuAction())
        self.menubar.addAction(self.menuhelp.menuAction())
        self.menubar.addAction(self.menuparameters.menuAction())

        self.retranslateUi(ControlPanel)
        self.graphic_tabs.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(ControlPanel)

    def retranslateUi(self, ControlPanel):
        _translate = QtCore.QCoreApplication.translate
        ControlPanel.setWindowTitle(_translate("ControlPanel", "Control Panel"))
        self.stabilisation_level.setFormat(_translate("ControlPanel", "%p%"))
        self.pH_label.setText(_translate("ControlPanel", "pH"))
        self.abs_label.setText(_translate("ControlPanel", "Direct and reference spectra"))
        self.stability_label.setText(_translate("ControlPanel", "stability"))
        self.shutter.setText(_translate("ControlPanel", "shutter"))
        self.last_cal_label.setText(_translate("ControlPanel", "last calibration"))
        self.titration_button.setText(_translate("ControlPanel", "Configure Sequence"))
        self.cal_button.setText(_translate("ControlPanel", "calibration"))
        self.reglage_spectro.setText(_translate("ControlPanel", "Spectrometry settings"))
        self.saving_config.setText(_translate("ControlPanel", "Configure data saving"))
        self.save_button.setText(_translate("ControlPanel", "Save current measure"))
        self.label_level.setText(_translate("ControlPanel", "level (0 - 400uL)"))
        self.level_number_A.setText(_translate("ControlPanel", "0 uL"))
        self.make_ref_A.setText(_translate("ControlPanel", "ref"))
        self.connect_phmeter.setText(_translate("ControlPanel", "connect pH meter"))
        self.connect_pump.setText(_translate("ControlPanel", "connect pump"))
        self.stop_syringe.setText(_translate("ControlPanel", "Stop"))
        self.connect_syringe_pump.setText(_translate("ControlPanel", "connect \n"
" Syringe Pump"))
        self.graphic_tabs.setTabText(self.graphic_tabs.indexOf(self.tab1), _translate("ControlPanel", "Tab 1"))
        self.graphic_tabs.setTabText(self.graphic_tabs.indexOf(self.tab_2), _translate("ControlPanel", "Tab 2"))
        self.start_pump.setText(_translate("ControlPanel", "Start"))
        self.label_pump.setText(_translate("ControlPanel", "Peristaltic Pump"))
        self.stop_pump.setText(_translate("ControlPanel", "Stop"))
        self.change_dir.setText(_translate("ControlPanel", "change Direction"))
        self.phmeter_selection_box.setCurrentText(_translate("ControlPanel", "Phidget ADP1000"))
        self.phmeter_selection_box.setItemText(0, _translate("ControlPanel", "Phidget ADP1000"))
        self.phmeter_selection_box.setItemText(1, _translate("ControlPanel", "Phidget 1130"))
        self.phmeter_selection_box.setItemText(2, _translate("ControlPanel", "HI5221"))
        self.phmeter_selection_box.setItemText(3, _translate("ControlPanel", "Metrohm titrando"))
        self.phmeter_selection_box.setItemText(4, _translate("ControlPanel", "other"))
        self.electrode_selection_box.setItemText(0, _translate("ControlPanel", "Oakton epoxy"))
        self.electrode_selection_box.setItemText(1, _translate("ControlPanel", "VWR 662-1793"))
        self.electrode_selection_box.setItemText(2, _translate("ControlPanel", "metrohm 6.0232.100"))
        self.electrode_selection_box.setItemText(3, _translate("ControlPanel", "metrohm 6.0259.100"))
        self.electrode_selection_box.setItemText(4, _translate("ControlPanel", "other"))
        self.load_calibration_button.setText(_translate("ControlPanel", "Select an existing calibration"))
        self.label_device.setText(_translate("ControlPanel", "device model :"))
        self.label_syringeA.setText(_translate("ControlPanel", "Syringe A \n"
" HCl 0.1M (acid)"))
        self.levelbarA.setFormat(_translate("ControlPanel", "%p%"))
        self.full_reload_A.setText(_translate("ControlPanel", "Full reload"))
        self.load_button_A.setText(_translate("ControlPanel", "load"))
        self.unload_button_A.setText(_translate("ControlPanel", "unload"))
        self.dispense_button_A.setText(_translate("ControlPanel", "Dispense"))
        self.label_added_volume.setText(_translate("ControlPanel", "added volume (uL)"))
        self.added_A_uL.setText(_translate("ControlPanel", "0 uL"))
        self.level_number_B.setText(_translate("ControlPanel", "0 uL"))
        self.label_syringeB.setText(_translate("ControlPanel", "Syringe B \n"
" NaOH 0.1M (base)"))
        self.levelbarB.setFormat(_translate("ControlPanel", "%p%"))
        self.level_number_C.setText(_translate("ControlPanel", "0 uL"))
        self.label_syringeC.setText(_translate("ControlPanel", "Syringe C \n"
" Reagent 3"))
        self.levelbarC.setFormat(_translate("ControlPanel", "%p%"))
        self.added_B_uL.setText(_translate("ControlPanel", "0 uL"))
        self.added_C_uL.setText(_translate("ControlPanel", "0 uL"))
        self.label_total_volume.setText(_translate("ControlPanel", "total (uL)"))
        self.added_total.setText(_translate("ControlPanel", "0 uL"))
        self.open_syringe_panel.setText(_translate("ControlPanel", "open Syringe Panel"))
        self.close_all.setText(_translate("ControlPanel", "close all devices"))
        self.connect_all_devices.setText(_translate("ControlPanel", "connect all devices"))
        self.unload_button_B.setText(_translate("ControlPanel", "unload"))
        self.full_reload_B.setText(_translate("ControlPanel", "Full reload"))
        self.dispense_button_B.setText(_translate("ControlPanel", "Dispense"))
        self.load_button_B.setText(_translate("ControlPanel", "load"))
        self.make_ref_B.setText(_translate("ControlPanel", "ref"))
        self.unload_button_C.setText(_translate("ControlPanel", "unload"))
        self.full_reload_C.setText(_translate("ControlPanel", "Full reload"))
        self.dispense_button_C.setText(_translate("ControlPanel", "Dispense"))
        self.load_button_C.setText(_translate("ControlPanel", "load"))
        self.make_ref_C.setText(_translate("ControlPanel", "ref"))
        self.menuPanneau_de_controle.setTitle(_translate("ControlPanel", "file"))
        self.menuedit.setTitle(_translate("ControlPanel", "edit"))
        self.menuhelp.setTitle(_translate("ControlPanel", "help"))
        self.menuparameters.setTitle(_translate("ControlPanel", "parameters"))
        self.actionget_help.setText(_translate("ControlPanel", "get help"))
        self.actionsave.setText(_translate("ControlPanel", "save"))
        self.actionchange_folder.setText(_translate("ControlPanel", "change folder"))
        self.actionSyringes_parameters.setText(_translate("ControlPanel", "Syringes parameters"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ControlPanel = QtWidgets.QMainWindow()
    ui = Ui_ControlPanel()
    ui.setupUi(ControlPanel)
    ControlPanel.show()
    sys.exit(app.exec_())
