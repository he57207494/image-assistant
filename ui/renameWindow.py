# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'renameWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow


class Ui_renameWindow(QMainWindow):
    def __init__(self):
        super(Ui_renameWindow, self).__init__()
        self.setupUi(self)
    def setupUi(self, renameWindow):
        renameWindow.setObjectName("renameWindow")
        renameWindow.resize(473, 467)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./image/favicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        renameWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(renameWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 441, 141))
        self.groupBox.setObjectName("groupBox")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(20, 30, 89, 16))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(110, 30, 89, 16))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_3.setGeometry(QtCore.QRect(20, 60, 89, 16))
        self.radioButton_3.setObjectName("radioButton_3")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 90, 61, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(170, 90, 61, 21))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(230, 90, 61, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(300, 90, 61, 21))
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(360, 90, 61, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_3.setGeometry(QtCore.QRect(80, 90, 61, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 160, 441, 251))
        self.groupBox_2.setObjectName("groupBox_2")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(90, 30, 201, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(10, 30, 91, 21))
        self.label_7.setObjectName("label_7")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(300, 30, 51, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(360, 30, 51, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox_2)
        self.tableWidget.setGeometry(QtCore.QRect(10, 60, 421, 181))
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        renameWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(renameWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 473, 23))
        self.menubar.setObjectName("menubar")
        renameWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(renameWindow)
        self.statusbar.setObjectName("statusbar")
        renameWindow.setStatusBar(self.statusbar)

        self.retranslateUi(renameWindow)
        QtCore.QMetaObject.connectSlotsByName(renameWindow)

    def retranslateUi(self, renameWindow):
        _translate = QtCore.QCoreApplication.translate
        renameWindow.setWindowTitle(_translate("renameWindow", "批量重命名"))
        self.groupBox.setTitle(_translate("renameWindow", "重命名设置"))
        self.radioButton.setText(_translate("renameWindow", "文件名大写"))
        self.radioButton_2.setText(_translate("renameWindow", "文件名小写"))
        self.radioButton_3.setText(_translate("renameWindow", "文件名编号"))
        self.label.setText(_translate("renameWindow", "设置模版："))
        self.label_2.setText(_translate("renameWindow", "起始编号："))
        self.label_3.setText(_translate("renameWindow", "编号增量："))
        self.groupBox_2.setTitle(_translate("renameWindow", "图片设置"))
        self.label_7.setText(_translate("renameWindow", "选择图片路径："))
        self.pushButton.setText(_translate("renameWindow", "选择"))
        self.pushButton_2.setText(_translate("renameWindow", "重命名"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("renameWindow", "图片名"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("renameWindow", "图片路径"))
