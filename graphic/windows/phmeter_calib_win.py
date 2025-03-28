# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'graphic/ui_files/phmeter_calib.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_calibration_window(object):
    def setupUi(self, calibration_window):
        calibration_window.setObjectName("calibration_window")
        calibration_window.resize(440, 290)
        self.buttonBox = QtWidgets.QDialogButtonBox(calibration_window)
        self.buttonBox.setGeometry(QtCore.QRect(190, 220, 231, 51))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Apply|QtWidgets.QDialogButtonBox.Cancel)
        self.buttonBox.setObjectName("buttonBox")
        self.lcdNumber = QtWidgets.QLCDNumber(calibration_window)
        self.lcdNumber.setGeometry(QtCore.QRect(210, 80, 211, 131))
        self.lcdNumber.setObjectName("lcdNumber")
        self.label = QtWidgets.QLabel(calibration_window)
        self.label.setGeometry(QtCore.QRect(260, 40, 131, 41))
        self.label.setObjectName("label")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(calibration_window)
        self.lcdNumber_2.setGeometry(QtCore.QRect(30, 50, 71, 51))
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.lcdNumber_3 = QtWidgets.QLCDNumber(calibration_window)
        self.lcdNumber_3.setGeometry(QtCore.QRect(30, 130, 71, 51))
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.lcdNumber_4 = QtWidgets.QLCDNumber(calibration_window)
        self.lcdNumber_4.setGeometry(QtCore.QRect(30, 210, 71, 51))
        self.lcdNumber_4.setObjectName("lcdNumber_4")
        self.pushButton = QtWidgets.QPushButton(calibration_window)
        self.pushButton.setGeometry(QtCore.QRect(130, 210, 51, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(calibration_window)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 130, 51, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(calibration_window)
        self.pushButton_3.setGeometry(QtCore.QRect(130, 50, 51, 51))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_2 = QtWidgets.QLabel(calibration_window)
        self.label_2.setGeometry(QtCore.QRect(30, 10, 151, 31))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(calibration_window)
        self.buttonBox.accepted.connect(calibration_window.accept) # type: ignore
        self.buttonBox.rejected.connect(calibration_window.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(calibration_window)

    def retranslateUi(self, calibration_window):
        _translate = QtCore.QCoreApplication.translate
        calibration_window.setWindowTitle(_translate("calibration_window", "pH meter calibration"))
        self.label.setText(_translate("calibration_window", "tension (mV) en direct"))
        self.pushButton.setText(_translate("calibration_window", "pH10"))
        self.pushButton_2.setText(_translate("calibration_window", "pH7"))
        self.pushButton_3.setText(_translate("calibration_window", "pH4"))
        self.label_2.setText(_translate("calibration_window", "Tensions enregistrées"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    calibration_window = QtWidgets.QDialog()
    ui = Ui_calibration_window()
    ui.setupUi(calibration_window)
    calibration_window.show()
    sys.exit(app.exec_())
