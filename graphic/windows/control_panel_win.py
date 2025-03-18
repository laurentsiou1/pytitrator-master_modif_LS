# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'graphic/ui_files/control_panel.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
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
        self.direct_pH.setGeometry(QtCore.QRect(710, 200, 101, 51))
        self.direct_pH.setObjectName("direct_pH")
        self.stabilisation_level = QtWidgets.QProgressBar(self.centralwidget)
        self.stabilisation_level.setGeometry(QtCore.QRect(710, 140, 101, 31))
        self.stabilisation_level.setMaximum(100)
        self.stabilisation_level.setProperty("value", 0)
        self.stabilisation_level.setTextVisible(True)
        self.stabilisation_level.setOrientation(QtCore.Qt.Horizontal)
        self.stabilisation_level.setObjectName("stabilisation_level")
        self.pH_label = QtWidgets.QLabel(self.centralwidget)
        self.pH_label.setGeometry(QtCore.QRect(670, 200, 41, 51))
        self.pH_label.setObjectName("pH_label")
        self.abs_label = QtWidgets.QLabel(self.centralwidget)
        self.abs_label.setGeometry(QtCore.QRect(10, 10, 351, 41))
        self.abs_label.setObjectName("abs_label")
        self.stability_label = QtWidgets.QLabel(self.centralwidget)
        self.stability_label.setGeometry(QtCore.QRect(710, 110, 101, 31))
        self.stability_label.setObjectName("stability_label")
        self.shutter = QtWidgets.QCheckBox(self.centralwidget)
        self.shutter.setGeometry(QtCore.QRect(20, 510, 111, 41))
        self.shutter.setObjectName("shutter")
        self.last_cal_label = QtWidgets.QLabel(self.centralwidget)
        self.last_cal_label.setGeometry(QtCore.QRect(840, 60, 191, 41))
        self.last_cal_label.setObjectName("last_cal_label")
        self.configure_sequence = QtWidgets.QPushButton(self.centralwidget)
        self.configure_sequence.setGeometry(QtCore.QRect(30, 650, 171, 41))
        self.configure_sequence.setObjectName("configure_sequence")
        self.cal_button = QtWidgets.QPushButton(self.centralwidget)
        self.cal_button.setGeometry(QtCore.QRect(710, 270, 101, 41))
        self.cal_button.setObjectName("cal_button")
        self.spectro_settings = QtWidgets.QPushButton(self.centralwidget)
        self.spectro_settings.setGeometry(QtCore.QRect(120, 510, 171, 41))
        self.spectro_settings.setObjectName("spectro_settings")
        self.save_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_button.setGeometry(QtCore.QRect(30, 590, 171, 41))
        self.save_button.setObjectName("save_button")
        self.label_level = QtWidgets.QLabel(self.centralwidget)
        self.label_level.setGeometry(QtCore.QRect(660, 790, 161, 31))
        self.label_level.setAutoFillBackground(False)
        self.label_level.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_level.setObjectName("label_level")
        self.levelA_uL = QtWidgets.QLabel(self.centralwidget)
        self.levelA_uL.setGeometry(QtCore.QRect(850, 790, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.levelA_uL.setFont(font)
        self.levelA_uL.setAlignment(QtCore.Qt.AlignCenter)
        self.levelA_uL.setObjectName("levelA_uL")
        self.connect_phmeter = QtWidgets.QPushButton(self.centralwidget)
        self.connect_phmeter.setGeometry(QtCore.QRect(570, 140, 101, 31))
        self.connect_phmeter.setObjectName("connect_phmeter")
        self.connect_disconnect_circuit = QtWidgets.QPushButton(self.centralwidget)
        self.connect_disconnect_circuit.setGeometry(QtCore.QRect(400, 590, 101, 31))
        self.connect_disconnect_circuit.setObjectName("connect_disconnect_circuit")
        self.stop_syringe = QtWidgets.QPushButton(self.centralwidget)
        self.stop_syringe.setGeometry(QtCore.QRect(580, 750, 61, 61))
        self.stop_syringe.setObjectName("stop_syringe")
        self.connect_syringe_pump = QtWidgets.QPushButton(self.centralwidget)
        self.connect_syringe_pump.setGeometry(QtCore.QRect(650, 510, 111, 61))
        self.connect_syringe_pump.setObjectName("connect_syringe_pump")
        self.graphic_tabs = QtWidgets.QTabWidget(self.centralwidget)
        self.graphic_tabs.setGeometry(QtCore.QRect(10, 50, 511, 441))
        self.graphic_tabs.setObjectName("graphic_tabs")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        self.graphic_tabs.addTab(self.tab1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.graphic_tabs.addTab(self.tab_2, "")
        self.stab_time = QtWidgets.QSpinBox(self.centralwidget)
        self.stab_time.setGeometry(QtCore.QRect(760, 80, 51, 31))
        self.stab_time.setMaximum(600)
        self.stab_time.setProperty("value", 15)
        self.stab_time.setObjectName("stab_time")
        self.calib_text_box = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.calib_text_box.setGeometry(QtCore.QRect(840, 100, 331, 211))
        self.calib_text_box.setObjectName("calib_text_box")
        self.start_stop_pump_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_stop_pump_button.setGeometry(QtCore.QRect(390, 640, 71, 31))
        self.start_stop_pump_button.setObjectName("start_stop_pump_button")
        self.label_circuit = QtWidgets.QLabel(self.centralwidget)
        self.label_circuit.setGeometry(QtCore.QRect(250, 590, 151, 31))
        self.label_circuit.setAlignment(QtCore.Qt.AlignCenter)
        self.label_circuit.setObjectName("label_circuit")
        self.change_dir = QtWidgets.QPushButton(self.centralwidget)
        self.change_dir.setGeometry(QtCore.QRect(260, 680, 181, 31))
        self.change_dir.setObjectName("change_dir")
        self.stab_step = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.stab_step.setGeometry(QtCore.QRect(690, 80, 51, 31))
        self.stab_step.setMinimum(0.01)
        self.stab_step.setMaximum(0.3)
        self.stab_step.setSingleStep(0.01)
        self.stab_step.setObjectName("stab_step")
        self.label_model = QtWidgets.QLabel(self.centralwidget)
        self.label_model.setGeometry(QtCore.QRect(310, 500, 171, 31))
        self.label_model.setObjectName("label_model")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(220, 570, 301, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(220, 890, 301, 21))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(210, 580, 21, 321))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(510, 580, 21, 321))
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
        self.line_7.setGeometry(QtCore.QRect(550, 480, 691, 21))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.label_added_volume = QtWidgets.QLabel(self.centralwidget)
        self.label_added_volume.setGeometry(QtCore.QRect(630, 850, 191, 31))
        self.label_added_volume.setAutoFillBackground(False)
        self.label_added_volume.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_added_volume.setObjectName("label_added_volume")
        self.added_A_uL = QtWidgets.QLabel(self.centralwidget)
        self.added_A_uL.setGeometry(QtCore.QRect(850, 850, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.added_A_uL.setFont(font)
        self.added_A_uL.setAlignment(QtCore.Qt.AlignCenter)
        self.added_A_uL.setObjectName("added_A_uL")
        self.levelB_uL = QtWidgets.QLabel(self.centralwidget)
        self.levelB_uL.setGeometry(QtCore.QRect(980, 790, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.levelB_uL.setFont(font)
        self.levelB_uL.setAlignment(QtCore.Qt.AlignCenter)
        self.levelB_uL.setObjectName("levelB_uL")
        self.levelbarB = QtWidgets.QProgressBar(self.centralwidget)
        self.levelbarB.setGeometry(QtCore.QRect(1000, 650, 51, 141))
        self.levelbarB.setMinimum(0)
        self.levelbarB.setMaximum(400)
        self.levelbarB.setProperty("value", 400)
        self.levelbarB.setTextVisible(True)
        self.levelbarB.setOrientation(QtCore.Qt.Vertical)
        self.levelbarB.setInvertedAppearance(False)
        self.levelbarB.setObjectName("levelbarB")
        self.levelC_uL = QtWidgets.QLabel(self.centralwidget)
        self.levelC_uL.setGeometry(QtCore.QRect(1110, 790, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.levelC_uL.setFont(font)
        self.levelC_uL.setAlignment(QtCore.Qt.AlignCenter)
        self.levelC_uL.setObjectName("levelC_uL")
        self.added_B_uL = QtWidgets.QLabel(self.centralwidget)
        self.added_B_uL.setGeometry(QtCore.QRect(980, 850, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.added_B_uL.setFont(font)
        self.added_B_uL.setAlignment(QtCore.Qt.AlignCenter)
        self.added_B_uL.setObjectName("added_B_uL")
        self.added_C_uL = QtWidgets.QLabel(self.centralwidget)
        self.added_C_uL.setGeometry(QtCore.QRect(1110, 850, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.added_C_uL.setFont(font)
        self.added_C_uL.setAlignment(QtCore.Qt.AlignCenter)
        self.added_C_uL.setObjectName("added_C_uL")
        self.label_total_volume = QtWidgets.QLabel(self.centralwidget)
        self.label_total_volume.setGeometry(QtCore.QRect(580, 880, 131, 31))
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
        self.added_total.setGeometry(QtCore.QRect(740, 880, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.added_total.setFont(font)
        self.added_total.setAlignment(QtCore.Qt.AlignCenter)
        self.added_total.setObjectName("added_total")
        self.open_syringe_panel = QtWidgets.QPushButton(self.centralwidget)
        self.open_syringe_panel.setGeometry(QtCore.QRect(560, 660, 161, 51))
        self.open_syringe_panel.setObjectName("open_syringe_panel")
        self.close_all = QtWidgets.QPushButton(self.centralwidget)
        self.close_all.setGeometry(QtCore.QRect(30, 850, 171, 41))
        self.close_all.setObjectName("close_all")
        self.connect_all_devices = QtWidgets.QPushButton(self.centralwidget)
        self.connect_all_devices.setGeometry(QtCore.QRect(30, 790, 171, 41))
        self.connect_all_devices.setObjectName("connect_all_devices")
        self.led_spectro = QtWidgets.QLabel(self.centralwidget)
        self.led_spectro.setGeometry(QtCore.QRect(470, 510, 31, 31))
        self.led_spectro.setObjectName("led_spectro")
        self.led_phmeter = QtWidgets.QLabel(self.centralwidget)
        self.led_phmeter.setGeometry(QtCore.QRect(600, 180, 31, 31))
        self.led_phmeter.setObjectName("led_phmeter")
        self.led_disp = QtWidgets.QLabel(self.centralwidget)
        self.led_disp.setGeometry(QtCore.QRect(580, 520, 31, 31))
        self.led_disp.setObjectName("led_disp")
        self.led_pump = QtWidgets.QLabel(self.centralwidget)
        self.led_pump.setGeometry(QtCore.QRect(230, 640, 31, 31))
        self.led_pump.setObjectName("led_pump")
        self.syringeA = QtWidgets.QLabel(self.centralwidget)
        self.syringeA.setGeometry(QtCore.QRect(840, 500, 111, 41))
        self.syringeA.setAlignment(QtCore.Qt.AlignCenter)
        self.syringeA.setObjectName("syringeA")
        self.reagentA = QtWidgets.QLabel(self.centralwidget)
        self.reagentA.setGeometry(QtCore.QRect(840, 550, 111, 41))
        self.reagentA.setAlignment(QtCore.Qt.AlignCenter)
        self.reagentA.setObjectName("reagentA")
        self.Ca = QtWidgets.QLabel(self.centralwidget)
        self.Ca.setGeometry(QtCore.QRect(840, 600, 111, 41))
        self.Ca.setAlignment(QtCore.Qt.AlignCenter)
        self.Ca.setObjectName("Ca")
        self.syringeB = QtWidgets.QLabel(self.centralwidget)
        self.syringeB.setGeometry(QtCore.QRect(980, 500, 91, 41))
        self.syringeB.setAlignment(QtCore.Qt.AlignCenter)
        self.syringeB.setObjectName("syringeB")
        self.Cc = QtWidgets.QLabel(self.centralwidget)
        self.Cc.setGeometry(QtCore.QRect(1110, 600, 91, 41))
        self.Cc.setAlignment(QtCore.Qt.AlignCenter)
        self.Cc.setObjectName("Cc")
        self.Cb = QtWidgets.QLabel(self.centralwidget)
        self.Cb.setGeometry(QtCore.QRect(980, 600, 91, 41))
        self.Cb.setAlignment(QtCore.Qt.AlignCenter)
        self.Cb.setObjectName("Cb")
        self.reagentC = QtWidgets.QLabel(self.centralwidget)
        self.reagentC.setGeometry(QtCore.QRect(1090, 550, 131, 41))
        self.reagentC.setAlignment(QtCore.Qt.AlignCenter)
        self.reagentC.setObjectName("reagentC")
        self.syringeC = QtWidgets.QLabel(self.centralwidget)
        self.syringeC.setGeometry(QtCore.QRect(1110, 500, 91, 41))
        self.syringeC.setAlignment(QtCore.Qt.AlignCenter)
        self.syringeC.setObjectName("syringeC")
        self.reagentB = QtWidgets.QLabel(self.centralwidget)
        self.reagentB.setGeometry(QtCore.QRect(980, 550, 91, 41))
        self.reagentB.setAlignment(QtCore.Qt.AlignCenter)
        self.reagentB.setObjectName("reagentB")
        self.label_concentration = QtWidgets.QLabel(self.centralwidget)
        self.label_concentration.setGeometry(QtCore.QRect(660, 600, 181, 41))
        self.label_concentration.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_concentration.setObjectName("label_concentration")
        self.label_reagent = QtWidgets.QLabel(self.centralwidget)
        self.label_reagent.setGeometry(QtCore.QRect(730, 550, 111, 41))
        self.label_reagent.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_reagent.setObjectName("label_reagent")
        self.levelbarA = QtWidgets.QProgressBar(self.centralwidget)
        self.levelbarA.setGeometry(QtCore.QRect(870, 650, 51, 141))
        self.levelbarA.setMinimum(0)
        self.levelbarA.setMaximum(400)
        self.levelbarA.setProperty("value", 400)
        self.levelbarA.setTextVisible(True)
        self.levelbarA.setOrientation(QtCore.Qt.Vertical)
        self.levelbarA.setInvertedAppearance(False)
        self.levelbarA.setObjectName("levelbarA")
        self.levelbarC = QtWidgets.QProgressBar(self.centralwidget)
        self.levelbarC.setGeometry(QtCore.QRect(1130, 650, 51, 141))
        self.levelbarC.setMinimum(0)
        self.levelbarC.setMaximum(400)
        self.levelbarC.setProperty("value", 400)
        self.levelbarC.setTextVisible(True)
        self.levelbarC.setOrientation(QtCore.Qt.Vertical)
        self.levelbarC.setInvertedAppearance(False)
        self.levelbarC.setObjectName("levelbarC")
        self.label_instrument_SN = QtWidgets.QLabel(self.centralwidget)
        self.label_instrument_SN.setGeometry(QtCore.QRect(220, 900, 261, 31))
        self.label_instrument_SN.setObjectName("label_instrument_SN")
        self.label_spectro_SN = QtWidgets.QLabel(self.centralwidget)
        self.label_spectro_SN.setGeometry(QtCore.QRect(310, 530, 171, 31))
        self.label_spectro_SN.setObjectName("label_spectro_SN")
        self.ev0_state = QtWidgets.QPushButton(self.centralwidget)
        self.ev0_state.setGeometry(QtCore.QRect(330, 750, 71, 31))
        self.ev0_state.setObjectName("ev0_state")
        self.ev1_state = QtWidgets.QPushButton(self.centralwidget)
        self.ev1_state.setGeometry(QtCore.QRect(420, 750, 71, 31))
        self.ev1_state.setObjectName("ev1_state")
        self.label_ev0 = QtWidgets.QLabel(self.centralwidget)
        self.label_ev0.setGeometry(QtCore.QRect(310, 720, 111, 31))
        self.label_ev0.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ev0.setObjectName("label_ev0")
        self.label_ev1 = QtWidgets.QLabel(self.centralwidget)
        self.label_ev1.setGeometry(QtCore.QRect(400, 720, 111, 31))
        self.label_ev1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ev1.setObjectName("label_ev1")
        self.fill_water = QtWidgets.QPushButton(self.centralwidget)
        self.fill_water.setGeometry(QtCore.QRect(240, 840, 121, 31))
        self.fill_water.setObjectName("fill_water")
        self.clean_empty = QtWidgets.QPushButton(self.centralwidget)
        self.clean_empty.setGeometry(QtCore.QRect(380, 840, 121, 51))
        self.clean_empty.setObjectName("clean_empty")
        self.led_ev_circuit = QtWidgets.QLabel(self.centralwidget)
        self.led_ev_circuit.setGeometry(QtCore.QRect(230, 730, 31, 31))
        self.led_ev_circuit.setObjectName("led_ev_circuit")
        self.pump_speed = QtWidgets.QSlider(self.centralwidget)
        self.pump_speed.setGeometry(QtCore.QRect(470, 640, 31, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.pump_speed.sizePolicy().hasHeightForWidth())
        self.pump_speed.setSizePolicy(sizePolicy)
        self.pump_speed.setMouseTracking(False)
        self.pump_speed.setMinimum(1)
        self.pump_speed.setMaximum(5)
        self.pump_speed.setOrientation(QtCore.Qt.Vertical)
        self.pump_speed.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.pump_speed.setTickInterval(1)
        self.pump_speed.setObjectName("pump_speed")
        self.label_pump = QtWidgets.QLabel(self.centralwidget)
        self.label_pump.setGeometry(QtCore.QRect(270, 640, 111, 31))
        self.label_pump.setAlignment(QtCore.Qt.AlignCenter)
        self.label_pump.setObjectName("label_pump")
        self.line_11 = QtWidgets.QFrame(self.centralwidget)
        self.line_11.setGeometry(QtCore.QRect(240, 620, 261, 21))
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.line_12 = QtWidgets.QFrame(self.centralwidget)
        self.line_12.setGeometry(QtCore.QRect(240, 710, 261, 21))
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.label_ev = QtWidgets.QLabel(self.centralwidget)
        self.label_ev.setGeometry(QtCore.QRect(230, 760, 91, 31))
        self.label_ev.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ev.setObjectName("label_ev")
        self.connect_disconnect_spectro_button = QtWidgets.QPushButton(self.centralwidget)
        self.connect_disconnect_spectro_button.setGeometry(QtCore.QRect(400, 20, 101, 31))
        self.connect_disconnect_spectro_button.setObjectName("connect_disconnect_spectro_button")
        self.electrode_label = QtWidgets.QLabel(self.centralwidget)
        self.electrode_label.setGeometry(QtCore.QRect(570, 20, 141, 31))
        self.electrode_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.electrode_label.setObjectName("electrode_label")
        self.electrode_box = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.electrode_box.setGeometry(QtCore.QRect(720, 20, 391, 31))
        self.electrode_box.setObjectName("electrode_box")
        self.empty = QtWidgets.QPushButton(self.centralwidget)
        self.empty.setGeometry(QtCore.QRect(380, 800, 121, 31))
        self.empty.setObjectName("empty")
        self.run_water = QtWidgets.QPushButton(self.centralwidget)
        self.run_water.setGeometry(QtCore.QRect(240, 800, 121, 31))
        self.run_water.setObjectName("run_water")
        self.logo_idil = QtWidgets.QLabel(self.centralwidget)
        self.logo_idil.setGeometry(QtCore.QRect(640, 370, 281, 101))
        self.logo_idil.setAlignment(QtCore.Qt.AlignCenter)
        self.logo_idil.setObjectName("logo_idil")
        self.logo_cnrs = QtWidgets.QLabel(self.centralwidget)
        self.logo_cnrs.setGeometry(QtCore.QRect(1040, 370, 101, 101))
        self.logo_cnrs.setAlignment(QtCore.Qt.AlignCenter)
        self.logo_cnrs.setObjectName("logo_cnrs")
        self.line_13 = QtWidgets.QFrame(self.centralwidget)
        self.line_13.setGeometry(QtCore.QRect(550, 340, 691, 21))
        self.line_13.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        ControlPanel.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ControlPanel)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1262, 18))
        self.menubar.setObjectName("menubar")
        self.menu_file = QtWidgets.QMenu(self.menubar)
        self.menu_file.setObjectName("menu_file")
        self.menu_help = QtWidgets.QMenu(self.menubar)
        self.menu_help.setObjectName("menu_help")
        self.menu_settings = QtWidgets.QMenu(self.menubar)
        self.menu_settings.setObjectName("menu_settings")
        ControlPanel.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ControlPanel)
        self.statusbar.setObjectName("statusbar")
        ControlPanel.setStatusBar(self.statusbar)
        self.action_get_help = QtWidgets.QAction(ControlPanel)
        self.action_get_help.setObjectName("action_get_help")
        self.action_save = QtWidgets.QAction(ControlPanel)
        self.action_save.setObjectName("action_save")
        self.action_edit_folder = QtWidgets.QAction(ControlPanel)
        self.action_edit_folder.setObjectName("action_edit_folder")
        self.action_open_settings = QtWidgets.QAction(ControlPanel)
        self.action_open_settings.setObjectName("action_open_settings")
        self.actionSaving_parameters = QtWidgets.QAction(ControlPanel)
        self.actionSaving_parameters.setObjectName("actionSaving_parameters")
        self.menu_file.addAction(self.action_save)
        self.menu_file.addAction(self.action_edit_folder)
        self.menu_help.addAction(self.action_get_help)
        self.menu_settings.addAction(self.action_open_settings)
        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_settings.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())

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
        self.configure_sequence.setText(_translate("ControlPanel", "Configure Sequence"))
        self.cal_button.setText(_translate("ControlPanel", "CAL"))
        self.spectro_settings.setText(_translate("ControlPanel", "Spectrometry settings"))
        self.save_button.setText(_translate("ControlPanel", "Save current measure"))
        self.label_level.setText(_translate("ControlPanel", "level (0 - 400uL)"))
        self.levelA_uL.setText(_translate("ControlPanel", "0 uL"))
        self.connect_phmeter.setText(_translate("ControlPanel", "Connect"))
        self.connect_disconnect_circuit.setText(_translate("ControlPanel", "Connect"))
        self.stop_syringe.setText(_translate("ControlPanel", "Stop"))
        self.connect_syringe_pump.setText(_translate("ControlPanel", "connect \n"
" Syringe Pump"))
        self.graphic_tabs.setTabText(self.graphic_tabs.indexOf(self.tab1), _translate("ControlPanel", "Absorbance"))
        self.graphic_tabs.setTabText(self.graphic_tabs.indexOf(self.tab_2), _translate("ControlPanel", "Intensity"))
        self.start_stop_pump_button.setText(_translate("ControlPanel", "Start/Stop"))
        self.label_circuit.setText(_translate("ControlPanel", "Circuit"))
        self.change_dir.setText(_translate("ControlPanel", "Change Direction"))
        self.label_model.setText(_translate("ControlPanel", "model :"))
        self.label_added_volume.setText(_translate("ControlPanel", "added volume (uL)"))
        self.added_A_uL.setText(_translate("ControlPanel", "0 uL"))
        self.levelB_uL.setText(_translate("ControlPanel", "0 uL"))
        self.levelbarB.setFormat(_translate("ControlPanel", "%p%"))
        self.levelC_uL.setText(_translate("ControlPanel", "0 uL"))
        self.added_B_uL.setText(_translate("ControlPanel", "0 uL"))
        self.added_C_uL.setText(_translate("ControlPanel", "0 uL"))
        self.label_total_volume.setText(_translate("ControlPanel", "total (uL)"))
        self.added_total.setText(_translate("ControlPanel", "0 uL"))
        self.open_syringe_panel.setText(_translate("ControlPanel", "Syringe Panel"))
        self.close_all.setText(_translate("ControlPanel", "close all devices"))
        self.connect_all_devices.setText(_translate("ControlPanel", "connect all devices"))
        self.led_spectro.setText(_translate("ControlPanel", "led spectro"))
        self.led_phmeter.setText(_translate("ControlPanel", "led phm"))
        self.led_disp.setText(_translate("ControlPanel", "led disp"))
        self.led_pump.setText(_translate("ControlPanel", "led pump"))
        self.syringeA.setText(_translate("ControlPanel", "Syringe A"))
        self.reagentA.setText(_translate("ControlPanel", "Acid (HCl)"))
        self.Ca.setText(_translate("ControlPanel", "0.001"))
        self.syringeB.setText(_translate("ControlPanel", "Syringe B"))
        self.Cc.setText(_translate("ControlPanel", "1"))
        self.Cb.setText(_translate("ControlPanel", "0.01"))
        self.reagentC.setText(_translate("ControlPanel", "Reagent unknown"))
        self.syringeC.setText(_translate("ControlPanel", "Syringe C"))
        self.reagentB.setText(_translate("ControlPanel", "Base (NaOH)"))
        self.label_concentration.setText(_translate("ControlPanel", "Concentration (mol/L)"))
        self.label_reagent.setText(_translate("ControlPanel", "Reagent"))
        self.levelbarA.setFormat(_translate("ControlPanel", "%p%"))
        self.levelbarC.setFormat(_translate("ControlPanel", "%p%"))
        self.label_instrument_SN.setText(_translate("ControlPanel", "Instrument S/N :"))
        self.label_spectro_SN.setText(_translate("ControlPanel", "S/N :"))
        self.ev0_state.setText(_translate("ControlPanel", "IN"))
        self.ev1_state.setText(_translate("ControlPanel", "OUT"))
        self.label_ev0.setText(_translate("ControlPanel", "valve 0"))
        self.label_ev1.setText(_translate("ControlPanel", "valve 1"))
        self.fill_water.setText(_translate("ControlPanel", "Fill water"))
        self.clean_empty.setText(_translate("ControlPanel", "Clean\n"
"empty"))
        self.led_ev_circuit.setText(_translate("ControlPanel", "led ev"))
        self.label_pump.setText(_translate("ControlPanel", "Pump"))
        self.label_ev.setText(_translate("ControlPanel", "Electrovalves"))
        self.connect_disconnect_spectro_button.setText(_translate("ControlPanel", "Connect"))
        self.electrode_label.setText(_translate("ControlPanel", "Electrode model"))
        self.empty.setText(_translate("ControlPanel", "Empty"))
        self.run_water.setText(_translate("ControlPanel", "Run water"))
        self.logo_idil.setText(_translate("ControlPanel", "logo idil"))
        self.logo_cnrs.setText(_translate("ControlPanel", "logo cnrs"))
        self.menu_file.setTitle(_translate("ControlPanel", "file"))
        self.menu_help.setTitle(_translate("ControlPanel", "help"))
        self.menu_settings.setTitle(_translate("ControlPanel", "settings"))
        self.action_get_help.setText(_translate("ControlPanel", "get help"))
        self.action_save.setText(_translate("ControlPanel", "save"))
        self.action_edit_folder.setText(_translate("ControlPanel", "edit saving folder"))
        self.action_open_settings.setText(_translate("ControlPanel", "Instrument settings"))
        self.actionSaving_parameters.setText(_translate("ControlPanel", "Saving parameters"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ControlPanel = QtWidgets.QMainWindow()
    ui = Ui_ControlPanel()
    ui.setupUi(ControlPanel)
    ControlPanel.show()
    sys.exit(app.exec_())
