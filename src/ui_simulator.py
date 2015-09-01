# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'simulator.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(828, 545)
        self.LoadCarButton = QtGui.QPushButton(Form)
        self.LoadCarButton.setGeometry(QtCore.QRect(10, 10, 75, 23))
        self.LoadCarButton.setObjectName(_fromUtf8("LoadCarButton"))
        self.LoadTrackButton = QtGui.QPushButton(Form)
        self.LoadTrackButton.setGeometry(QtCore.QRect(100, 10, 75, 23))
        self.LoadTrackButton.setObjectName(_fromUtf8("LoadTrackButton"))
        self.verticalLayoutWidget = QtGui.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 40, 601, 491))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(630, 160, 54, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(630, 190, 54, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(630, 220, 54, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(630, 250, 54, 21))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(630, 280, 54, 21))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.SpeedEdit = QtGui.QLineEdit(Form)
        self.SpeedEdit.setGeometry(QtCore.QRect(700, 160, 113, 20))
        self.SpeedEdit.setObjectName(_fromUtf8("SpeedEdit"))
        self.AccelerateEdit = QtGui.QLineEdit(Form)
        self.AccelerateEdit.setGeometry(QtCore.QRect(700, 190, 113, 20))
        self.AccelerateEdit.setObjectName(_fromUtf8("AccelerateEdit"))
        self.OffsetEdit = QtGui.QLineEdit(Form)
        self.OffsetEdit.setGeometry(QtCore.QRect(700, 220, 113, 20))
        self.OffsetEdit.setObjectName(_fromUtf8("OffsetEdit"))
        self.TimeEdit = QtGui.QLineEdit(Form)
        self.TimeEdit.setGeometry(QtCore.QRect(700, 250, 113, 20))
        self.TimeEdit.setObjectName(_fromUtf8("TimeEdit"))
        self.CoordinateEdit = QtGui.QLineEdit(Form)
        self.CoordinateEdit.setGeometry(QtCore.QRect(700, 280, 113, 20))
        self.CoordinateEdit.setObjectName(_fromUtf8("CoordinateEdit"))
        self.verticalLayoutWidget_2 = QtGui.QWidget(Form)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(620, 330, 201, 201))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(630, 50, 91, 21))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(720, 50, 71, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.StartButton = QtGui.QPushButton(Form)
        self.StartButton.setGeometry(QtCore.QRect(630, 80, 75, 23))
        self.StartButton.setObjectName(_fromUtf8("StartButton"))
        self.PauseButton = QtGui.QPushButton(Form)
        self.PauseButton.setGeometry(QtCore.QRect(720, 80, 75, 23))
        self.PauseButton.setObjectName(_fromUtf8("PauseButton"))
        self.ResetButton = QtGui.QPushButton(Form)
        self.ResetButton.setGeometry(QtCore.QRect(630, 110, 75, 23))
        self.ResetButton.setObjectName(_fromUtf8("ResetButton"))
        self.SaveButton = QtGui.QPushButton(Form)
        self.SaveButton.setGeometry(QtCore.QRect(720, 110, 75, 23))
        self.SaveButton.setObjectName(_fromUtf8("SaveButton"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "仿真", None))
        self.LoadCarButton.setText(_translate("Form", "加载赛车", None))
        self.LoadTrackButton.setText(_translate("Form", "加载赛道", None))
        self.label.setText(_translate("Form", "速度：", None))
        self.label_2.setText(_translate("Form", "加速度：", None))
        self.label_3.setText(_translate("Form", "偏离距离：", None))
        self.label_4.setText(_translate("Form", "时间：", None))
        self.label_5.setText(_translate("Form", "坐标：", None))
        self.label_6.setText(_translate("Form", "仿真步长(ms)：", None))
        self.StartButton.setText(_translate("Form", "开始仿真", None))
        self.PauseButton.setText(_translate("Form", "暂停仿真", None))
        self.ResetButton.setText(_translate("Form", "复位", None))
        self.SaveButton.setText(_translate("Form", "保存数据", None))

