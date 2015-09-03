#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from simulator import *
from PaintEvent import *

class Replay(QGraphicsView):
	moveAnimEnd = pyqtSignal()
	def __init__(self, scene, parent = None):
		super(Replay, self).__init__(parent)

		self.scene = scene
		self.setScene(self.scene)

		self.tracks = []
		self.car = None

		self.last_pos = None
		self.last_toward = None
		self.new_pos = None
		self.new_toward = None
		self.ani = None
		self.aniobj = None
		self.TIME_PER_STEP = 10

	def Initialize(self, simulator):
		tracks = simulator.track.parts
		for track in tracks:
			if isinstance(track, StraightTrack):
				newtrack = LineUnit()
				self.scene.addItem(newtrack)
				self.tracks.appedn(newtrack)
			elif isinstance(track, CurveTrack):
				pass
			"""remaining to be completed"""

		self.car = simulator.car
		'''draw the car'''

	def Play(self, simulator):
		self.last_pos = simulator.car.pos
		self.last_toward = simulator.car.toward
		simulator.step()
		self.new_pos = simulator.car.pos
		self.new_toward = simulator.car.toward
		self.ani = self.animation(self.last_pos, self.last_toward, self.new_pos, self.new_toward)
		self.connect(ani, SIGNAL("finished()"), self.moveAnimEnd)
		self.animation.start()

	def TerminateAni(self):
		if self.ani:
			self.ani.stop()
			self.ani.deleteLater()
			self.ani = None

	def animation(self, pos1, tow1, pos2, tow2):
		ani = QParallelAnimationGroup()
		moveAnim = QPropertyAnimation(self.car, "pos")
		moveAnim.setDuration(self.TIME_PER_STEP * 60)
		moveAnim.setStartValue(QPointF(pos1[0], pos1[1]))
		moveAnim.setEndValue(QPointF(pos2[0], pos2[1]))
		fixAnim = QPropertyAnimation(self.car, "rotation")
		fixAnim.setDuration(self.TIME_PER_STEP * 60)
		fixAnim.setStartValue(0)
		fixAnim.setEndValue(tow2-tow1)
		ani.addAnimation(moveAnim)
		ani.addAnimation(fixAnim)
		return ani


	def resetTracks(self):
		for track in self.tracks:
			self.scene.removeItem(track)
			track.deleteLater()

	def resetCar(self):
		self.scene.removeItem(self.car)
		self.car.deleteLater()

	def reset(self):
		self.resetTracks()
		self.resetCar()
		self.TerminateAni()
		self.tracks = []
		self.car = None

		self.last_pos = None
		self.last_toward = None
		self.new_pos = None
		self.new_toward = None
		self.ani = None
		self.aniobj = None