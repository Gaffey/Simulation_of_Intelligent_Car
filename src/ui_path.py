# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_design.ui'
#
# Created: Sat Mar 14 19:51:21 2015
#      by: PyQt4 UI code generator 4.10.4
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
        Form.resize(1000, 600)
        self.verticalLayoutWidget = QtGui.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 30, 631, 531))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.CenterLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.CenterLayout.setMargin(0)
        self.CenterLayout.setObjectName(_fromUtf8("CenterLayout"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 570, 54, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.CoordinateLabel = QtGui.QLabel(Form)
        self.CoordinateLabel.setGeometry(QtCore.QRect(40, 570, 54, 21))
        self.CoordinateLabel.setObjectName(_fromUtf8("CoordinateLabel"))
        self.LineButton = QtGui.QPushButton(Form)
        self.LineButton.setGeometry(QtCore.QRect(650, 30, 41, 41))
        self.LineButton.setObjectName(_fromUtf8("LineButton"))
        self.ArcButton = QtGui.QPushButton(Form)
        self.ArcButton.setGeometry(QtCore.QRect(650, 80, 41, 41))
        self.ArcButton.setObjectName(_fromUtf8("ArcButton"))
        self.CrossButton = QtGui.QPushButton(Form)
        self.CrossButton.setGeometry(QtCore.QRect(650, 130, 41, 41))
        self.CrossButton.setObjectName(_fromUtf8("CrossButton"))
        self.BarrierButton = QtGui.QPushButton(Form)
        self.BarrierButton.setGeometry(QtCore.QRect(650, 180, 41, 41))
        self.BarrierButton.setObjectName(_fromUtf8("BarrierButton"))
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(700, 220, 54, 12))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_13 = QtGui.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(710, 20, 54, 12))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.layoutWidget = QtGui.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(710, 40, 270, 154))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.LightEdit = QtGui.QLineEdit(self.layoutWidget)
        self.LightEdit.setObjectName(_fromUtf8("LightEdit"))
        self.gridLayout_2.addWidget(self.LightEdit, 5, 1, 1, 1)
        self.TWidthEdit = QtGui.QLineEdit(self.layoutWidget)
        self.TWidthEdit.setObjectName(_fromUtf8("TWidthEdit"))
        self.gridLayout_2.addWidget(self.TWidthEdit, 1, 1, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.MinEdit = QtGui.QLineEdit(self.layoutWidget)
        self.MinEdit.setObjectName(_fromUtf8("MinEdit"))
        self.horizontalLayout.addWidget(self.MinEdit)
        self.label_20 = QtGui.QLabel(self.layoutWidget)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.horizontalLayout.addWidget(self.label_20)
        self.MaxEdit = QtGui.QLineEdit(self.layoutWidget)
        self.MaxEdit.setObjectName(_fromUtf8("MaxEdit"))
        self.horizontalLayout.addWidget(self.MaxEdit)
        self.gridLayout_2.addLayout(self.horizontalLayout, 3, 1, 1, 1)
        self.label_17 = QtGui.QLabel(self.layoutWidget)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.gridLayout_2.addWidget(self.label_17, 1, 0, 1, 1)
        self.TLengthEdit = QtGui.QLineEdit(self.layoutWidget)
        self.TLengthEdit.setObjectName(_fromUtf8("TLengthEdit"))
        self.gridLayout_2.addWidget(self.TLengthEdit, 0, 1, 1, 1)
        self.label_18 = QtGui.QLabel(self.layoutWidget)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.gridLayout_2.addWidget(self.label_18, 2, 0, 1, 1)
        self.label_19 = QtGui.QLabel(self.layoutWidget)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.gridLayout_2.addWidget(self.label_19, 3, 0, 1, 1)
        self.label_14 = QtGui.QLabel(self.layoutWidget)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout_2.addWidget(self.label_14, 4, 0, 1, 1)
        self.FrictionEdit = QtGui.QLineEdit(self.layoutWidget)
        self.FrictionEdit.setObjectName(_fromUtf8("FrictionEdit"))
        self.gridLayout_2.addWidget(self.FrictionEdit, 4, 1, 1, 1)
        self.label_15 = QtGui.QLabel(self.layoutWidget)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.gridLayout_2.addWidget(self.label_15, 5, 0, 1, 1)
        self.label_16 = QtGui.QLabel(self.layoutWidget)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.gridLayout_2.addWidget(self.label_16, 0, 0, 1, 1)
        self.comboBox = QtGui.QComboBox(self.layoutWidget)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.comboBox, 2, 1, 1, 1)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(100, 570, 54, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.StateLabel = QtGui.QLabel(Form)
        self.StateLabel.setGeometry(QtCore.QRect(170, 570, 381, 21))
        self.StateLabel.setText(_fromUtf8(""))
        self.StateLabel.setObjectName(_fromUtf8("StateLabel"))
        self.RampButton = QtGui.QPushButton(Form)
        self.RampButton.setGeometry(QtCore.QRect(650, 230, 41, 41))
        self.RampButton.setObjectName(_fromUtf8("RampButton"))
        self.RightAngleButton = QtGui.QPushButton(Form)
        self.RightAngleButton.setGeometry(QtCore.QRect(650, 280, 41, 41))
        self.RightAngleButton.setObjectName(_fromUtf8("RightAngleButton"))
        self.label_21 = QtGui.QLabel(Form)
        self.label_21.setGeometry(QtCore.QRect(520, 10, 54, 12))
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.ZoomLabel = QtGui.QLabel(Form)
        self.ZoomLabel.setGeometry(QtCore.QRect(580, 10, 54, 12))
        self.ZoomLabel.setObjectName(_fromUtf8("ZoomLabel"))
        self.LengthLabel = QtGui.QLabel(Form)
        self.LengthLabel.setGeometry(QtCore.QRect(460, 10, 54, 12))
        self.LengthLabel.setObjectName(_fromUtf8("LengthLabel"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(400, 10, 54, 12))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.InputEdit = QtGui.QLineEdit(Form)
        self.InputEdit.setGeometry(QtCore.QRect(560, 570, 81, 20))
        self.InputEdit.setObjectName(_fromUtf8("InputEdit"))
        self.NewButton = QtGui.QPushButton(Form)
        self.NewButton.setGeometry(QtCore.QRect(10, 0, 75, 23))
        self.NewButton.setObjectName(_fromUtf8("NewButton"))
        self.OpenButton = QtGui.QPushButton(Form)
        self.OpenButton.setGeometry(QtCore.QRect(100, 0, 75, 23))
        self.OpenButton.setObjectName(_fromUtf8("OpenButton"))
        self.SaveButton = QtGui.QPushButton(Form)
        self.SaveButton.setGeometry(QtCore.QRect(190, 0, 75, 23))
        self.SaveButton.setObjectName(_fromUtf8("SaveButton"))
        self.CloseButton = QtGui.QPushButton(Form)
        self.CloseButton.setGeometry(QtCore.QRect(650, 330, 41, 41))
        self.CloseButton.setObjectName(_fromUtf8("CloseButton"))
        self.DeleteButton = QtGui.QPushButton(Form)
        self.DeleteButton.setGeometry(QtCore.QRect(650, 380, 41, 41))
        self.DeleteButton.setObjectName(_fromUtf8("DeleteButton"))
        self.tableWidget = QtGui.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(700, 240, 291, 351))
        self.tableWidget.setMinimumSize(QtCore.QSize(291, 0))
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(80)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.TLengthEdit, self.TWidthEdit)
        Form.setTabOrder(self.TWidthEdit, self.comboBox)
        Form.setTabOrder(self.comboBox, self.MinEdit)
        Form.setTabOrder(self.MinEdit, self.MaxEdit)
        Form.setTabOrder(self.MaxEdit, self.FrictionEdit)
        Form.setTabOrder(self.FrictionEdit, self.LightEdit)
        Form.setTabOrder(self.LightEdit, self.NewButton)
        Form.setTabOrder(self.NewButton, self.OpenButton)
        Form.setTabOrder(self.OpenButton, self.SaveButton)
        Form.setTabOrder(self.SaveButton, self.LineButton)
        Form.setTabOrder(self.LineButton, self.InputEdit)
        Form.setTabOrder(self.InputEdit, self.ArcButton)
        Form.setTabOrder(self.ArcButton, self.CrossButton)
        Form.setTabOrder(self.CrossButton, self.BarrierButton)
        Form.setTabOrder(self.BarrierButton, self.RampButton)
        Form.setTabOrder(self.RampButton, self.RightAngleButton)
        Form.setTabOrder(self.RightAngleButton, self.CloseButton)
        Form.setTabOrder(self.CloseButton, self.DeleteButton)
        Form.setTabOrder(self.DeleteButton, self.tableWidget)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "坐标：", None))
        self.CoordinateLabel.setText(_translate("Form", "（0 ，0）", None))
        self.LineButton.setText(_translate("Form", "直线\n"
"赛道", None))
        self.ArcButton.setText(_translate("Form", "曲线\n"
"弯道", None))
        self.CrossButton.setText(_translate("Form", "十字\n"
"交叉", None))
        self.BarrierButton.setText(_translate("Form", "障碍", None))
        self.label_5.setText(_translate("Form", "赛道元素：", None))
        self.label_13.setText(_translate("Form", "赛道参数：", None))
        self.label_20.setText(_translate("Form", "至", None))
        self.label_17.setText(_translate("Form", "场地总宽度：", None))
        self.label_18.setText(_translate("Form", "场地类型：", None))
        self.label_19.setText(_translate("Form", "电流强度：", None))
        self.label_14.setText(_translate("Form", "摩擦系数：", None))
        self.label_15.setText(_translate("Form", "环境光强：", None))
        self.label_16.setText(_translate("Form", "场地总长度：", None))
        self.comboBox.setItemText(0, _translate("Form", "光电&CCD", None))
        self.comboBox.setItemText(1, _translate("Form", "电磁", None))
        self.label_2.setText(_translate("Form", "状态提示：", None))
        self.RampButton.setText(_translate("Form", "坡道", None))
        self.RightAngleButton.setText(_translate("Form", "直角\n"
"弯道", None))
        self.label_21.setText(_translate("Form", "放大倍数：", None))
        self.ZoomLabel.setText(_translate("Form", "1x", None))
        self.LengthLabel.setText(_translate("Form", "0m", None))
        self.label_3.setText(_translate("Form", "赛道总长：", None))
        self.NewButton.setText(_translate("Form", "New", None))
        self.OpenButton.setText(_translate("Form", "Open", None))
        self.SaveButton.setText(_translate("Form", "Save", None))
        self.CloseButton.setText(_translate("Form", "自动\n"
"封闭", None))
        self.DeleteButton.setText(_translate("Form", "删除\n"
"赛道", None))

