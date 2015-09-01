# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'car_design.ui'
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
        Form.resize(263, 240)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 20, 54, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.LengthEdit = QtGui.QLineEdit(Form)
        self.LengthEdit.setGeometry(QtCore.QRect(100, 20, 61, 20))
        self.LengthEdit.setObjectName(_fromUtf8("LengthEdit"))
        self.WidthEdit = QtGui.QLineEdit(Form)
        self.WidthEdit.setGeometry(QtCore.QRect(190, 20, 61, 20))
        self.WidthEdit.setObjectName(_fromUtf8("WidthEdit"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(80, 20, 21, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(170, 20, 16, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(10, 50, 54, 21))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.DisEdit = QtGui.QLineEdit(Form)
        self.DisEdit.setGeometry(QtCore.QRect(80, 50, 171, 20))
        self.DisEdit.setObjectName(_fromUtf8("DisEdit"))
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(10, 80, 54, 21))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.WeightEdit = QtGui.QLineEdit(Form)
        self.WeightEdit.setGeometry(QtCore.QRect(80, 80, 171, 20))
        self.WeightEdit.setObjectName(_fromUtf8("WeightEdit"))
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(10, 110, 54, 21))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.FcoffEdit = QtGui.QLineEdit(Form)
        self.FcoffEdit.setGeometry(QtCore.QRect(80, 110, 171, 20))
        self.FcoffEdit.setObjectName(_fromUtf8("FcoffEdit"))
        self.label_7 = QtGui.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(10, 140, 54, 21))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.TorqueEdit = QtGui.QLineEdit(Form)
        self.TorqueEdit.setGeometry(QtCore.QRect(80, 140, 171, 20))
        self.TorqueEdit.setObjectName(_fromUtf8("TorqueEdit"))
        self.PowerEdit = QtGui.QLineEdit(Form)
        self.PowerEdit.setGeometry(QtCore.QRect(80, 170, 171, 20))
        self.PowerEdit.setObjectName(_fromUtf8("PowerEdit"))
        self.label_8 = QtGui.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(10, 170, 54, 21))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.OpenButton = QtGui.QPushButton(Form)
        self.OpenButton.setGeometry(QtCore.QRect(30, 200, 75, 23))
        self.OpenButton.setObjectName(_fromUtf8("OpenButton"))
        self.SaveButton = QtGui.QPushButton(Form)
        self.SaveButton.setGeometry(QtCore.QRect(160, 200, 75, 23))
        self.SaveButton.setObjectName(_fromUtf8("SaveButton"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "赛车设计", None))
        self.label.setText(_translate("Form", "车身(mm)：", None))
        self.label_2.setText(_translate("Form", "长", None))
        self.label_3.setText(_translate("Form", "宽", None))
        self.label_4.setText(_translate("Form", "轮间距：", None))
        self.label_5.setText(_translate("Form", "重量：", None))
        self.label_6.setText(_translate("Form", "摩擦系数：", None))
        self.label_7.setText(_translate("Form", "扭矩比：", None))
        self.label_8.setText(_translate("Form", "电机功率：", None))
        self.OpenButton.setText(_translate("Form", "打开", None))
        self.SaveButton.setText(_translate("Form", "保存", None))

