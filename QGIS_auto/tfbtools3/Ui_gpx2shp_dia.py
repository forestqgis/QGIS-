# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\vincentlu\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\tfb_tools3\gpx2shp_dia.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_gpx2shp_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(391, 372)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(140, 310, 91, 35))
        self.pushButton.setObjectName("pushButton")
        self.groupBox_4 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 20, 361, 151))
        self.groupBox_4.setObjectName("groupBox_4")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 70, 331, 61))
        self.groupBox_3.setObjectName("groupBox_3")
        self.radioButton_5 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_5.setGeometry(QtCore.QRect(210, 30, 81, 20))
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_3.setGeometry(QtCore.QRect(40, 30, 111, 20))
        self.radioButton_3.setObjectName("radioButton_3")
        self.label = QtWidgets.QLabel(self.groupBox_4)
        self.label.setGeometry(QtCore.QRect(10, 30, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setGeometry(QtCore.QRect(90, 30, 221, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.toolButton = QtWidgets.QToolButton(self.groupBox_4)
        self.toolButton.setGeometry(QtCore.QRect(320, 30, 25, 25))
        self.toolButton.setObjectName("toolButton")
        self.groupBox_5 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 190, 361, 101))
        self.groupBox_5.setObjectName("groupBox_5")
        self.comboBox = QtWidgets.QComboBox(self.groupBox_5)
        self.comboBox.setGeometry(QtCore.QRect(160, 60, 131, 25))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_3 = QtWidgets.QLabel(self.groupBox_5)
        self.label_3.setGeometry(QtCore.QRect(20, 60, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.groupBox_5)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 20, 221, 25))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.toolButton_2 = QtWidgets.QToolButton(self.groupBox_5)
        self.toolButton_2.setGeometry(QtCore.QRect(330, 20, 25, 25))
        self.toolButton_2.setObjectName("toolButton_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "GPX to shapefile"))
        self.pushButton.setText(_translate("Dialog", "開始轉換"))
        self.groupBox_4.setTitle(_translate("Dialog", "輸入"))
        self.groupBox_3.setTitle(_translate("Dialog", "請選擇要增加的向量類型"))
        self.radioButton_5.setText(_translate("Dialog", "track(線)"))
        self.radioButton_3.setText(_translate("Dialog", "track_point(點)"))
        self.label.setText(_translate("Dialog", "輸入GPX"))
        self.toolButton.setText(_translate("Dialog", "..."))
        self.groupBox_5.setTitle(_translate("Dialog", "輸出"))
        self.comboBox.setItemText(0, _translate("Dialog", "WGS 84"))
        self.comboBox.setItemText(1, _translate("Dialog", "TWD 97"))
        self.label_3.setText(_translate("Dialog", "請選擇輸出檔案坐標系統"))
        self.label_2.setText(_translate("Dialog", "輸出SHP"))
        self.toolButton_2.setText(_translate("Dialog", "..."))


