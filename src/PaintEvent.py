#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *
import math

PI = 3.1415926535898

class LineUnit(QGraphicsObject):
	def __init__(self, x1, y1, width1, width2, direction, x2 = None, y2 = None, length = None, theta = None, line1 = None, line2 = None, parent = None):
		super(LineUnit, self).__init__(parent)
		self.x1 = x1
		self.y1 = y1
		self.direction = direction
		print self.x1, self.y1
		if x2 and y2:
			self.x2 = x2
			self.y2 = y2
			self.theta = theta = math.atan2(self.y2 - self.y1, self.x2 - self.x1)
		else:
			self.length = length
			self.theta = theta
			print "direction:",theta, direction
			self.x2 = self.x1 + abs(math.cos(theta)) * self.length * direction[0]
			self.y2 = self.y1 + abs(math.sin(theta)) * self.length * direction[1]
		self.width1 = width1
		self.width2 = width2
		self.x_lu = self.x1 - math.sin(theta) * self.width1/2
		self.y_lu = self.y1 + math.cos(theta) * self.width1/2
		self.x_ru = self.x2 - math.sin(theta) * self.width1/2
		self.y_ru = self.y2 + math.cos(theta) * self.width1/2
		self.x_ld = self.x1 + math.sin(theta) * self.width1/2
		self.y_ld = self.y1 - math.cos(theta) * self.width1/2
		self.x_rd = self.x2 + math.sin(theta) * self.width1/2
		self.y_rd = self.y2 - math.cos(theta) * self.width1/2
		print self.x_lu, self.y_lu, self.x_ld, self.y_ld, self.x_ru, self.y_ru, self.x_rd, self.y_rd
		if line1:
			self.x3 = self.x1 + abs(math.cos(theta)) * line1 * direction[0]
			self.y3 = self.y1 + abs(math.sin(theta)) * line1 * direction[1]
			self.x4 = self.x3 + abs(math.cos(theta)) * line2 * direction[0]
			self.y4 = self.y3 + abs(math.sin(theta)) * line2 * direction[1]
			self.x_ru1 = self.x3 - math.sin(theta) * self.width1/2
			self.y_ru1 = self.y3 + math.cos(theta) * self.width1/2
			self.x_rd1 = self.x3 + math.sin(theta) * self.width1/2
			self.y_rd1 = self.y3 - math.cos(theta) * self.width1/2
			self.x_ru2 = self.x4 - math.sin(theta) * self.width1/2
			self.y_ru2 = self.y4 + math.cos(theta) * self.width1/2
			self.x_rd2 = self.x4 + math.sin(theta) * self.width1/2
			self.y_rd2 = self.y4 - math.cos(theta) * self.width1/2
	def getInLine(self):
		return [(self.x_lu, self.y_lu), (self.x_ld, self.y_ld)]

	def getOutLine(self):
		return [(self.x_ru, self.y_ru), (self.x_rd, self.y_rd)]

	def getMid1(self):
		return [(self.x_ru1, self.y_ru1), (self.x_rd1, self.y_rd1)]

	def getMid2(self):
		return [(self.x_ru2, self.y_ru2), (self.x_rd2, self.y_rd2)]

	def boundingRect(self):
		cor = self.mapFromScene(QPointF(0, 0))
		return QRectF(cor.x(),cor.y(),cor.x()+1000,cor.y()+1000)

	def getSlope(self):
		return math.atan2((self.y2 - self.y1),(self.x2 - self.x1))

	def getBeginPoint(self):
		return [((self.x_ru + self.x_rd)/2, (self.y_ru + self.y_rd)/2)]

	def getDirection(self):
		print "return direction:", 1 if self.x2 > self.x1 or self.x1 == self.x2 and self.y2 > self.y1 else -1
		return [1 if self.x2 > self.x1 else -1,  1 if self.y2 > self.y1 else -1]

	def paint(self, painter, option, widget = None):
		painter.save()
		pen = QPen()
		pen.setWidth(self.width2)
		pen.setCapStyle(Qt.RoundCap)
		pen.setJoinStyle(Qt.RoundJoin)
		pen.setColor(QColor(0, 0, 0))
		painter.setPen(pen)
		painter.drawLine(QPointF(self.x_lu, self.y_lu), QPointF(self.x_ru, self.y_ru))
		painter.drawLine(QPointF(self.x_ld, self.y_ld), QPointF(self.x_rd, self.y_rd))
		painter.restore()

class CenterLineUnit(QGraphicsObject):
	def __init__(self, x1, y1, width2, direction, x2 = None, y2 = None, theta = None, length = None, parent = None):
		super(CenterLineUnit, self).__init__(parent)
		self.x1 = x1
		self.y1 = y1
		self.direction = direction
		if x2 and y2:
			self.x2 = x2
			self.y2 = y2
			self.theta = math.atan2(self.y2 - self.y1, self.x2 - self.x1)
		else:
			self.length = length
			self.theta = theta
			self.x2 = self.x1 + abs(math.cos(theta)) * self.length * direction[0]
			self.y2 = self.y1 + abs(math.sin(theta)) * self.length * direction[1]
		self.width2 = width2

	def boundingRect(self):
		cor = self.mapFromScene(QPointF(0, 0))
		return QRectF(cor.x(),cor.y(),cor.x()+1000,cor.y()+1000)

	def getSlope(self):
		return math.atan2(float(self.y2 - self.y1),float(self.x2 - self.x1))

	def getBeginPoint(self):
		return [(self.x2, self.y2)]

	def getDirection(self):
		return [1 if self.x2 > self.x1 else -1, 1 if self.y2 > self.y1 else -1]

	def paint(self, painter, option, widget = None):
		painter.save()
		pen = QPen()
		pen.setWidth(self.width2)
		pen.setCapStyle(Qt.RoundCap)
		pen.setJoinStyle(Qt.RoundJoin)
		pen.setColor(QColor(0, 0, 0))
		painter.setPen(pen)
		painter.drawLine(QPointF(self.x1, self.y1), QPointF(self.x2, self.y2))
		painter.restore()

class ArcUnit(QGraphicsObject):
	def __init__(self, x1, y1, arc, radius, theta, width1, width2, direction, parent = None):
		super(ArcUnit, self).__init__(parent)
		self.x1 = x1
		self.y1 = y1
		self.arc = arc
		print "I get direction:",direction, " and theta = ", theta
		self.width1 = width1
		self.width2 = width2
		self.radius = radius
		self.direction = direction
		self.theta = theta
		if arc < 0:
			self.x_c = self.x1 - abs(math.sin(self.theta)) * (self.radius) * direction[1]
			self.y_c = self.y1 + abs(math.cos(self.theta)) * (self.radius) * direction[0]
			if abs(self.theta - PI/2) < 0.05 or abs(self.theta + PI/2) < 0.05:
				if self.x_c > self.x1:
					self.start = -180*16
				else:
					self.start = 0
			elif direction[0] == 1 and direction[1] == 1:
				self.start = float(- self.theta + PI/2)*180.0*16.0/PI
			elif direction[0] == 1 and direction[1] == -1:
				self.start = float(- self.theta + PI/2)*180.0*16.0/PI
			elif direction[1] == 1 and direction[0] == -1:
				self.start = float(- self.theta - PI/2)*180.0*16.0/PI
			else:
				self.start = float(- PI/2 - self.theta)*180.0*16.0/PI
			self.span = arc*16
			self.x2 = self.x_c + self.radius * math.cos(-(float(self.start)/16.0*PI/180.0 + float(self.span)/16.0*PI/180.0))
			self.y2 = self.y_c + self.radius * math.sin(-(float(self.start)/16.0*PI/180.0 + float(self.span)/16.0*PI/180.0))
			
		else:
			print self.theta
			self.x_c = self.x1 + abs(math.sin(self.theta)) * (self.radius) * direction[1]
			self.y_c = self.y1 - abs(math.cos(self.theta)) * (self.radius) * direction[0]
			print math.sin(self.theta) * (self.radius)
			if abs(self.theta - PI/2) < 0.05:
				if self.x_c > self.x1:
					self.start = -180*16
				else:
					self.start = 0
			elif direction[0] == 1 and direction[1] == 1:
				self.start = float(- self.theta - PI/2)*180.0*16.0/PI
			elif direction[0] == 1 and direction[1] == -1:
				self.start = float(- self.theta - PI/2)*180.0*16.0/PI
			elif direction[1] == 1 and direction[0] == -1:
				self.start = float(- self.theta + PI/2)*180.0*16.0/PI
			else:
				self.start = float(PI/2 - self.theta)*180.0*16.0/PI
			self.span = arc*16
			self.x2 = self.x_c + self.radius * math.cos(-(float(self.start)/16.0*PI/180.0 + float(self.span)/16.0*PI/180.0))
			self.y2 = self.y_c + self.radius * math.sin(-(float(self.start)/16.0*PI/180.0 + float(self.span)/16.0*PI/180.0))

	def getSlope(self):
		#slope = -(self.theta + float(self.arc)*PI/180.0)
		slope = -(float(self.start)/16.0 + float(self.span)/16.0 + 90)/180*PI
		print "count slope:",self.start/16.0, " ", self.span/16.0, " ", slope
		while slope > PI/2:
			slope -= PI
		while slope <= -PI/2:
			slope += PI
		return slope

	def getBeginPoint(self):
		return [(self.x2, self.y2)]

	def getDirection(self):
		angle = (self.start/16 + self.span/16)%360
		print "return angle:", self.start, self.span, angle, int(angle) in range(0, 90), self.span < 0
		if int(angle) in range(0, 90) and self.span > 0 or int(angle) in range(180, 270) and self.span < 0:
			return [-1, -1]
		elif int(angle) in range(90, 180) and self.span > 0 or int(angle) in range(270, 360) and self.span < 0: 
			return [-1, 1]
		elif int(angle) in range(180, 270) and self.span > 0 or int(angle) in range(0, 90) and self.span < 0:
			return [1, 1]
		else:
			return [1, -1]

	def boundingRect(self):
		cor = self.mapFromScene(QPointF(0, 0))
		return QRectF(cor.x(),cor.y(),cor.x()+1000,cor.y()+1000)

	def paint(self, painter, option, widget = None):
		painter.save()
		pen = QPen()
		pen.setWidth(self.width2)
		pen.setCapStyle(Qt.RoundCap)
		pen.setJoinStyle(Qt.RoundJoin)
		pen.setColor(QColor(0, 0, 0))
		painter.setPen(pen)
		painter.drawArc(QRectF(self.x_c - self.radius - self.width1/2, self.y_c - self.radius - self.width1/2, 2*(self.radius + self.width1/2), 2*(self.radius + self.width1/2)), self.start, self.span)
		painter.drawArc(QRectF(self.x_c - self.radius + self.width1/2, self.y_c - self.radius + self.width1/2, 2*(self.radius - self.width1/2), 2*(self.radius - self.width1/2)), self.start, self.span)
		painter.restore()

class CenterArcUnit(QGraphicsObject):
	def __init__(self, x1, y1, arc, radius, theta, width, direction, parent = None):
		super(CenterArcUnit, self).__init__(parent)
		self.x1 = x1
		self.y1 = y1
		self.arc = arc
		self.width = width
		self.radius = radius
		self.theta = theta
		self.width2 = width
		self.direction = direction
		if arc < 0:
			self.x_c = self.x1 - abs(math.sin(self.theta)) * (self.radius) * direction[1]
			self.y_c = self.y1 + abs(math.cos(self.theta)) * (self.radius) * direction[0]
			if abs(self.theta - PI/2) < 0.05 or abs(sel.theta + PI/2) < 0.05:
				if self.x_c > self.x1:
					self.start = -180*16
				else:
					self.start = 0
			elif direction[0] == 1 and direction[1] == 1:
				self.start = float(- self.theta + PI/2)*180.0*16.0/PI
			elif direction[0] == 1 and direction[1] == -1:
				self.start = float(- self.theta + PI/2)*180.0*16.0/PI
			elif direction[1] == 1 and direction[0] == -1:
				self.start = float(- self.theta - PI/2)*180.0*16.0/PI
			else:
				self.start = float(- PI/2 - self.theta)*180.0*16.0/PI
			self.span = arc*16
			self.x2 = self.x_c + self.radius * math.cos(-(float(self.start)/16.0*PI/180.0 + float(self.span)/16.0*PI/180.0))
			self.y2 = self.y_c + self.radius * math.sin(-(float(self.start)/16.0*PI/180.0 + float(self.span)/16.0*PI/180.0))
			
		else:
			print self.theta
			self.x_c = self.x1 + abs(math.sin(self.theta)) * (self.radius) * direction[1]
			self.y_c = self.y1 - abs(math.cos(self.theta)) * (self.radius) * direction[0]
			print math.sin(self.theta) * (self.radius)
			if abs(self.theta - PI/2) < 0.05:
				if self.x_c > self.x1:
					self.start = -180*16
				else:
					self.start = 0
			elif direction[0] == 1 and direction[1] == 1:
				self.start = float(- self.theta - PI/2)*180.0*16.0/PI
			elif direction[0] == 1 and direction[1] == -1:
				self.start = float(- self.theta - PI/2)*180.0*16.0/PI
			elif direction[1] == 1 and direction[0] == -1:
				self.start = float(- self.theta + PI/2)*180.0*16.0/PI
			else:
				self.start = float(PI/2 - self.theta)*180.0*16.0/PI
			self.span = arc*16
			self.x2 = self.x_c + self.radius * math.cos(-(float(self.start)/16.0*PI/180.0 + float(self.span)/16.0*PI/180.0))
			self.y2 = self.y_c + self.radius * math.sin(-(float(self.start)/16.0*PI/180.0 + float(self.span)/16.0*PI/180.0))

	def getSlope(self):
		#slope = -(self.theta + float(self.arc)*PI/180.0)
		slope = -(float(self.start)/16.0 + float(self.span)/16.0 + 90)/180*PI
		print "count slope:",self.start/16.0, " ", self.span/16.0, " ", slope
		while slope > PI/2:
			slope -= PI
		while slope <= -PI/2:
			slope += PI
		return slope

	def getBeginPoint(self):
		return [(self.x2, self.y2)]

	def getDirection(self):
		angle = (self.start/16 + self.span/16)%360
		print "return angle:", self.start, self.span, angle, int(angle) in range(0, 90), self.span < 0
		if int(angle) in range(0, 90) and self.span > 0 or int(angle) in range(180, 270) and self.span < 0:
			return [-1, -1]
		elif int(angle) in range(90, 180) and self.span > 0 or int(angle) in range(270, 360) and self.span < 0: 
			return [-1, 1]
		elif int(angle) in range(180, 270) and self.span > 0 or int(angle) in range(0, 90) and self.span < 0:
			return [1, 1]
		else:
			return [1, -1]

	def boundingRect(self):
		cor = self.mapFromScene(QPointF(0, 0))
		return QRectF(cor.x(),cor.y(),cor.x()+1000,cor.y()+1000)

	def paint(self, painter, option, widget = None):
		painter.save()
		pen = QPen()
		pen.setWidth(self.width2)
		pen.setCapStyle(Qt.RoundCap)
		pen.setJoinStyle(Qt.RoundJoin)
		pen.setColor(QColor(0, 0, 0))
		painter.setPen(pen)
		painter.drawArc(QRectF(self.x_c - self.radius, self.y_c - self.radius, 2*(self.radius), 2*(self.radius)), self.start, self.span)
		painter.restore()

class AngleUnit(QGraphicsObject):
	def __init__(self, x1, y1, width1, width2, theta, direction, side, angle, parent = None):
		super(AngleUnit, self).__init__(parent)
		self.x1 = x1
		self.y1 = y1
		self.width1 = width1
		self.width2 = width2
		self.theta = theta
		self.direction = direction
		print self.direction
		self.side = side
		self.angle = angle
		if theta > 0:
			self.x_ld = self.x1 + (math.sin(theta)) * self.width1/2 * self.direction[1]
			self.y_ld = self.y1 - (math.cos(theta)) * self.width1/2 * self.direction[1]
			self.x_lu = self.x1 - (math.sin(theta)) * self.width1/2 * self.direction[1]
			self.y_lu = self.y1 + (math.cos(theta)) * self.width1/2 * self.direction[1]
		else:
			self.x_ld = self.x1 - (math.sin(theta)) * self.width1/2 * self.direction[1]
			self.y_ld = self.y1 + (math.cos(theta)) * self.width1/2 * self.direction[1]
			self.x_lu = self.x1 + (math.sin(theta)) * self.width1/2 * self.direction[1]
			self.y_lu = self.y1 - (math.cos(theta)) * self.width1/2 * self.direction[1]
		'''
		self.x_lu = self.x1 - math.sin(theta) * self.width1/2 * direction[1]
		self.y_lu = self.y1 + math.cos(theta) * self.width1/2 * direction[0]
		#self.x_ru = self.x2 - math.sin(theta) * self.width1/2
		#self.y_ru = self.y2 + math.cos(theta) * self.width1/2
		self.x_ld = self.x1 + math.sin(theta) * self.width1/2 * direction[1]
		self.y_ld = self.y1 - math.cos(theta) * self.width1/2 * direction[0]
		#self.x_rd = self.x2 + math.sin(theta) * self.width1/2
		#self.y_rd = self.y2 - math.cos(theta) * self.width1/2
		'''
		angle_length = self.width1 * math.tan((PI - angle*PI/180.0)/2.0)
		if self.side:
			self.xm = self.x_lu + abs(math.cos(theta)) * angle_length * direction[0]
			self.ym = self.y_lu + abs(math.sin(theta)) * angle_length * direction[1]
			self.new_theta = self.theta + angle*PI/180
			while self.new_theta > PI/2.0:
				self.new_theta -= PI
			while self.new_theta <= -PI/2.0:
				self.new_theta += PI
			print "new_theta = ", self.new_theta
			self.compare_1_x = (self.x_ld + self.xm)/2.0
			self.compare_1_y = (self.y_ld + self.ym)/2.0
		else:
			self.xm = self.x_ld + abs(math.cos(theta)) * angle_length * direction[0]
			self.ym = self.y_ld + abs(math.sin(theta)) * angle_length * direction[1]
			self.new_theta = self.theta - angle*PI/180
			while self.new_theta > PI/2.0:
				self.new_theta -= PI
			while self.new_theta <= -PI/2.0:
				self.new_theta += PI
			print "new_theta = ", self.new_theta
			self.compare_1_x = (self.x_lu + self.xm)/2.0
			self.compare_1_y = (self.y_lu + self.ym)/2.0
		'''
		if direction[0] == 1:
			tmp_theta = theta
		else:
			if abs(theta) != 0:
				tmp_theta = theta - theta/abs(theta) * PI
			else:
				tmp_theta = PI
		new_tmp_theta = - tmp_theta + angle * PI / 180 * 2 * (side - 0.5)
		while new_tmp_theta > PI:
			new_tmp_theta -= 2 * PI
		while new_tmp_theta < -PI:
			new_tmp_theta += 2 * PI
		'''
		if side:
			if abs(theta) <= 0.05:
				new_direct = [direction[0], -direction[0]]
			elif abs(theta - PI/2) <= 0.05 or abs(theta + PI/2) < 0.05:
				if direction[1] == -1:
					new_direct = [-1, -1]
				else:
					new_direct = [1, 1]
			elif direction[0] == direction[1]:
				if abs(self.theta) + angle > PI:
					new_direct = direction
				else:
					new_direct = [direction[0], -direction[1]]
			else:
				if PI/2.0 + self.theta + angle > PI:
					new_direct = direction
				else:
					new_direct = [-direction[0], direction[1]]
		else:
			if abs(theta) <= 0.05:
				new_direct = [direction[0], direction[0]]
			elif abs(theta - PI/2) <= 0.05 or abs(theta + PI/2) < 0.05:
				if direction[1] == -1:
					new_direct = [1, -1]
				else:
					new_direct = [-1, 1]
			elif direction[0] == direction[1]:
				if PI/2.0 - abs(self.theta) + angle > PI:
					new_direct = direction
				else:
					new_direct = [-direction[0], direction[1]]
			else:
				if - self.theta + angle > PI:
					new_direct = direction
				else:
					new_direct = [direction[0], -direction[1]]
		print "new_direct:",new_direct
		self.xe = self.xm + abs(math.cos(self.new_theta)) * angle_length * new_direct[0]
		self.ye = self.ym + abs(math.sin(self.new_theta)) * angle_length * new_direct[1]
		print "m:(",self.xm,self.ym,") e:(",self.xe,self.ye,")"
		if self.side:
			self.compare_2_x = (self.x_ld + self.xe)/2.0
			self.compare_2_y = (self.y_ld + self.ye)/2.0
		else:
			self.compare_2_x = (self.x_lu + self.xe)/2.0
			self.compare_2_y = (self.y_lu + self.ye)/2.0
		print "bg pt:(",self.compare_2_x,self.compare_2_y,")"

	def getSlope(self):
		return math.atan2(self.compare_2_y - self.compare_1_y, self.compare_2_x - self.compare_1_x)

	def getBeginPoint(self):
		return[(self.compare_2_x, self.compare_2_y)]

	def getDirection(self):
		return [1 if self.compare_2_x > self.compare_1_x else -1, 1 if self.compare_2_y > self.compare_1_y else -1]

	def boundingRect(self):
		cor = self.mapFromScene(QPointF(0, 0))
		return QRectF(cor.x(),cor.y(),cor.x()+1000,cor.y()+1000)

	def paint(self, painter, option, widget = None):
		painter.save()
		pen = QPen()
		pen.setWidth(self.width2)
		pen.setCapStyle(Qt.RoundCap)
		pen.setJoinStyle(Qt.RoundJoin)
		pen.setColor(QColor(0, 0, 0))
		painter.setPen(pen)
		if not self.side:
			painter.drawLine(QPointF(self.x_ld, self.y_ld), QPointF(self.xm, self.ym))
		else:
			painter.drawLine(QPointF(self.x_lu, self.y_lu), QPointF(self.xm, self.ym))
		painter.drawLine(QPointF(self.xm, self.ym), QPointF(self.xe, self.ye))
		painter.restore()


class RightAngleUnit(QGraphicsObject):
	def __init__(self, x1, y1, width1, width2, theta, direction, side, parent = None):
		super(RightAngleUnit, self).__init__(parent)
		self.x1 = x1
		self.y1 = y1
		self.theta = theta
		self.direction = direction
		self.side = side
		self.width1 = width1
		self.width2 = width2
		print "get message:",self.theta, direction, side, width1, width2, x1, y1
		if theta > 0:
			self.x_lu = self.x1 + (math.sin(theta)) * self.width1/2 * self.direction[1]
			self.y_lu = self.y1 - (math.cos(theta)) * self.width1/2 * self.direction[1]
			self.x_ld = self.x1 - (math.sin(theta)) * self.width1/2 * self.direction[1]
			self.y_ld = self.y1 + (math.cos(theta)) * self.width1/2 * self.direction[1]
		else:
			self.x_lu = self.x1 - (math.sin(theta)) * self.width1/2 * self.direction[1]
			self.y_lu = self.y1 + (math.cos(theta)) * self.width1/2 * self.direction[1]
			self.x_ld = self.x1 + (math.sin(theta)) * self.width1/2 * self.direction[1]
			self.y_ld = self.y1 - (math.cos(theta)) * self.width1/2 * self.direction[1]
		print "count start point: ",self.x_lu, self.y_lu, self.x_ld, self.y_ld
		if self.side and self.direction == [1,1] or not self.side and self.direction == [-1,-1]:
			self.new_direct = new_direct = [1,-1]
		elif self.side and self.direction == [-1,1] or not self.side and self.direction == [1,-1]:
			self.new_direct = new_direct = [1,1]
		elif self.side and self.direction == [-1,-1] or not self.side and self.direction == [1,1]:
			self.new_direct = new_direct = [-1,1]
		else:
			self.new_direct = new_direct = [-1,-1]
		if not self.side:
			self.x_mu = self.x_lu + (110 + self.width1) * abs(math.cos(theta)) * direction[0]
			self.y_mu = self.y_lu + (110 + self.width1) * abs(math.sin(theta)) * direction[1]
			self.x_md = self.x_ld + 110 * abs(math.cos(theta)) * direction[0]
			self.y_md = self.y_ld + 110 * abs(math.sin(theta)) * direction[1]
			self.x_u = self.x_lu + 10 * abs(math.cos(theta)) * direction[0]
			self.y_u = self.y_lu + 10 * abs(math.sin(theta)) * direction[1]
		else:
			self.x_mu = self.x_lu + 110 * abs(math.cos(theta)) * direction[0]
			self.y_mu = self.y_lu + 110 * abs(math.sin(theta)) * direction[1]
			self.x_md = self.x_ld + (110 + self.width1) * abs(math.cos(theta)) * direction[0]
			self.y_md = self.y_ld + (110 + self.width1) * abs(math.sin(theta)) * direction[1]
			self.x_u = self.x_lu + 10 * abs(math.cos(theta)) * direction[0]
			self.y_u = self.y_lu + 10 * abs(math.sin(theta)) * direction[1]
		if theta > 0:
			theta_ = theta - PI/2
		else:
			theta_ = theta + PI/2
		if not self.side:
			self.x_ru = self.x_mu + (110 + self.width1) * abs(math.cos(theta_)) * new_direct[0]
			self.y_ru = self.y_mu + (110 + self.width1) * abs(math.sin(theta_)) * new_direct[1]
			self.x_rd = self.x_md + 110 * abs(math.cos(theta_)) * new_direct[0]
			self.y_rd = self.y_md + 110 * abs(math.sin(theta_)) * new_direct[1]
			self.x_d = self.x_rd - 10 * abs(math.cos(theta_)) * new_direct[0]
			self.y_d = self.y_rd - 10 * abs(math.sin(theta_)) * new_direct[1]
		else:
			self.x_ru = self.x_mu + 110 * abs(math.cos(theta_)) * new_direct[0]
			self.y_ru = self.y_mu + 110 * abs(math.sin(theta_)) * new_direct[1]
			self.x_rd = self.x_md + (110 + self.width1) * abs(math.cos(theta_)) * new_direct[0]
			self.y_rd = self.y_md + (110 + self.width1) * abs(math.sin(theta_)) * new_direct[1]
			self.x_d = self.x_rd - 10 * abs(math.cos(theta_)) * new_direct[0]
			self.y_d = self.y_rd - 10 * abs(math.sin(theta_)) * new_direct[1]

	def getDirection(self):
		return self.new_direct

	def getSlope(self):
		if self.theta + PI/2 > PI/2:
			self.theta -= PI
		elif self.theta + PI/2 <= -PI/2:
			self.theta += PI
		return PI/2 + self.theta

	def getPos(self):
		return [(self.x_u, self.y_u), (self.x_d, self.y_d)]

	def getBeginPoint(self):
		return [(float(self.x_ru + self.x_rd)/2.0, float(self.y_ru + self.y_rd)/2.0)]

	def boundingRect(self):
		cor = self.mapFromScene(QPointF(0, 0))
		return QRectF(cor.x(),cor.y(),cor.x()+1000,cor.y()+1000)

	def paint(self, painter, option, widget = None):
		painter.save()
		pen = QPen()
		pen.setWidth(self.width2)
		pen.setCapStyle(Qt.RoundCap)
		pen.setJoinStyle(Qt.RoundJoin)
		pen.setColor(QColor(0, 0, 0))
		painter.setPen(pen)
		painter.drawLine(QPointF(self.x_lu, self.y_lu), QPointF(self.x_mu, self.y_mu))
		painter.drawLine(QPointF(self.x_ld, self.y_ld), QPointF(self.x_md, self.y_md))
		painter.drawLine(QPointF(self.x_mu, self.y_mu), QPointF(self.x_ru, self.y_ru))
		painter.drawLine(QPointF(self.x_md, self.y_md), QPointF(self.x_rd, self.y_rd))
		painter.restore()

class BlackAreaUnit(QGraphicsObject):
	def __init__(self, pos, width, theta, side, direction, id_, parent = None):
		super(BlackAreaUnit, self).__init__(parent)
		self.pos = pos
		self.width = width
		self.theta = theta
		self.side = side
		self.direction = direction
		self.id = id_
		print "in black area:",self.pos

	def boundingRect(self):
		cor = self.mapFromScene(QPointF(0, 0))
		return QRectF(cor.x(),cor.y(),cor.x()+1000,cor.y()+1000)

	def getTheta(self):
		if self.direction[0] == 1:
			print "output1:",-(- self.theta + PI/2) *180/PI
			return -(- self.theta + PI/2) *180/PI
		else:
			print "output2:",(self.theta + PI/2) *180/PI
			return (self.theta + PI/2) *180/PI

	def paint(self, painter, option, widget = None):
		painter.save()
		painter.setPen(Qt.NoPen)
		brush = QBrush(QColor(0,0,0))
		painter.setBrush(brush)
		painter.drawRect(self.pos[0], self.pos[1], self.width, 10)
		painter.restore()

class RampUnit(QGraphicsObject):
	def __init__(self, x1, x2, y1, y2, id_, parent = None):
		super(RampUnit, self).__init__(parent)
		self.x1 = x1
		self.y1 = y1
		self.x2 = x2
		self.y2 = y2
		self.id = id_

	def paint(self, painter, option, widget = None):
		painter.save()
		pen = QPen()
		pen.setWidth(1)
		pen.setCapStyle(Qt.RoundCap)
		pen.setJoinStyle(Qt.RoundJoin)
		pen.setColor(QColor(0, 0, 0))
		painter.setPen(pen)
		painter.setBrush(Qt.NoBrush)
		painter.drawLine(self.x1, self.y1, self.x2, self.y2)
		painter.restore()

	def boundingRect(self):
		cor = self.mapFromScene(QPointF(0, 0))
		return QRectF(cor.x(),cor.y(),cor.x()+1000,cor.y()+1000)

class BarrierUnit(QGraphicsObject):
	def __init__(self, x1, y1, position, theta, direction, id_, parent = None):
		super(BarrierUnit, self).__init__(parent)
		if not position:
			self.x = x1 - 5 * math.sin(theta)
			self.y = y1 + 5 * math.cos(theta)
		else:
			self.x = x1 + 15 * math.sin(theta)
			self.y = y1 - 15 * math.cos(theta)
		if direction[0] == -1:
			self.x -= 30 * math.cos(theta)
			self.y -= 30 * math.sin(theta)
		self.setZValue(0.9)
		self.id = id_

	def boundingRect(self):
		cor = self.mapFromScene(QPointF(0, 0))
		return QRectF(cor.x(),cor.y(),cor.x()+1000,cor.y()+1000)

	def getOrigin(self):
		return QPointF(self.x, self.y)

	def paint(self, painter, option, widget = None):
		painter.save()
		pen = QPen()
		pen.setWidth(1)
		pen.setCapStyle(Qt.RoundCap)
		pen.setJoinStyle(Qt.RoundJoin)
		pen.setColor(QColor(0, 0, 0))
		painter.setPen(pen)
		painter.setBrush(Qt.NoBrush)
		painter.drawRect(self.x, self.y, 30, 10)
		painter.restore()

class CrossUnit(QGraphicsObject):
	def __init__(self, x1, y1, theta, width1, width2, direction, parent = None):
		super(CrossUnit, self).__init__(parent)
		self.x1 = x1
		self.y1 = y1
		self.width2 = width2
		self.theta = theta
		self.direction = direction
		print width1/2, theta
		self.x_lu = x1 - width1/2 * abs(math.sin(theta))
		self.point1_x = self.x_lu + width1 * abs(math.cos(theta)) * self.direction[0]
		self.y_lu = y1 + width1/2 * math.cos(theta)
		self.point1_y = self.y_lu + width1 * abs(math.sin(theta)) * self.direction[1]
		self.x_ld = x1 + width1/2 * math.sin(theta)
		self.point2_x = self.x_ld + width1 * abs(math.cos(theta)) * self.direction[0]
		self.y_ld = y1 - width1/2 * math.cos(theta)
		self.point2_y = self.y_ld + width1 * abs(math.sin(theta)) * self.direction[1]
		print self.x_lu, " ", self.y_lu, " ", self.x_ld, " ", self.y_ld, " ", self.point1_x, " ", self.point1_y, " ", self.point2_x, " ", self.point2_y

	def paint(self, painter, option, widget = None):
		painter.save()
		painter.setPen(Qt.NoPen)
		brush = QBrush(QColor(0,0,0),Qt.SolidPattern)
		painter.setBrush(brush)
		painter.drawEllipse(0, 0, self.width2, self.width2)
		painter.restore()

	def boundingRect(self):
		cor = self.mapFromScene(QPointF(0, 0))
		return QRectF(cor.x(),cor.y(),cor.x()+1000,cor.y()+1000)

	def getBeginPoint(self):
		print "BeginPoint:", [(float(self.x_lu + self.point1_x)/2.0, float(self.y_lu + self.point1_y)/2.0), (float(self.x_ld + self.point2_x)/2.0, float(self.y_ld + self.point2_y)/2.0), (float(self.point2_x + self.point1_x)/2.0, float(self.point2_y + self.point1_y)/2.0)]
		return [(float(self.x_lu + self.point1_x)/2.0, float(self.y_lu + self.point1_y)/2.0), (float(self.x_ld + self.point2_x)/2.0, float(self.y_ld + self.point2_y)/2.0), (float(self.point2_x + self.point1_x)/2.0, float(self.point2_y + self.point1_y)/2.0)]

	def getSlope(self):
		if self.theta + PI/2 > PI/2:
			self.theta -= PI
		elif self.theta + PI/2 <= -PI/2:
			self.theta += PI
		print "slope: ", [(PI/2+self.theta), (PI/2+self.theta), self.theta]
		return [(PI/2+self.theta), (PI/2+self.theta), self.theta]

	def getDirection(self):
		print "direction: ",[[self.direction[0], -self.direction[1]], self.direction, [-self.direction[0], self.direction[1]]]
		if float(self.x_lu + self.point1_x)/2.0 > float(self.x_ld + self.point2_x)/2.0:
			if float(self.y_lu + self.point1_y)/2.0 > float(self.y_ld + self.point2_y)/2.0:
				return [[1,1], [-1,-1], self.direction]
			else:
				return [[1,-1], [-1,1], self.direction]
		else:
			if float(self.y_lu + self.point1_y)/2.0 > float(self.y_ld + self.point2_y)/2.0:
				return [[-1,1], [1,-1], self.direction]
			else:
				return [[-1,-1], [1,1], self.direction]

class BeginPointUnit(QGraphicsTextItem):
	def __init__(self, text, x, y, id_ = None, parent = None):
		super(BeginPointUnit, self).__init__(text, parent)
		self.text = text
		self.x_ = x
		self.y_ = y
		font = self.font()
		self.setZValue(0.5)
		self.setDefaultTextColor(QColor(0,0,0))
		self.setFont(font)
		self.setPos(self.x_ - 4, self.y_ - 4)
		if id_:
			self.id = id_

	def setPosi(self):
		self.setPos(self.x_ - 4, self.y_ - 4)

	def setText(self, text):
		QGraphicsTextItem.setText(self, text)

	def boundingRect(self):
		cor = self.mapFromScene(QPointF(0, 0))
		return QRectF(cor.x(),cor.y(),cor.x()+1000,cor.y()+1000)

	def setColor(self, color):
		self.setDefaultTextColor(color)