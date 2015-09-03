#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from ui_simulator import *
from simulator import *
from replayer import *
from camera import *
import sys, pickle

REPLAY_FILE_DIR = '.'

class Simulation(QWidget, Ui_Form):
    def __init__(self, parent = None):
        super(Simulation, self).__init__(parent)
        self.setupUi(self)
        self.car = None
        self.track = None
        self.ai = None
        self.initial_pos = True
        self.start = False
        self.simulator = None
        self.step = 10
        self.pause = False
        self.simu_info = []
        self.StepEdit.setValidator(QIntValidator(5,200))
        self.scene1 = QGraphicsScene()
        self.scene2 = QGraphicsScene()
        self.CenterWidget = Replay(self.scene1)
        self.CenterLayout.addWidget(self.CenterWidget)
        self.Camera = Camera(self.scene2)
        self.CameraLayout.addWidget(self.Camera)
        self.update()

    def update(self):
        if not self.car or not self.track or not self.ai:
            self.StartButton.setEnabled(False)
            self.PauseButton.setEnabled(False)
            self.ResetButton.setEnabled(False)
            self.SaveButton.setEnabled(False)
        elif not self.start:
            self.StartButton.setEnabled(True)
        if not self.initial_pos:
            self.ResetButton.setEnabled(True)
            self.SaveButton.setEnabled(True)
        else:
            self.ResetButton.setEnabled(False)
            self.SaveButton.setEnabled(False)
        if self.start and not self.pause:
            self.PauseButton.setEnabled(True)
            self.LoadAIButton.setEnabled(False)
            self.LoadCarButton.setEnabled(False)
            self.LoadTrackButton.setEnabled(False)
        else:
            self.PauseButton.setEnabled(False)
            self.LoadAIButton.setEnabled(True)
            self.LoadCarButton.setEnabled(True)
            self.LoadTrackButton.setEnabled(True)
        if self.start:
            self.StepEdit.setEnabled(False)
        else:
            self.StepEdit.setEnabled(True)

    @pyqtSlot()
    def on_StepEdit_editingFinished(self):
        self.step = int(unicode(self.StepEdit.text()))

    @pyqtSlot()
    def on_StartButton_clicked(self):
        self.start = True
        if not self.pause:
            self.simulator = Simulator(self.step, self.track, self.car, self.ai)
            self.info_initialize()
            self.CenterWidget.Initialize(self.simulator)
            self.CenterWidget.Play(self.simulator)
            self.CameraWidget.Initialize(self.simulator)
            self.update()
        else:
            self.info_initialize()
            self.CenterWidget.Play(self.simulator)
            self.pause = False
            self.update()

    @pyqtSlot()
    def on_PauseButton_clicked(self):
        self.pause = True
        self.update()

    @pyqtSlot()
    def on_ResetButton_clicked(self):
        self.start = False
        self.pause = True
        self.simulator = simulator.Simulator(self.step, self.track, self.car, self.ai)
        self.info_initialize()
        self.CenterWidget.Initialize(self.simulator)
        self.update()

    @pyqtSlot()
    def on_SaveButton_clicked(self):
        fname = unicode(QFileDialog.getSaveFileName(self, QString.fromUtf8("储存数据文件"), REPLAY_FILE_DIR, "data files(*.data)"))
        f = open(fname,'wb')
        if f:
            try:
                pickle.dump(self.simu_info,f)
            except:
                if fname != "":
                    QMessageBox.critical(self, QString.fromUtf8("文件储存错误"), QString.fromUtf8("储存中出现问题,加载失败。"), QMessageBox.Ok, QMessageBox.NoButton)

    @pyqtSlot()
    def on_LoadCarButton_clicked(self):
        fname = unicode(QFileDialog.getOpenFileName(self, QString.fromUtf8("加载赛车文件"), REPLAY_FILE_DIR, "car files(*.car)"))
        if fname:
            try:
                f = open(fname,'rb')
                fileInfo = pickle.load(f)
            except:
                if fname != "":
                    QMessageBox.critical(self, QString.fromUtf8("文件加载错误"), QString.fromUtf8("加载中出现问题,加载失败。"), QMessageBox.Ok, QMessageBox.NoButton)
            else:
                self.car = fileInfo
                self.start = False
                self.pause = False
                if self.CenterWidget.car and self.CenterWidget.tracks:
                    self.resetUI()
                self.update()

    @pyqtSlot()
    def on_LoadTrackButton_clicked(self):
        fname = unicode(QFileDialog.getOpenFileName(self, QString.fromUtf8("加载赛道文件"), REPLAY_FILE_DIR, "track files(*.tk)"))
        if fname:
            try:
                f = open(fname,'rb')
                fileInfo = pickle.load(f)
            except:
                if fname != "":
                    QMessageBox.critical(self, QString.fromUtf8("文件加载错误"), QString.fromUtf8("加载中出现问题,加载失败。"), QMessageBox.Ok, QMessageBox.NoButton)
            else:
                self.track = fileInfo
                self.start = False
                self.pause = False
                if self.CenterWidget.car and self.CenterWidget.tracks:
                    self.resetUI()
                self.update()

    @pyqtSlot()
    def on_LoadAIButton_clicked(self):
        fname = unicode(QFileDialog.getOpenFileName(self, QString.fromUtf8("加载ai文件"), REPLAY_FILE_DIR, "ai files(*.exe)"))
        if fname:
            '''
            ###remaining to be completed###
            try:
                f = open(fname,'rb')
                fileInfo = pickle.load(f)
            except:
                if fname != "":
                    QMessageBox.critical(self, QString.fromUtf8("文件加载错误"), QString.fromUtf8("加载中出现问题,加载失败。"), QMessageBox.Ok, QMessageBox.NoButton)
            else:
                self.track = fileInfo
            '''

    def info_initialize(self):
        newinfo = (self.simulator.time, self.car.pos, self.car.speed, self.car.acce, self.simulator.off_center)
        self.simu_info.append(newinfo)
        self.CoordinateEdit.setText("(%d, %d)" %(newinfo[1][0], newinfo[1][1]))
        self.SpeedEdit.setText("%d" %newinfo[2])
        self.AccelerateEdit.setText("%0.3f" %newinfo[3])
        self.TimeEdit.setText("%d" %newinfo[0])
        self.OffsetEdit.setText("%d" %newinfo[4])

    def on_animEnd(self):
        self.CenterWidget.TerminateAni()
        if self.isPaused:
            return
        self.CenterWidget.Play(self.simulator)
        self.info_initialize()
        self.CameraWidget.Initialize(self.simulator)

    def resetUI(self):
        self.CoordinateEdit.setText("")
        self.SpeedEdit.setText("")
        self.AccelerateEdit.setText("")
        self.TimeEdit.setText("")
        self.OffsetEdit.setText("")
        self.CenterWidget.reset()
        self.CameraWidget.reset()
        self.simu_info = []

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Simulation()
    form.show()
    app.exec_()