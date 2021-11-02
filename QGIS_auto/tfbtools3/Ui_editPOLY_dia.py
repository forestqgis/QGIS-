# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\johnvoo\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\TFB-Tools3\editPOLY_dia.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_editPOLY_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(333, 220)
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 80, 111, 35))
        self.pushButton_4.setObjectName("pushButton_4")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBox.setGeometry(QtCore.QRect(20, 150, 151, 22))
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.doubleSpinBox.setSuffix(" m2")
        self.doubleSpinBox.setMaximum(999999999)
        self.doubleSpinBox.setDecimals(0)
        self.labelX = QtWidgets.QLabel(Dialog)
        self.labelX.setEnabled(False)
        self.labelX.setGeometry(QtCore.QRect(20, 250, 47, 12))
        self.labelX.setObjectName("labelX")
        self.labelY = QtWidgets.QLabel(Dialog)
        self.labelY.setEnabled(False)
        self.labelY.setGeometry(QtCore.QRect(80, 250, 47, 12))
        self.labelY.setObjectName("labelY")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(200, 140, 111, 35))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(150, 30, 71, 16))
        self.label.setObjectName("label")
        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(20, 20, 111, 35))
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(150, 80, 71, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(220, 30, 71, 16))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.msg_label = QtWidgets.QLabel(Dialog)
        self.msg_label.setEnabled(False)
        self.msg_label.setGeometry(QtCore.QRect(20, 190, 47, 12))
        self.msg_label.setText("")
        self.msg_label.setObjectName("msg_label")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 130, 141, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(150, 100, 171, 16))
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.lastPolyArea = any

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_4.setText(_translate("Dialog", "選擇頂點"))
        self.labelX.setText(_translate("Dialog", "TextLabel"))
        self.labelY.setText(_translate("Dialog", "TextLabel"))
        self.pushButton_5.setText(_translate("Dialog", "修正"))
        self.label.setText(_translate("Dialog", "目前面積："))
        self.pushButton_6.setText(_translate("Dialog", "點選圖徵"))
        self.label_2.setText(_translate("Dialog", "可異動區間："))
        self.label_4.setText(_translate("Dialog", "輸入面積："))
