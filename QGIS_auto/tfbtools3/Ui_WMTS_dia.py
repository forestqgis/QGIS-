# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\admin\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\TFB-Tools3\WMTS_dia.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_WMTS_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(443, 600)
        self.groupBox_4 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 20, 421, 191))
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_3 = QtWidgets.QLabel(self.groupBox_4)
        self.label_3.setGeometry(QtCore.QRect(10, 20, 41, 23))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 50, 91, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.comboBox = QtWidgets.QComboBox(self.groupBox_4)
        self.comboBox.setGeometry(QtCore.QRect(50, 90, 331, 25))
        self.comboBox.setObjectName("comboBox")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_3.setGeometry(QtCore.QRect(290, 120, 91, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_4)
        self.label_4.setGeometry(QtCore.QRect(10, 90, 41, 23))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_7.setGeometry(QtCore.QRect(90, 50, 91, 28))
        self.pushButton_7.setObjectName("pushButton_7")
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox_4)
        self.comboBox_2.setGeometry(QtCore.QRect(50, 20, 331, 25))
        self.comboBox_2.setObjectName("comboBox_2")
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_8.setGeometry(QtCore.QRect(190, 50, 91, 28))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_9.setGeometry(QtCore.QRect(10, 150, 91, 28))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_10.setGeometry(QtCore.QRect(110, 150, 91, 28))
        self.pushButton_10.setObjectName("pushButton_10")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 220, 421, 371))
        self.groupBox.setObjectName("groupBox")
        self.tableWidget_4 = QtWidgets.QTableWidget(self.groupBox)
        self.tableWidget_4.setGeometry(QtCore.QRect(10, 30, 401, 291))
        self.tableWidget_4.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_4.setSelectionMode(
            QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget_4.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.setColumnCount(3)
        self.tableWidget_4.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(2, item)
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4.setGeometry(QtCore.QRect(320, 330, 91, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_6.setGeometry(QtCore.QRect(10, 330, 101, 31))
        self.pushButton_6.setObjectName("pushButton_6")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "連結地圖服務"))
        self.groupBox_4.setTitle(_translate("Dialog", "自行輸入網址"))
        self.label_3.setText(_translate("Dialog", "URL"))
        self.pushButton_2.setText(_translate("Dialog", "取得圖層"))
        self.pushButton_3.setText(_translate("Dialog", "加入列表"))
        self.label_4.setText(_translate("Dialog", "圖層"))
        self.pushButton_7.setText(_translate("Dialog", "新增站台"))
        self.pushButton_8.setText(_translate("Dialog", "移除站台"))
        self.pushButton_9.setText(_translate("Dialog", "匯入設定"))
        self.pushButton_10.setText(_translate("Dialog", "匯出設定"))
        self.groupBox.setTitle(_translate("Dialog", "圖層列表"))
        item = self.tableWidget_4.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "圖層"))
        item = self.tableWidget_4.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "標題"))
        item = self.tableWidget_4.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "url"))
        self.pushButton_4.setText(_translate("Dialog", "套疊圖層"))
        self.pushButton_6.setText(_translate("Dialog", "從列表移除"))
