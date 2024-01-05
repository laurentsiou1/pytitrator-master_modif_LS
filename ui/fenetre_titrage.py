# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files/fenetre_titrage.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_titrationWindow(object):
    def setupUi(self, titrationWindow):
        titrationWindow.setObjectName("titrationWindow")
        titrationWindow.resize(1759, 941)
        titrationWindow.setTabletTracking(False)
        titrationWindow.setIconSize(QtCore.QSize(18, 27))
        self.centralwidget = QtWidgets.QWidget(titrationWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.direct_pH = QtWidgets.QLCDNumber(self.centralwidget)
        self.direct_pH.setGeometry(QtCore.QRect(10, 490, 121, 61))
        self.direct_pH.setObjectName("direct_pH")
        self.stabilisation_level = QtWidgets.QProgressBar(self.centralwidget)
        self.stabilisation_level.setGeometry(QtCore.QRect(150, 510, 151, 41))
        self.stabilisation_level.setMaximum(100)
        self.stabilisation_level.setProperty("value", 0)
        self.stabilisation_level.setTextVisible(False)
        self.stabilisation_level.setOrientation(QtCore.Qt.Horizontal)
        self.stabilisation_level.setObjectName("stabilisation_level")
        self.label_pH = QtWidgets.QLabel(self.centralwidget)
        self.label_pH.setGeometry(QtCore.QRect(30, 450, 61, 41))
        self.label_pH.setObjectName("label_pH")
        self.label_direct_abs = QtWidgets.QLabel(self.centralwidget)
        self.label_direct_abs.setGeometry(QtCore.QRect(40, 20, 171, 41))
        self.label_direct_abs.setObjectName("label_direct_abs")
        self.label_stability = QtWidgets.QLabel(self.centralwidget)
        self.label_stability.setGeometry(QtCore.QRect(150, 450, 71, 41))
        self.label_stability.setObjectName("label_stability")
        self.ajout_ok = QtWidgets.QPushButton(self.centralwidget)
        self.ajout_ok.setGeometry(QtCore.QRect(140, 590, 61, 41))
        self.ajout_ok.setObjectName("ajout_ok")
        self.label_base_level = QtWidgets.QLabel(self.centralwidget)
        self.label_base_level.setGeometry(QtCore.QRect(50, 680, 251, 41))
        self.label_base_level.setAutoFillBackground(False)
        self.label_base_level.setObjectName("label_base_level")
        self.base_level_number = QtWidgets.QLabel(self.centralwidget)
        self.base_level_number.setGeometry(QtCore.QRect(50, 710, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.base_level_number.setFont(font)
        self.base_level_number.setObjectName("base_level_number")
        self.base_level_bar = QtWidgets.QProgressBar(self.centralwidget)
        self.base_level_bar.setGeometry(QtCore.QRect(50, 750, 201, 41))
        self.base_level_bar.setMinimum(0)
        self.base_level_bar.setMaximum(500)
        self.base_level_bar.setProperty("value", 0)
        self.base_level_bar.setTextVisible(False)
        self.base_level_bar.setOrientation(QtCore.Qt.Horizontal)
        self.base_level_bar.setInvertedAppearance(False)
        self.base_level_bar.setObjectName("base_level_bar")
        self.label_pump_speed = QtWidgets.QLabel(self.centralwidget)
        self.label_pump_speed.setGeometry(QtCore.QRect(30, 830, 171, 41))
        self.label_pump_speed.setObjectName("label_pump_speed")
        self.background_and_reference = QtWidgets.QPushButton(self.centralwidget)
        self.background_and_reference.setGeometry(QtCore.QRect(330, 20, 201, 41))
        self.background_and_reference.setObjectName("background_and_reference")
        self.label_delta_abs = QtWidgets.QLabel(self.centralwidget)
        self.label_delta_abs.setGeometry(QtCore.QRect(670, 10, 371, 41))
        self.label_delta_abs.setObjectName("label_delta_abs")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(650, 770, 1081, 101))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.grid_all_pH_vol = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.grid_all_pH_vol.setContentsMargins(0, 0, 0, 0)
        self.grid_all_pH_vol.setObjectName("grid_all_pH_vol")
        self.label_pH_2 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_pH_2.setObjectName("label_pH_2")
        self.grid_all_pH_vol.addWidget(self.label_pH_2, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.grid_all_pH_vol.addWidget(self.label_3, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.grid_all_pH_vol.addWidget(self.label_5, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.grid_all_pH_vol.addWidget(self.label_6, 0, 2, 1, 1)
        self.label_vol = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_vol.setObjectName("label_vol")
        self.grid_all_pH_vol.addWidget(self.label_vol, 1, 0, 1, 1)
        self.label_measure = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_measure.setObjectName("label_measure")
        self.grid_all_pH_vol.addWidget(self.label_measure, 0, 0, 1, 1)
        self.total_volume = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.total_volume.setObjectName("total_volume")
        self.grid_all_pH_vol.addWidget(self.total_volume, 1, 3, 1, 1)
        self.label_total_volume = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_total_volume.setObjectName("label_total_volume")
        self.grid_all_pH_vol.addWidget(self.label_total_volume, 0, 3, 1, 1)
        self.added_acid_label = QtWidgets.QLabel(self.centralwidget)
        self.added_acid_label.setGeometry(QtCore.QRect(70, 550, 211, 41))
        self.added_acid_label.setAutoFillBackground(False)
        self.added_acid_label.setObjectName("added_acid_label")
        self.added_acid = QtWidgets.QSpinBox(self.centralwidget)
        self.added_acid.setGeometry(QtCore.QRect(70, 590, 61, 41))
        self.added_acid.setObjectName("added_acid")
        self.experiment_parameters = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.experiment_parameters.setGeometry(QtCore.QRect(320, 460, 291, 411))
        self.experiment_parameters.setObjectName("experiment_parameters")
        self.pump_speed_rpm = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.pump_speed_rpm.setGeometry(QtCore.QRect(170, 830, 81, 41))
        self.pump_speed_rpm.setAccessibleName("")
        self.pump_speed_rpm.setDecimals(0)
        self.pump_speed_rpm.setMaximum(1000.0)
        self.pump_speed_rpm.setSingleStep(0.0)
        self.pump_speed_rpm.setProperty("value", 400.0)
        self.pump_speed_rpm.setObjectName("pump_speed_rpm")
        self.stab_time = QtWidgets.QSpinBox(self.centralwidget)
        self.stab_time.setGeometry(QtCore.QRect(231, 461, 71, 41))
        self.stab_time.setMinimum(5)
        self.stab_time.setMaximum(600)
        self.stab_time.setProperty("value", 15)
        self.stab_time.setObjectName("stab_time")
        self.absorbance_tabs = QtWidgets.QTabWidget(self.centralwidget)
        self.absorbance_tabs.setGeometry(QtCore.QRect(650, 50, 1081, 681))
        self.absorbance_tabs.setObjectName("absorbance_tabs")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        self.absorbance_tabs.addTab(self.tab1, "")
        self.tab2 = QtWidgets.QWidget()
        self.tab2.setObjectName("tab2")
        self.absorbance_tabs.addTab(self.tab2, "")
        self.widget_direct = QtWidgets.QWidget(self.centralwidget)
        self.widget_direct.setGeometry(QtCore.QRect(20, 80, 591, 341))
        self.widget_direct.setObjectName("widget_direct")
        titrationWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(titrationWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1759, 18))
        self.menubar.setObjectName("menubar")
        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setObjectName("menufile")
        self.menuhelp = QtWidgets.QMenu(self.menubar)
        self.menuhelp.setObjectName("menuhelp")
        titrationWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(titrationWindow)
        self.statusbar.setObjectName("statusbar")
        titrationWindow.setStatusBar(self.statusbar)
        self.actionsave = QtWidgets.QAction(titrationWindow)
        self.actionsave.setObjectName("actionsave")
        self.actionquit = QtWidgets.QAction(titrationWindow)
        self.actionquit.setObjectName("actionquit")
        self.actionedit_saving_folder = QtWidgets.QAction(titrationWindow)
        self.actionedit_saving_folder.setObjectName("actionedit_saving_folder")
        self.menufile.addAction(self.actionsave)
        self.menufile.addAction(self.actionedit_saving_folder)
        self.menufile.addAction(self.actionquit)
        self.menubar.addAction(self.menufile.menuAction())
        self.menubar.addAction(self.menuhelp.menuAction())

        self.retranslateUi(titrationWindow)
        self.absorbance_tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(titrationWindow)

    def retranslateUi(self, titrationWindow):
        _translate = QtCore.QCoreApplication.translate
        titrationWindow.setWindowTitle(_translate("titrationWindow", "Titration Window"))
        self.stabilisation_level.setFormat(_translate("titrationWindow", "%p%"))
        self.label_pH.setText(_translate("titrationWindow", "pH"))
        self.label_direct_abs.setText(_translate("titrationWindow", "Intensity"))
        self.label_stability.setText(_translate("titrationWindow", "stability"))
        self.ajout_ok.setText(_translate("titrationWindow", "Ok"))
        self.label_base_level.setText(_translate("titrationWindow", "base syringe level (0 - 500uL)"))
        self.base_level_number.setText(_translate("titrationWindow", "0 uL"))
        self.base_level_bar.setFormat(_translate("titrationWindow", "%p%"))
        self.label_pump_speed.setText(_translate("titrationWindow", "pump speed rpm"))
        self.background_and_reference.setText(_translate("titrationWindow", "Spectro parameters"))
        self.label_delta_abs.setText(_translate("titrationWindow", "Absorbance (Raw and Delta)"))
        self.label_pH_2.setText(_translate("titrationWindow", "pH"))
        self.label_5.setText(_translate("titrationWindow", "1"))
        self.label_6.setText(_translate("titrationWindow", "2"))
        self.label_vol.setText(_translate("titrationWindow", "vol"))
        self.label_measure.setText(_translate("titrationWindow", "measure"))
        self.total_volume.setText(_translate("titrationWindow", "550"))
        self.label_total_volume.setText(_translate("titrationWindow", "total volume"))
        self.added_acid_label.setText(_translate("titrationWindow", "added acid (HCl 0.1M) uL"))
        self.experiment_parameters.setPlainText(_translate("titrationWindow", "Experience name :\n"
"Description :\n"
"\n"
"Parameters ..."))
        self.absorbance_tabs.setTabText(self.absorbance_tabs.indexOf(self.tab1), _translate("titrationWindow", "Tab 1"))
        self.absorbance_tabs.setTabText(self.absorbance_tabs.indexOf(self.tab2), _translate("titrationWindow", "Tab 2"))
        self.menufile.setTitle(_translate("titrationWindow", "file"))
        self.menuhelp.setTitle(_translate("titrationWindow", "help"))
        self.actionsave.setText(_translate("titrationWindow", "save titration"))
        self.actionquit.setText(_translate("titrationWindow", "quit"))
        self.actionedit_saving_folder.setText(_translate("titrationWindow", "edit saving folder"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    titrationWindow = QtWidgets.QMainWindow()
    ui = Ui_titrationWindow()
    ui.setupUi(titrationWindow)
    titrationWindow.show()
    sys.exit(app.exec_())
