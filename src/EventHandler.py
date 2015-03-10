#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *
import math

def getDis(point1, point2):
	return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

class PathView(QGraphicsView):
	ChooseBegin = pyqtSignal()
	ChooseEnd = pyqtSignal()
	ChooseR = pyqtSignal()
	ChooseWidth = pyqtSignal()
	ChooseSide = pyqtSignal()
	Coordinate = pyqtSignal()
	zoomed = pyqtSignal()
	def __init__(self, scene, parent = None):
		super(PathView, self).__init__(parent)
		self.scene = scene
		self.setScene(self.scene)
		self.started = False
		self.PointList = []
		self.painter = QPainter()
		self.toolId = 0
		self.stateId = 0
		self.dragPos = None
		self.BarrierPos = None
		self.zoom = 1

	def mouseMoveEvent(self, event):
		if not self.started:
			QGraphicsView.mouseMoveEvent(self, event)
			return

		pos = event.pos()
		self.emit(SIGNAL("Coordinate"), pos)
		if self.dragPos:
			self.translate(pos.x() - self.dragPos.x(), pos.y() - self.dragPos.y())
			self.dragPos = pos
			return
		minDis = 5
		BigPoint = None
		for point in self.PointList:
			dis = getDis(point, pos)
			if dis < minDis:
				minDis = dis
				BigPoint = point
		if BigPoint:
			self.emit(SIGNAL("Coordinate"), BigPoint)

	def mousePressEvent(self, event):
		if not self.started:
			QGraphicsView.mousePressEvent(self, event)
			return

		if self.toolId in [0,1,2]:
			if self.toolId == 0:
				self.dragPos = event.pos()
			return

		pos = event.pos()

		if self.stateId == 0:
			self.emit(SIGNAL("ChooseBegin"), pos)
			self.stateId = 1

		elif self.stateId == 1:
			self.emit(SIGNAL("ChooseEnd"), pos)
			self.stateId = 2

		elif self.stateId == 2:
			self.emit(SIGNAL("ChooseWidth"), pos)
			if self.toolId == 3:
				self.stateId = 0
			elif self.toolId in [4,5,6]:
				self.stateId = 3

	def mouseReleaseEvent(self, event):
		if not self.started:
			QGraphicsView.mouseReleaseEvent(self, event)
			return

		if self.dragPos:
			self.dragPos = None

	def wheelEvent(self, event):
		if self.started:
		    factor = 1.414213562373 ** (event.delta() / 240.0)
		    self.scale(factor, factor)
		    self.zoom *= factor
		    self.emit(SIGNAL("zoomed"), self.zoom)

