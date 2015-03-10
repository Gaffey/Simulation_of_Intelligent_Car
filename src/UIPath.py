#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from ui_path import *
from PaintEvent import *
from EventHandler import *
import math, sys

PI = 3.1415926535898

class Path(QWidget, Ui_Form):
	def __init__(self, parent = None):
		super(Path, self).__init__(parent)
		self.setupUi(self)
		self.scene1 = QGraphicsScene()
		self.CenterWidget = PathView(self.scene1)
		self.CenterLayout.addWidget(self.CenterWidget)
		self.BeginPoint_list = {}
		bg = BeginPointUnit("0", 0, 0)
		self.BeginPoint_list[0] = bg
		self.last_slope = None
		self.tool = -1
		self.state = 0
		self.width_guide = 2
		self.commands = {"type":0, "beginpoint":0, "width1":0, "width2":0, "length":None, "arc":0, "x2":None, 
						"y2":None, "last_slope":self.last_slope, "radius":0, "position":0, "angle_u":0, "angle_d":0}
		self.element_list = []
		vali = QIntValidator(-1000, 1000)
		self.InputEdit.setValidator(vali)

		self.connect(self.CenterWidget, SIGNAL("Coordinate"), self.set_label)
		self.connect(self.CenterWidget, SIGNAL("zoomed"), self.zoom_text)

	@pyqtSlot()
	def on_NewButton_clicked(self):
		print "clicked start"
		self.CenterWidget.started = True

	def zoom_text(self, zoom_f):
		print "use zoom:",zoom_f
		self.ZoomLabel.setText(QString("%fx" %zoom_f))

	def Information(self):
		if self.tool == 0:
			if self.state == 0:
				if not self.last_slope:
					self.StateLabel.setText(QString.fromUtf8("请输入您想使用的起点x坐标:"))
				else:
					self.StateLabel.setText(QString.fromUtf8("请输入直线类型(0为普通，1为中心线):"))
			elif self.state == 1:
				if not self.last_slope:
					self.StateLabel.setText(QString.fromUtf8("请输入您想使用的起点y坐标:"))
				else:
					self.StateLabel.setText(QString.fromUtf8("请输入您想使用的起点:"))
			elif self.state == 2:
				if self.last_slope:
					self.StateLabel.setText(QString.fromUtf8("请输入直线长度:"))
				else:
					self.StateLabel.setText(QString.fromUtf8("请输入终点x坐标:"))
			elif self.state == 3:
				self.StateLabel.setText(QString.fromUtf8("请输入终点y坐标:"))
			elif self.state == 4:
				self.StateLabel.setText(QString.fromUtf8("请输入直线宽度:"))
		elif self.tool == 1:
			if self.state == 0:
				self.StateLabel.setText(QString.fromUtf8("请输入曲线类型(0为普通，1为中心线):"))
			elif self.state == 1:
				self.StateLabel.setText(QString.fromUtf8("请输入您想使用的起点:"))
			elif self.state == 2:
				self.StateLabel.setText(QString.fromUtf8("请输入曲率半径:"))
			elif self.state == 3:
				self.StateLabel.setText(QString.fromUtf8("请输入弧度值:"))
			elif self.state == 4:
				self.StateLabel.setText(QString.fromUtf8("请输入赛道宽度:"))
		elif self.tool == 2:
			if self.state == 0:
				self.StateLabel.setText(QString.fromUtf8("请输入您想使用的起点:"))
			elif self.state == 1:
				self.StateLabel.setText(QString.fromUtf8("请输入赛道宽度:"))
		elif self.tool == 3:
			if self.state == 0:
				self.StateLabel.setText(QString.fromUtf8("请输入您想使用的起点:"))
			elif self.state == 1:
				self.StateLabel.setText(QString.fromUtf8("请输入您想放置的位置(0下侧，1上侧):"))
			elif self.state == 2:
				self.StateLabel.setText(QString.fromUtf8("请输入赛道宽度:"))
		elif self.tool == 4:
			if self.state == 0:
				self.StateLabel.setText(QString.fromUtf8("请输入您想使用的起点:"))
			elif self.state == 1:
				self.StateLabel.setText(QString.fromUtf8("请输入坡道水平长度:"))
			elif self.state == 2:
				self.StateLabel.setText(QString.fromUtf8("请输入上行坡道角度:"))
			elif self.state == 3:
				self.StateLabel.setText(QString.fromUtf8("请输入下行坡道角度:"))
		elif self.tool == 5:
			if self.state == 0:
				self.StateLabel.setText(QString.fromUtf8("请输入您想使用的起点:"))
			elif self.state == 1:
				self.StateLabel.setText(QString.fromUtf8("请输入转角的方向(0顺,1逆):"))
			elif self.state == 2:
				self.StateLabel.setText(QString.fromUtf8("请输入赛道宽度:"))
		else:
			self.StateLabel.setText("")

	def set_label(self, pos):
		self.CoordinateLabel.setText("(%d,%d)" %(pos.x(), pos.y()))

	@pyqtSlot()
	def on_LineButton_clicked(self):
		print "in"
		self.commands = {"type":0, "beginpoint":0, "width1":0, "width2":self.width_guide, "length":None, "arc":0, "x2":None, 
						"y2":None, "last_slope":self.last_slope, "radius":0, "position":0, "angle_u":0, "angle_d":0}
		self.tool = 0
		self.state = 0
		self.Information()

	@pyqtSlot()
	def on_ArcButton_clicked(self):
		self.commands = {"type":0, "beginpoint":0, "width1":0, "width2":self.width_guide, "length":None, "arc":0, "x2":None, 
						"y2":None, "last_slope":self.last_slope, "radius":0, "position":0, "angle_u":0, "angle_d":0}
		self.tool = 1
		self.state = 0
		self.Information()

	@pyqtSlot()
	def on_CrossButton_clicked(self):
		self.commands = {"type":0, "beginpoint":0, "width1":0, "width2":self.width_guide, "length":None, "arc":0, "x2":None, 
						"y2":None, "last_slope":self.last_slope, "radius":0, "position":0, "angle_u":0, "angle_d":0}
		self.tool = 2
		self.state = 0
		self.Information()

	@pyqtSlot()
	def on_BarrierButton_clicked(self):
		self.commands = {"type":0, "beginpoint":0, "width1":0, "width2":self.width_guide, "length":None, "arc":0, "x2":None, 
						"y2":None, "last_slope":self.last_slope, "radius":0, "position":0, "angle_u":0, "angle_d":0}
		self.tool = 3
		self.state = 0
		self.Information()

	@pyqtSlot()
	def on_RampButton_clicked(self):
		self.commands = {"type":0, "beginpoint":0, "width1":0, "width2":self.width_guide, "length":None, "arc":0, "x2":None, 
						"y2":None, "last_slope":self.last_slope, "radius":0, "position":0, "angle_u":0, "angle_d":0}
		self.tool = 4
		self.state = 0
		self.Information()

	@pyqtSlot()
	def on_RightAngleButton_clicked(self):
		self.commands = {"type":0, "beginpoint":0, "width1":0, "width2":self.width_guide, "length":None, "arc":0, "x2":None, 
						"y2":None, "last_slope":self.last_slope, "radius":0, "position":0, "angle_u":0, "angle_d":0}
		self.tool = 5
		self.state = 0
		self.Information()

	@pyqtSlot()
	def on_InputEdit_editingFinished(self):
		command = int(unicode(self.InputEdit.text()))
		self.InputEdit.setText("")
		if self.tool == 0:
			if self.state == 0:
				if self.last_slope:
					if command in [0, 1]:
						self.commands["type"] = command
						self.state = 1
						self.Information()
					else:
						self.StateLabel.setText(QString.fromUtf8("输入错误，请输入0（普通）或1（中心线）。"))
						return
				else:
					if command > 0:
						self.BeginPoint_list[0].x = command
						self.state = 1
						self.Information()
					else:
						self.StateLabel.setText(QString.fromUtf8("输入错误，请输入大于0的数字"))
						return
			elif self.state == 1:
				if self.last_slope:
					if command in range(len(self.BeginPoint_list.keys())):
						self.commands["beginpoint"] = command
						self.state = 2
						self.Information()
					else:
						self.StateLabel.setText(QString.fromUtf8("输入错误，请输入0~%d的数字" %len(self.BeginPoint_list.keys()) - 1))
						return
				else:
					if command > 0:
						self.BeginPoint_list[0].y = command
						self.BeginPoint_list[0].setPosi()
						self.state = 2
						self.Information()
					else:
						self.StateLabel.setText(QString.fromUtf8("输入错误，请输入大于0的数字"))
						return
			elif self.state == 2:
				if self.last_slope:
					if command > 0:
						self.commands["length"] = command
						self.state = 4
						self.Information()
					else:
						self.StateLabel.setText(QString.fromUtf8("输入错误，请输入大于0的数字"))
						return
				else:
					if command > 0:
						self.commands["x2"] = command
						self.state = 3
						self.Information()
					else:
						self.StateLabel.setText(QString.fromUtf8("输入错误，请输入大于0的数字"))
						return
			elif self.state == 3:
				if command > 0:
					self.commands["y2"] = command
					self.state = 4
					self.Information()
				else:
					self.StateLabel.setText(QString.fromUtf8("输入错误，请输入大于0的数字"))
					return
			elif self.state == 4:
				if command >= 45:
					self.commands["width1"] = command
					if self.commands["type"]:
						graphs = CenterLineUnit(self.BeginPoint_list[self.commands["beginpoint"]].x, self.BeginPoint_list[self.commands["beginpoint"]].y, self.commands["width2"], self.commands["last_slope"][self.commands["beginpoint"]][1], self.commands["x2"], self.commands["y2"], self.commands["last_slope"][self.commands["beginpoint"]][0], self.commands["length"])
					else:
						if not self.last_slope:
							graphs = LineUnit(self.BeginPoint_list[self.commands["beginpoint"]].x, self.BeginPoint_list[self.commands["beginpoint"]].y, self.commands["width1"], self.commands["width2"], None, self.commands["x2"], self.commands["y2"], self.commands["length"], None)
						else:
							graphs = LineUnit(self.BeginPoint_list[self.commands["beginpoint"]].x, self.BeginPoint_list[self.commands["beginpoint"]].y, self.commands["width1"], self.commands["width2"], self.commands["last_slope"][self.commands["beginpoint"]][1], self.commands["x2"], self.commands["y2"], self.commands["length"], self.commands["last_slope"][self.commands["beginpoint"]][0])
					for points in graphs.getBeginPoint():
						if points[0] < 0 or points[1] < 0:
							self.StateLabel.setText(QString.fromUtf8("超出边界，绘制失败"))
							self.state = 0
							self.tool = -1
							self.LineButton.setChecked(False)
							return
					if self.last_slope:
						has = False
						self.scene1.removeItem(self.BeginPoint_list[self.commands["beginpoint"]])
						for unit in self.BeginPoint_list.values():
							if unit.x == graphs.getBeginPoint()[0][0] and unit.y == graphs.getBeginPoint()[0][1]:
								has = True
								for k in self.BeginPoint_list.keys():
									if self.BeginPoint_list[k] == unit:
										del self.BeginPoint_list[k]
										break
								break
						if not has:
							bg = BeginPointUnit("%d" %self.commands["beginpoint"], graphs.getBeginPoint()[0][0], graphs.getBeginPoint()[0][1])
							self.BeginPoint_list[self.commands["beginpoint"]] = bg
							self.scene1.addItem(bg)
							self.last_slope[self.commands["beginpoint"]] = (graphs.getSlope(), graphs.getDirection())
					else:
						bg = BeginPointUnit("1", graphs.getBeginPoint()[0][0], graphs.getBeginPoint()[0][1])
						self.BeginPoint_list[1] = bg
						self.scene1.addItem(bg)
						self.scene1.addItem(self.BeginPoint_list[0])
						self.last_slope = [0 for x in range(100)]
						self.last_slope[0] = (graphs.getSlope(), [-graphs.getDirection()[0], -graphs.getDirection()[1]])
						self.last_slope[1] = (graphs.getSlope(), graphs.getDirection())
					self.element_list.append(graphs)
					self.scene1.addItem(graphs)
					self.LineButton.setChecked(False)
					self.tool = -1
				else:
					self.StateLabel.setText(QString.fromUtf8("输入错误，请输入大于等于45的数字"))
					return
		elif self.tool == 1:
			if self.state == 0:
				if command in [0, 1]:
					self.commands["type"] = command
					self.state = 1
					self.Information()
				else:
					self.StateLabel.setText(QString.fromUtf8("输入错误，请输入0（普通）或1（中心线）。"))
			elif self.state == 1:
				if command in range(len(self.BeginPoint_list.keys())):
					self.commands["beginpoint"] = command
					self.state = 2
					self.Information()
				else:
					self.StateLabel.setText(QString.fromUtf8("输入错误，请输入0~%d的数字" %len(self.BeginPoint_list.keys()) - 1))
			elif self.state == 2:
				if command > 0:
					self.commands["radius"] = command
					self.state = 3
					self.Information()
				else:
					self.StateLabel.setText(QString.fromUtf8("输入错误，请输入大于0的数字"))
					return
			elif self.state == 3:
				if command < 360 and command > -360:
					self.commands["arc"] = command
					self.state = 4
					self.Information()
				else:
					self.StateLabel.setText(QString.fromUtf8("输入错误，请输入-360~360的数字"))
					return
			elif self.state == 4:
				if command >= 45:
					self.commands["width1"] = command
					if self.commands["type"]:
						graphs = CenterArcUnit(self.BeginPoint_list[self.commands["beginpoint"]].x, self.BeginPoint_list[self.commands["beginpoint"]].y, self.commands["arc"], self.commands["radius"], self.commands["last_slope"][self.commands["beginpoint"]][0], self.commands["width2"], self.commands["last_slope"][self.commands["beginpoint"]][1])
					else:
						graphs = ArcUnit(self.BeginPoint_list[self.commands["beginpoint"]].x, self.BeginPoint_list[self.commands["beginpoint"]].y, self.commands["arc"], self.commands["radius"], self.commands["last_slope"][self.commands["beginpoint"]][0], self.commands["width1"], self.commands["width2"], self.commands["last_slope"][self.commands["beginpoint"]][1])
					for points in graphs.getBeginPoint():
						if points[0] < 0 or points[1] < 0:
							self.StateLabel.setText(QString.fromUtf8("超出边界，绘制失败"))
							self.state = 0
							self.tool = -1
							self.ArcButton.setChecked(False)
							return
					if self.last_slope:
						has = False
						self.scene1.removeItem(self.BeginPoint_list[self.commands["beginpoint"]])
						for unit in self.BeginPoint_list.values():
							if unit.x == graphs.getBeginPoint()[0][0] and unit.y == graphs.getBeginPoint()[0][1]:
								has = True
								for k in self.BeginPoint_list.keys():
									if self.BeginPoint_list[k] == unit:
										del self.BeginPoint_list[k]
										'''
										直接用del可能用错误
										'''
										break
								break
						if not has:
							bg = BeginPointUnit("%d" %self.commands["beginpoint"], graphs.getBeginPoint()[0][0], graphs.getBeginPoint()[0][1])
							self.BeginPoint_list[self.commands["beginpoint"]] = bg
							self.scene1.addItem(bg)
							self.last_slope[self.commands["beginpoint"]] = (graphs.getSlope(), graphs.getDirection())
					else:
						for i in range(100):
							if i not in self.BeginPoint_list.keys():
								bg = BeginPointUnit("%d" %i, graphs.getBeginPoint()[0][0], graphs.getBeginPoint()[0][1])
								self.BeginPoint_list[i] = bg
								self.scene1.addItem(bg)
								self.last_slope[0] = (graphs.getSlope(), graphs.getDirection())
								self.last_slope[i] = (graphs.getSlope(), graphs.getDirection())
								break
					self.element_list.append(graphs)
					self.scene1.addItem(graphs)
					self.ArcButton.setChecked(False)
					self.tool = -1
				else:
					self.StateLabel.setText(QString.fromUtf8("输入错误，请输入大于等于45的数字"))
					return

		elif self.tool == 2:
			if self.state == 0:
				if command in range(len(self.BeginPoint_list.keys())):
					self.commands["beginpoint"] = command
					self.state = 1
					self.Information()
				else:
					self.StateLabel.setText(QString.fromUtf8("输入错误，请输入0~%d的数字" %len(self.BeginPoint_list.keys()) - 1))
					return
			elif self.state == 1:
				if command >= 45:
					self.commands["width1"] = command
					graphs = CrossUnit(self.BeginPoint_list[self.commands["beginpoint"]].x, self.BeginPoint_list[self.commands["beginpoint"]].y, self.commands["last_slope"][self.commands["beginpoint"]][0], self.commands["width1"], self.commands["width2"], self.commands["last_slope"][self.commands["beginpoint"]][1])
					for points in graphs.getBeginPoint():
						if points[0] < 0 or points[1] < 0:
							self.StateLabel.setText(QString.fromUtf8("超出边界，绘制失败"))
							self.state = 0
							self.tool = -1
							self.CrossButton.setChecked(False)
							return
					has = [False for x in range(len(graphs.getBeginPoint()))]
					self.scene1.removeItem(self.BeginPoint_list[self.commands["beginpoint"]])
					del self.BeginPoint_list[self.commands["beginpoint"]]
					for index in range(len(graphs.getBeginPoint())):
						for unit in self.BeginPoint_list.values():
							if unit.x == graphs.getBeginPoint()[index][0] and unit.y == graphs.getBeginPoint()[index][1]:
								has[index] = True
								for k in self.BeginPoint_list.keys():
									if self.BeginPoint_list[k] == unit:
										del self.BeginPoint_list[k]
										break
						if not has[index]:
							for i in range(100):
								if i not in self.BeginPoint_list.keys():
									bg = BeginPointUnit("%d" %i, graphs.getBeginPoint()[index][0], graphs.getBeginPoint()[index][1])
									self.BeginPoint_list[i] = bg
									self.scene1.addItem(bg)
									self.last_slope[i] = (graphs.getSlope()[index], graphs.getDirection()[index])
									break
					self.element_list.append(graphs)
					self.scene1.addItem(graphs)
					self.CrossButton.setChecked(False)
					self.tool = -1
				else:
					self.StateLabel.setText(QString.fromUtf8("输入错误，请输入大于等于45的数字"))
					return

		elif self.tool == 3:
			if self.state == 0:
				if command in range(len(self.BeginPoint_list.keys())):
					self.commands["beginpoint"] = command
					self.state = 1
					self.Information()
				else:
					self.StateLabel.setText(QString.fromUtf8("输入错误，请输入0~%d的数字" %len(self.BeginPoint_list.keys()) - 1))
			elif self.state == 1:
				if command in [0, 1]:
					self.commands["position"] = command
					self.state = 2
					self.Information()
				else:
					self.StateLabel.setText(QString.fromUtf8("输入错误，请输入0（下侧）或1（上侧）。"))
			elif self.state == 2:
				if command >= 45:
					self.commands["width1"] = command
					graphs_bar = BarrierUnit(self.BeginPoint_list[self.commands["beginpoint"]].x, self.BeginPoint_list[self.commands["beginpoint"]].y, self.commands["position"], self.commands["last_slope"][self.commands["beginpoint"]][0], self.commands["last_slope"][self.commands["beginpoint"]][1])
					print "set rotation: ", self.commands["last_slope"][self.commands["beginpoint"]][0]*180/PI
					graphs_bar.setTransformOriginPoint(graphs_bar.getOrigin())
					graphs_bar.setRotation(self.commands["last_slope"][self.commands["beginpoint"]][0]*180/PI)
					self.scene1.addItem(graphs_bar)
					self.element_list.append(graphs_bar)
					graphs = LineUnit(self.BeginPoint_list[self.commands["beginpoint"]].x, self.BeginPoint_list[self.commands["beginpoint"]].y, self.commands["width1"], self.commands["width2"], self.commands["last_slope"][self.commands["beginpoint"]][1], self.commands["x2"], self.commands["y2"], 30, self.commands["last_slope"][self.commands["beginpoint"]][0])
					for points in graphs.getBeginPoint():
						if points[0] < 0 or points[1] < 0:
							self.StateLabel.setText(QString.fromUtf8("超出边界，绘制失败"))
							self.state = 0
							self.tool = -1
							self.CrossButton.setChecked(False)
							return
					has = False
					self.scene1.removeItem(self.BeginPoint_list[self.commands["beginpoint"]])
					for unit in self.BeginPoint_list.values():
						if abs(unit.x - graphs.getBeginPoint()[0][0]) <= 1 and abs(unit.y - graphs.getBeginPoint()[0][1]) <= 1:
							has = True
							for k in self.BeginPoint_list.keys():
								if self.BeginPoint_list[k] == unit:
									del self.BeginPoint_list[k]
									break
							break
					if not has:
						bg = BeginPointUnit("%d" %self.commands["beginpoint"], graphs.getBeginPoint()[0][0], graphs.getBeginPoint()[0][1])
						self.BeginPoint_list[self.commands["beginpoint"]] = bg
						self.scene1.addItem(bg)
						self.last_slope[self.commands["beginpoint"]] = (graphs.getSlope(), graphs.getDirection())
					self.element_list.append(graphs)
					self.scene1.addItem(graphs)
					self.BarrierButton.setChecked(False)
					self.tool = -1
				else:
					self.StateLabel.setText(QString.fromUtf8("输入错误，请输入大于等于45的数字"))
					return


		elif self.tool == 4:
			if self.state == 0:
				if command in range(len(self.BeginPoint_list.keys())):
					self.commands["beginpoint"] = command
					self.state = 1
					self.Information()
				else:
					self.StateLabel.setText(QString.fromUtf8("输入错误，请输入0~%d的数字" %len(self.BeginPoint_list.keys())))
			elif self.state == 1:
				self.commands["length"] = command
			elif self.state == 2:
				self.commands["angle_u"] = command
			elif self.state == 3:
				self.commands["angle_d"] = command
		elif self.tool == 5:
			if self.state == 0:
				if command in range(len(self.BeginPoint_list.keys())):
					self.commands["beginpoint"] = command
					self.state = 1
					self.Information()
				else:
					self.StateLabel.setText(QString.fromUtf8("输入错误，请输入0~%d的数字" %len(self.BeginPoint_list.keys())))
			elif self.state == 1:
				if command in [0, 1]:
					self.commands["position"] = command
					self.state = 2
					self.Information()
				else:
					self.StateLabel.setText(QString.fromUtf8("输入错误，请输入0(顺)/1(逆)"))
			elif self.state == 2:
				if command >= 45:
					self.commands["width1"] = command
					graphs = RightAngleUnit(self.BeginPoint_list[self.commands["beginpoint"]].x, self.BeginPoint_list[self.commands["beginpoint"]].y, self.commands["width1"], self.commands["width2"], self.commands["last_slope"][self.commands["beginpoint"]][0], self.commands["last_slope"][self.commands["beginpoint"]][1], self.commands["position"])
					for points in graphs.getBeginPoint():
						if points[0] < 0 or points[1] < 0:
							self.StateLabel.setText(QString.fromUtf8("超出边界，绘制失败"))
							self.state = 0
							self.tool = -1
							self.CrossButton.setChecked(False)
							return
					pos = graphs.getPos()
					black1 = BlackAreaUnit(pos[0], self.commands["width1"])
					black1.setTransformOriginPoint(QPointF(pos[0][0], pos[0][1]))
					black1.setRotation(self.commands["last_slope"][self.commands["beginpoint"]][0]*180/PI - 90)
					black2 = BlackAreaUnit(pos[1], self.commands["width1"])
					black2.setTransformOriginPoint(QPointF(pos[1][0], pos[1][1]))
					black2.setRotation(graphs.getSlope()[0]*180/PI - 90)
					self.scene1.addItem(black1)
					self.scene1.addItem(black2)
					has = False
					self.scene1.removeItem(self.BeginPoint_list[self.commands["beginpoint"]])
					for unit in self.BeginPoint_list.values():
						if unit.x == graphs.getBeginPoint()[0][0] and unit.y == graphs.getBeginPoint()[0][1]:
							has = True
							for k in self.BeginPoint_list.keys():
								if self.BeginPoint_list[k] == unit:
									del self.BeginPoint_list[k]
									break
							break
					if not has:
						bg = BeginPointUnit("%d" %self.commands["beginpoint"], graphs.getBeginPoint()[0][0], graphs.getBeginPoint()[0][1])
						self.BeginPoint_list[self.commands["beginpoint"]] = bg
						self.scene1.addItem(bg)
						self.last_slope[self.commands["beginpoint"]] = graphs.getSlope()
					self.scene1.addItem(graphs)
					self.element_list.append(graphs)
					self.RightAngleButton.setChecked(False)
					self.tool = -1
				else:
					self.StateLabel.setText(QString.fromUtf8("输入错误，请输入大于等于45的数字"))
					return

		else:
			self.StateLabel.setText("")

if __name__ == "__main__":
	app = QApplication(sys.argv)
	form = Path()
	form.show()
	app.exec_()