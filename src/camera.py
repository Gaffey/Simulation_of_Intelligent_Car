#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from simulator import *

class Camera(QGraphicsView):
	def __init__(self, scene, parent = None):
		super(Camera, self).__init__(parent)

		self.scene = scene
		self.setScene(self.scene)

	def Initialize(self, simulator):
		image = simulator.view
		""" """

	def reset(self):
		pass