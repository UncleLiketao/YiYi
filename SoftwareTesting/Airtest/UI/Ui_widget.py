# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\Game\BC\test\UI\test.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from UI.QLineTextBrowser import QLineTextBrowser


class Ui_widget(object):
    def setupUi(self, widget):
        widget.setObjectName("widget")
        widget.resize(722, 899)
        widget.setAcceptDrops(True)
        self.groupBox = QtWidgets.QGroupBox(widget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 701, 61))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(10, 10, 89, 16))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(10, 40, 89, 16))
        self.radioButton_2.setObjectName("radioButton_2")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox.setGeometry(QtCore.QRect(450, 30, 71, 16))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_2.setGeometry(QtCore.QRect(270, 20, 71, 16))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_4 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_4.setGeometry(QtCore.QRect(350, 10, 71, 16))
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_3.setGeometry(QtCore.QRect(350, 40, 71, 16))
        self.checkBox_3.setObjectName("checkBox_3")
        self.groupBox_2 = QtWidgets.QGroupBox(widget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 80, 701, 131))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 54, 12))
        self.label_2.setObjectName("label_2")
        self.spinBox = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox.setGeometry(QtCore.QRect(20, 30, 71, 31))
        self.spinBox.setMinimum(1)
        self.spinBox.setObjectName("spinBox")
        self.radioButton_6 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_6.setGeometry(QtCore.QRect(110, 10, 89, 21))
        self.radioButton_6.setObjectName("radioButton_6")
        self.comboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox.setGeometry(QtCore.QRect(110, 30, 91, 31))
        self.comboBox.setCurrentText("")
        self.comboBox.setIconSize(QtCore.QSize(16, 20))
        self.comboBox.setObjectName("comboBox")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_5.setGeometry(QtCore.QRect(540, 10, 75, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_6.setGeometry(QtCore.QRect(460, 10, 75, 31))
        self.pushButton_6.setObjectName("pushButton_6")
        self.checkBox_5 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_5.setGeometry(QtCore.QRect(20, 70, 121, 21))
        self.checkBox_5.setObjectName("checkBox_5")
        self.spinBox_2 = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_2.setGeometry(QtCore.QRect(20, 90, 111, 31))
        self.spinBox_2.setMinimum(1)
        self.spinBox_2.setObjectName("spinBox_2")
        self.adblog = QtWidgets.QPushButton(self.groupBox_2)
        self.adblog.setGeometry(QtCore.QRect(460, 60, 81, 23))
        self.adblog.setObjectName("adblog")
        self.inputlog = QtWidgets.QPushButton(self.groupBox_2)
        self.inputlog.setGeometry(QtCore.QRect(460, 90, 81, 23))
        self.inputlog.setObjectName("inputlog")
        self.groupBox_3 = QtWidgets.QGroupBox(widget)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 310, 701, 41))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 10, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.FileTextBrowser = QtWidgets.QTextEdit(self.groupBox_3)
        self.FileTextBrowser.setGeometry(QtCore.QRect(90, 10, 591, 21))
        self.FileTextBrowser.setInputMethodHints(QtCore.Qt.ImhNone)
        self.FileTextBrowser.setObjectName("FileTextBrowser")
        self.pushButton = QtWidgets.QPushButton(widget)
        self.pushButton.setGeometry(QtCore.QRect(10, 840, 681, 23))
        self.pushButton.setObjectName("pushButton")
        self.groupBox_4 = QtWidgets.QGroupBox(widget)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 360, 701, 201))
        self.groupBox_4.setObjectName("groupBox_4")
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox_4)
        self.textBrowser.setGeometry(QtCore.QRect(10, 20, 681, 171))
        self.textBrowser.setAcceptDrops(False)
        self.textBrowser.setObjectName("textBrowser")
        self.groupBox_5 = QtWidgets.QGroupBox(widget)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 570, 701, 261))
        self.groupBox_5.setObjectName("groupBox_5")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.groupBox_5)
        self.textBrowser_2.setGeometry(QtCore.QRect(10, 20, 681, 231))
        self.textBrowser_2.setAcceptDrops(False)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.groupBox_6 = QtWidgets.QGroupBox(widget)
        self.groupBox_6.setGeometry(QtCore.QRect(10, 220, 701, 80))
        self.groupBox_6.setAcceptDrops(True)
        self.groupBox_6.setTitle("")
        self.groupBox_6.setObjectName("groupBox_6")
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_8.setGeometry(QtCore.QRect(10, 50, 75, 23))
        self.pushButton_8.setObjectName("pushButton_8")
        self.PkgFile = QLineTextBrowser(self.groupBox_6)
        self.PkgFile.setGeometry(QtCore.QRect(90, 50, 591, 21))
        self.PkgFile.setInputMethodHints(QtCore.Qt.ImhMultiLine)
        self.PkgFile.setTabChangesFocus(True)
        self.PkgFile.setReadOnly(False)
        self.PkgFile.setOpenExternalLinks(True)
        self.PkgFile.setObjectName("PkgFile")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_4.setGeometry(QtCore.QRect(280, 10, 75, 21))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_3.setGeometry(QtCore.QRect(390, 10, 75, 21))
        self.pushButton_3.setObjectName("pushButton_3")
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox_6)
        self.comboBox_2.setGeometry(QtCore.QRect(80, 10, 151, 21))
        self.comboBox_2.setObjectName("comboBox_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_6)
        self.label_4.setGeometry(QtCore.QRect(10, 20, 54, 12))
        self.label_4.setObjectName("label_4")
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_7.setGeometry(QtCore.QRect(240, 10, 21, 23))
        self.pushButton_7.setText("")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_9 = QtWidgets.QPushButton(widget)
        self.pushButton_9.setGeometry(QtCore.QRect(10, 840, 691, 23))
        self.pushButton_9.setObjectName("pushButton_9")

        self.retranslateUi(widget)
        self.comboBox.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(widget)

    def retranslateUi(self, widget):
        _translate = QtCore.QCoreApplication.translate
        widget.setWindowTitle(_translate("widget", "自动测试"))
        self.radioButton.setText(_translate("widget", "Air"))
        self.radioButton_2.setText(_translate("widget", "Poco"))
        self.checkBox.setText(_translate("widget", "是否UPR"))
        self.checkBox_2.setText(_translate("widget", "断线重连"))
        self.checkBox_4.setText(_translate("widget", "小重连"))
        self.checkBox_3.setText(_translate("widget", "wifi关闭"))
        self.label_2.setText(_translate("widget", "循环次数："))
        self.radioButton_6.setText(_translate("widget", "测试文件"))
        self.pushButton_5.setText(_translate("widget", "关闭wifi"))
        self.pushButton_6.setText(_translate("widget", "开启wifi"))
        self.checkBox_5.setText(_translate("widget", "结束后需要跑流程"))
        self.adblog.setText(_translate("widget", "打开日志"))
        self.inputlog.setText(_translate("widget", "输出日志"))
        self.pushButton_2.setText(_translate("widget", "文件路径"))
        self.pushButton.setText(_translate("widget", "开始测试"))
        self.groupBox_4.setTitle(_translate("widget", "输出"))
        self.groupBox_5.setTitle(_translate("widget", "错误信息"))
        self.pushButton_8.setText(_translate("widget", "安装游戏"))
        self.pushButton_4.setText(_translate("widget", "启动游戏"))
        self.pushButton_3.setText(_translate("widget", "关闭游戏"))
        self.label_4.setText(_translate("widget", "连接设备："))
        self.pushButton_9.setText(_translate("widget", "停止测试"))
