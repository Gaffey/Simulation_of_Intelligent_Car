#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from ui_cardesign import *
from simulator.racing_car import *
import pickle,sys

REPLAY_FILE_DIR = '.'

class Car(QWidget, Ui_Form):
    def __init__(self, parent = None):
        super(Car, self).__init__(parent)
        self.setupUi(self)
        self.param = {'length':0,'width':0,'dis':0,'weight':0,'fcoff':0,'torque':0,'power':0}
        self.vali = QDoubleValidator(0,1000,3)
        self.LengthEdit.setValidator(self.vali)
        self.WidthEdit.setValidator(self.vali)
        self.DisEdit.setValidator(self.vali)
        self.WeightEdit.setValidator(self.vali)
        self.FcoffEdit.setValidator(self.vali)
        self.TorqueEdit.setValidator(self.vali)
        self.PowerEdit.setValidator(self.vali)

    @pyqtSlot()
    def on_OpenButton_clicked(self):
        fname = unicode(QFileDialog.getOpenFileName(self, QString.fromUtf8("加载赛车文件"), REPLAY_FILE_DIR, "car files(*.car)"))
        if fname:
            try:
                f = open(fname,'rb')
                fileInfo = pickle.load(f)
            except:
                if fname != "":
                    QMessageBox.critical(self, QString.fromUtf8("文件加载错误"), QString.fromUtf8("加载中出现问题,加载失败。"), QMessageBox.Ok, QMessageBox.NoButton)
            else:
                self.param = fileInfo.param
                self.update()

    def update(self):
        self.LengthEdit.setText("%0.3f" %self.param['length'])
        self.WidthEdit.setText("%0.3f" %self.param['width'])
        self.DisEdit.setText("%0.3f" %self.param['dis'])
        self.WeightEdit.setText("%0.3f" %self.param['weight'])
        self.FcoffEdit.setText("%0.3f" %self.param['fcoff'])
        self.TorqueEdit.setText("%0.3f" %self.param['torque'])
        self.PowerEdit.setText("%0.3f" %self.param['power'])

    @pyqtSlot()
    def on_LengthEdit_editingFinished(self):
        self.param['length'] = float(unicode(self.LengthEdit.text()))

    @pyqtSlot()
    def on_WidthEdit_editingFinished(self):
        self.param['width'] = float(unicode(self.WidthEdit.text()))

    @pyqtSlot()
    def on_WeightEdit_editingFinished(self):
        self.param['weight'] = float(unicode(self.WeightEdit.text()))

    @pyqtSlot()
    def on_TorqueEdit_editingFinished(self):
        self.param['torque'] = float(unicode(self.TorqueEdit.text()))

    @pyqtSlot()
    def on_FcoffEdit_editingFinished(self):
        self.param['fcoff'] = float(unicode(self.FcoffEdit.text()))

    @pyqtSlot()
    def on_DisEdit_editingFinished(self):
        self.param['dis'] = float(unicode(self.DisEdit.text()))

    @pyqtSlot()
    def on_PowerEdit_editingFinished(self):
        self.param['power'] = float(unicode(self.PowerEdit.text()))

    @pyqtSlot()
    def on_SaveButton_clicked(self):
        fname = unicode(QFileDialog.getSaveFileName(self, QString.fromUtf8("储存赛车文件"), REPLAY_FILE_DIR, "car files(*.car)"))
        print fname
        f = open(fname,'wb')
        savefile = RacingCar(self.param)
        if f:
            try:
                pickle.dump(savefile,f)
            except:
                if fname != "":
                    QMessageBox.critical(self, QString.fromUtf8("文件储存错误"), QString.fromUtf8("储存中出现问题,加载失败。"), QMessageBox.Ok, QMessageBox.NoButton)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Car()
    form.show()
    app.exec_()
