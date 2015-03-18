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
		self.mode = -1
		self.width_guide = 2
		self.commands = {"type":0, "beginpoint":0, "width1":0, "width2":0, "length":None, "arc":0, "x2":None, 
						"y2":None, "last_slope":self.last_slope, "radius":0, "position":0, "angle_u":0, "angle_d":0, "length_u":None, "length_d":None}
		self.element_list = []
		self.black_list = []
		self.barrier_list = []
		self.ramp_list = []
		vali = QIntValidator(-1000, 1000)
		self.InputEdit.setValidator(vali)

		self.connect(self.CenterWidget, SIGNAL("Coordinate"), self.set_label)
		self.connect(self.CenterWidget, SIGNAL("zoomed"), self.zoom_text)

		self.LineButton.setEnabled(False)
		self.ArcButton.setEnabled(False)
		self.BarrierButton.setEnabled(False)
		self.RampButton.setEnabled(False)
		self.RightAngleButton.setEnabled(False)
		self.CrossButton.setEnabled(False)
		self.DeleteButton.setEnabled(False)
		self.CloseButton.setEnabled(False)

		self.MinEdit.setEnabled(False)
		self.MaxEdit.setEnabled(False)
		self.NewButton.setEnabled(False)
		self.SaveButton.setEnabled(False)

		self.count = 0

		self.table_head = QStringList()
		self.tableWidget.setColumnCount(4)
		self.table_head.append(QString.fromUtf8("类型"))
		self.table_head.append(QString.fromUtf8("起点"))
		self.table_head.append(QString.fromUtf8("终点/半径"))
		self.table_head.append(QString.fromUtf8("宽度"))
		self.tableWidget.setHorizontalHeaderLabels(self.table_head)
		self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
		self.StateLabel.setText(QString.fromUtf8("请先选择赛道参数或者打开一条赛道"))

	@pyqtSlot(int)
	def on_comboBox_currentIndexChanged(self, index):
		if index == 0:
			self.MinEdit.setText("")
			self.MinEdit.setEnabled(False)
			self.MaxEdit.setText("")
			self.MaxEdit.setEnabled(False)
			self.LightEdit.setEnabled(True)
		else:
			self.LightEdit.setText("")
			self.LightEdit.setEnabled(False)
			self.MinEdit.setEnabled(True)
			self.MaxEdit.setEnabled(True)
		self.updateUi()

	def updateUi(self):
		print "update"
		if self.comboBox.currentIndex():
			if self.MinEdit.text() != "" and self.MaxEdit.text() != "" and self.TWidthEdit.text() != ""	and self.TLengthEdit.text() != "" and self.FrictionEdit.text() != "":
				self.NewButton.setEnabled(True)
				self.mode = 1
			else:
				self.NewButton.setEnabled(False)
		else:
			if self.TWidthEdit.text() != "" and self.LightEdit.text() != ""	and self.TLengthEdit.text() != "" and self.FrictionEdit.text() != "":
				self.NewButton.setEnabled(True)
				self.mode = 0
			else:
				self.NewButton.setEnabled(False)

	@pyqtSlot(QString)
	def on_MinEdit_textEdited(self, text):
		self.updateUi()

	@pyqtSlot(QString)
	def on_MaxEdit_textEdited(self, text):
		self.updateUi()

	@pyqtSlot(QString)
	def on_LightEdit_textEdited(self, text):
		self.updateUi()

	@pyqtSlot(QString)
	def on_FrictionEdit_textEdited(self, text):
		self.updateUi()

	@pyqtSlot(QString)
	def on_TWidthEdit_textEdited(self, text):
		self.updateUi()

	@pyqtSlot(QString)
	def on_TLengthEdit_textEdited(self, text):
		self.updateUi()

	@pyqtSlot()
	def on_NewButton_clicked(self):
		print "clicked start"
		self.CenterWidget.started = True
		self.LineButton.setEnabled(True)
		self.StateLabel.setText(QString.fromUtf8("请创建一条直线赛道作为开始"))
		self.MinEdit.setEnabled(False)
		self.MaxEdit.setEnabled(False)
		self.LightEdit.setEnabled(False)
		self.FrictionEdit.setEnabled(False)
		self.TWidthEdit.setEnabled(False)
		self.TLengthEdit.setEnabled(False)
		self.comboBox.setEnabled(False)


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
				self.StateLabel.setText(QString.fromUtf8("请输入角度数:"))
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
				self.StateLabel.setText(QString.fromUtf8("请输入赛道宽度:"))
			elif self.state == 2:
				self.StateLabel.setText(QString.fromUtf8("请输入上行坡道角度:"))
			elif self.state == 3:
				self.StateLabel.setText(QString.fromUtf8("请输入上行坡道水平长度:"))
			elif self.state == 4:
				self.StateLabel.setText(QString.fromUtf8("请输入下行坡道角度:"))
			elif self.state == 5:
				self.StateLabel.setText(QString.fromUtf8("请输入下行坡道水平长度:"))
			elif self.state == 6:
				self.StateLabel.setText(QString.fromUtf8("请输入水平坡道的长度"))
		elif self.tool == 5:
			if self.state == 0:
				self.StateLabel.setText(QString.fromUtf8("请输入您想使用的起点:"))
			elif self.state == 1:
				self.StateLabel.setText(QString.fromUtf8("请输入转角的方向(0顺,1逆):"))
			elif self.state == 2:
				self.StateLabel.setText(QString.fromUtf8("请输入赛道宽度:"))
			elif self.state == 3:
				self.StateLabel.setText(QString.fromUtf8("请输入折角角度:"))
		elif self.tool == 7:
			self.StateLabel.setText(QString.fromUtf8("请输入您想删除的赛道编号:"))
		else:
			self.StateLabel.setText("")


	def set_label(self, pos):
		self.CoordinateLabel.setText("(%d,%d)" %(pos.x(), pos.y()))

	@pyqtSlot()
	def on_LineButton_clicked(self):
		print "in"
		self.commands = {"type":0, "beginpoint":0, "width1":0, "width2":self.width_guide, "length":None, "arc":0, "x2":None, 
						"y2":None, "last_slope":self.last_slope, "radius":0, "position":0, "angle_u":0, "angle_d":0, "length_u":None, "length_d":None}
		self.tool = 0
		self.state = 0
		self.Information()

	@pyqtSlot()
	def on_ArcButton_clicked(self):
		self.commands = {"type":0, "beginpoint":0, "width1":0, "width2":self.width_guide, "length":None, "arc":0, "x2":None, 
						"y2":None, "last_slope":self.last_slope, "radius":0, "position":0, "angle_u":0, "angle_d":0, "length_u":None, "length_d":None}
		self.tool = 1
		self.state = 0
		self.Information()

	@pyqtSlot()
	def on_CrossButton_clicked(self):
		self.commands = {"type":0, "beginpoint":0, "width1":0, "width2":self.width_guide, "length":None, "arc":0, "x2":None, 
						"y2":None, "last_slope":self.last_slope, "radius":0, "position":0, "angle_u":0, "angle_d":0, "length_u":None, "length_d":None}
		self.tool = 2
		self.state = 0
		self.Information()

	@pyqtSlot()
	def on_BarrierButton_clicked(self):
		self.commands = {"type":0, "beginpoint":0, "width1":0, "width2":self.width_guide, "length":None, "arc":0, "x2":None, 
						"y2":None, "last_slope":self.last_slope, "radius":0, "position":0, "angle_u":0, "angle_d":0, "length_u":None, "length_d":None}
		self.tool = 3
		self.state = 0
		self.Information()

	@pyqtSlot()
	def on_RampButton_clicked(self):
		self.commands = {"type":0, "beginpoint":0, "width1":0, "width2":self.width_guide, "length":None, "arc":0, "x2":None, 
						"y2":None, "last_slope":self.last_slope, "radius":0, "position":0, "angle_u":0, "angle_d":0, "length_u":None, "length_d":None}
		self.tool = 4
		self.state = 0
		self.Information()

	@pyqtSlot()
	def on_RightAngleButton_clicked(self):
		self.commands = {"type":0, "beginpoint":0, "width1":0, "width2":self.width_guide, "length":None, "arc":0, "x2":None, 
						"y2":None, "last_slope":self.last_slope, "radius":0, "position":0, "angle_u":0, "angle_d":0, "length_u":None, "length_d":None}
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
						self.BeginPoint_list[0].x_ = command
						self.state = 1
						self.Information()
					else:
						self.StateLabel.setText(QString.fromUtf8("输入错误，请输入大于0的数字"))
						return
			elif self.state == 1:
				if self.last_slope:
					if command in self.BeginPoint_list.keys():
						self.commands["beginpoint"] = command
						self.state = 2
						self.Information()
					else:
						self.StateLabel.setText(QString.fromUtf8("输入错误，请输入显示为起点的数字"))
						return
				else:
					if command > 0:
						self.BeginPoint_list[0].y_ = command
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
						print "I get command:",command
						self.state = 3
						self.Information()
					else:
						self.StateLabel.setText(QString.fromUtf8("输入错误，请输入大于0的数字"))
						return
			elif self.state == 3:
				if command > 0:
					self.commands["y2"] = command
					print "I get command:",command
					self.state = 4
					self.Information()
				else:
					self.StateLabel.setText(QString.fromUtf8("输入错误，请输入大于0的数字"))
					return
			elif self.state == 4:
				if command >= 45:
					self.commands["width1"] = command
					print self.commands
					if self.commands["type"]:
						graphs = CenterLineUnit(self.BeginPoint_list[self.commands["beginpoint"]].x_, self.BeginPoint_list[self.commands["beginpoint"]].y_, self.commands["width2"], self.commands["last_slope"][self.commands["beginpoint"]][1], self.commands["x2"], self.commands["y2"], self.commands["last_slope"][self.commands["beginpoint"]][0], self.commands["length"])
					else:
						if not self.last_slope:
							graphs = LineUnit(self.BeginPoint_list[self.commands["beginpoint"]].x_, self.BeginPoint_list[self.commands["beginpoint"]].y_, self.commands["width1"], self.commands["width2"], None, self.commands["x2"], self.commands["y2"], self.commands["length"], None)
						else:
							print self.BeginPoint_list[self.commands["beginpoint"]].x_, self.BeginPoint_list[self.commands["beginpoint"]].y_, self.commands["width1"], self.commands["width2"], self.commands["last_slope"][self.commands["beginpoint"]][1], self.commands["x2"], self.commands["y2"], self.commands["length"], self.commands["last_slope"][self.commands["beginpoint"]][0]
							graphs = LineUnit(self.BeginPoint_list[self.commands["beginpoint"]].x_, self.BeginPoint_list[self.commands["beginpoint"]].y_, self.commands["width1"], self.commands["width2"], self.commands["last_slope"][self.commands["beginpoint"]][1], self.commands["x2"], self.commands["y2"], self.commands["length"], self.commands["last_slope"][self.commands["beginpoint"]][0])
					for points in graphs.getBeginPoint():
						if points[0] < 0 or points[1] < 0:
							self.StateLabel.setText(QString.fromUtf8("超出边界，绘制失败"))
							self.state = 0
							self.tool = -1
							self.LineButton.setChecked(False)
							return
					self.tableWidget.insertRow(self.tableWidget.rowCount())
					self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 0, QTableWidgetItem(QString.fromUtf8("直线赛道")))
					self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 1, QTableWidgetItem(QString.fromUtf8("(%d, %d)" %(self.BeginPoint_list[self.commands["beginpoint"]].x_, self.BeginPoint_list[self.commands["beginpoint"]].y_))))
					self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 2, QTableWidgetItem(QString.fromUtf8("(%d, %d)" %(graphs.getBeginPoint()[0][0], graphs.getBeginPoint()[0][1]))))
					self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 3, QTableWidgetItem(QString.fromUtf8("%d" %self.commands["width1"])))
					if self.last_slope:
						has = False
						self.scene1.removeItem(self.BeginPoint_list[self.commands["beginpoint"]])
						for unit in self.BeginPoint_list.values():
							if abs(unit.x_ - graphs.getBeginPoint()[0][0]) <= 2 and abs(unit.y_ - graphs.getBeginPoint()[0][1]) <= 2:
								has = True
								for k in self.BeginPoint_list.keys():
									if self.BeginPoint_list[k] == unit:
										self.scene1.removeItem(self.BeginPoint_list[k])
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
						self.ArcButton.setEnabled(True)
						self.BarrierButton.setEnabled(True)
						self.RampButton.setEnabled(True)
						self.RightAngleButton.setEnabled(True)
						self.CrossButton.setEnabled(True)
						self.DeleteButton.setEnabled(True)
						self.CloseButton.setEnabled(True)
						self.SaveButton.setEnabled(True)
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
				if command in self.BeginPoint_list.keys():
					self.commands["beginpoint"] = command
					self.state = 2
					self.Information()
				else:
					self.StateLabel.setText(QString.fromUtf8("输入错误，请输入显示为起点的数字"))
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
						graphs = CenterArcUnit(self.BeginPoint_list[self.commands["beginpoint"]].x_, self.BeginPoint_list[self.commands["beginpoint"]].y_, self.commands["arc"], self.commands["radius"], self.commands["last_slope"][self.commands["beginpoint"]][0], self.commands["width2"], self.commands["last_slope"][self.commands["beginpoint"]][1])
					else:
						graphs = ArcUnit(self.BeginPoint_list[self.commands["beginpoint"]].x_, self.BeginPoint_list[self.commands["beginpoint"]].y_, self.commands["arc"], self.commands["radius"], self.commands["last_slope"][self.commands["beginpoint"]][0], self.commands["width1"], self.commands["width2"], self.commands["last_slope"][self.commands["beginpoint"]][1])
					for points in graphs.getBeginPoint():
						if points[0] < 0 or points[1] < 0:
							self.StateLabel.setText(QString.fromUtf8("超出边界，绘制失败"))
							self.state = 0
							self.tool = -1
							self.ArcButton.setChecked(False)
							return
					self.tableWidget.insertRow(self.tableWidget.rowCount())
					self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 0, QTableWidgetItem(QString.fromUtf8("圆弧赛道")))
					self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 1, QTableWidgetItem(QString.fromUtf8("(%d, %d)" %(self.BeginPoint_list[self.commands["beginpoint"]].x_, self.BeginPoint_list[self.commands["beginpoint"]].y_))))
					self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 2, QTableWidgetItem(QString.fromUtf8("%d" %self.commands["radius"])))
					self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 3, QTableWidgetItem(QString.fromUtf8("%d" %self.commands["width1"])))
					if self.last_slope:
						has = False
						self.scene1.removeItem(self.BeginPoint_list[self.commands["beginpoint"]])
						for unit in self.BeginPoint_list.values():
							if abs(unit.x_ - graphs.getBeginPoint()[0][0]) <= 2 and abs(unit.y_ - graphs.getBeginPoint()[0][1]) <= 2:
								has = True
								for k in self.BeginPoint_list.keys():
									if self.BeginPoint_list[k] == unit:
										self.scene1.removeItem(self.BeginPoint_list[k])
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
				if command in self.BeginPoint_list.keys():
					self.commands["beginpoint"] = command
					self.state = 1
					self.Information()
				else:
					self.StateLabel.setText(QString.fromUtf8("输入错误，请输入显示为起点的数字"))
					return
			elif self.state == 1:
				if command >= 45:
					self.commands["width1"] = command
					graphs = CrossUnit(self.BeginPoint_list[self.commands["beginpoint"]].x_, self.BeginPoint_list[self.commands["beginpoint"]].y_, self.commands["last_slope"][self.commands["beginpoint"]][0], self.commands["width1"], self.commands["width2"], self.commands["last_slope"][self.commands["beginpoint"]][1])
					for points in graphs.getBeginPoint():
						if points[0] < 0 or points[1] < 0:
							self.StateLabel.setText(QString.fromUtf8("超出边界，绘制失败"))
							self.state = 0
							self.tool = -1
							self.CrossButton.setChecked(False)
							return
					self.tableWidget.insertRow(self.tableWidget.rowCount())
					self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 0, QTableWidgetItem(QString.fromUtf8("十字交叉")))
					self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 1, QTableWidgetItem(QString.fromUtf8("(%d, %d)" %(self.BeginPoint_list[self.commands["beginpoint"]].x_, self.BeginPoint_list[self.commands["beginpoint"]].y_))))
					self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 3, QTableWidgetItem(QString.fromUtf8("%d" %self.commands["width1"])))
					has = [False for x in range(len(graphs.getBeginPoint()))]
					self.scene1.removeItem(self.BeginPoint_list[self.commands["beginpoint"]])
					del self.BeginPoint_list[self.commands["beginpoint"]]
					for index in range(len(graphs.getBeginPoint())):
						for unit in self.BeginPoint_list.values():
							if abs(unit.x_ - graphs.getBeginPoint()[index][0]) <= 2 and abs(unit.y_ - graphs.getBeginPoint()[index][1]) <= 2:
								has[index] = True
								for k in self.BeginPoint_list.keys():
									if self.BeginPoint_list[k] == unit:
										self.scene1.removeItem(self.BeginPoint_list[k])
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
				if command in self.BeginPoint_list.keys():
					self.commands["beginpoint"] = command
					self.state = 1
					self.Information()
				else:
					self.StateLabel.setText(QString.fromUtf8("输入错误，请输入显示为起点的数字"))
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
					graphs = LineUnit(self.BeginPoint_list[self.commands["beginpoint"]].x_, self.BeginPoint_list[self.commands["beginpoint"]].y_, self.commands["width1"], self.commands["width2"], self.commands["last_slope"][self.commands["beginpoint"]][1], self.commands["x2"], self.commands["y2"], 30, self.commands["last_slope"][self.commands["beginpoint"]][0])
					graphs_bar = BarrierUnit(self.BeginPoint_list[self.commands["beginpoint"]].x_, self.BeginPoint_list[self.commands["beginpoint"]].y_, self.commands["position"], self.commands["last_slope"][self.commands["beginpoint"]][0], self.commands["last_slope"][self.commands["beginpoint"]][1], graphs)
					print "set rotation: ", self.commands["last_slope"][self.commands["beginpoint"]][0]*180/PI
					graphs_bar.setTransformOriginPoint(graphs_bar.getOrigin())
					graphs_bar.setRotation(self.commands["last_slope"][self.commands["beginpoint"]][0]*180/PI)
					self.scene1.addItem(graphs_bar)
					self.barrier_list.append(graphs_bar)
					for points in graphs.getBeginPoint():
						if points[0] < 0 or points[1] < 0:
							self.StateLabel.setText(QString.fromUtf8("超出边界，绘制失败"))
							self.state = 0
							self.tool = -1
							self.CrossButton.setChecked(False)
							return
					self.tableWidget.insertRow(self.tableWidget.rowCount())
					self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 0, QTableWidgetItem(QString.fromUtf8("障碍")))
					self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 1, QTableWidgetItem(QString.fromUtf8("(%d, %d)" %(self.BeginPoint_list[self.commands["beginpoint"]].x_, self.BeginPoint_list[self.commands["beginpoint"]].y_))))
					self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 2, QTableWidgetItem(QString.fromUtf8("(%d, %d)" %(graphs.getBeginPoint()[0][0], graphs.getBeginPoint()[0][1]))))
					self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 3, QTableWidgetItem(QString.fromUtf8("%d" %self.commands["width1"])))	
					has = False
					self.scene1.removeItem(self.BeginPoint_list[self.commands["beginpoint"]])
					for unit in self.BeginPoint_list.values():
						if abs(unit.x_ - graphs.getBeginPoint()[0][0]) <= 2 and abs(unit.y_ - graphs.getBeginPoint()[0][1]) <= 2:
							has = True
							for k in self.BeginPoint_list.keys():
								if self.BeginPoint_list[k] == unit:
									self.scene1.removeItem(self.BeginPoint_list[k])
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
				if command in self.BeginPoint_list.keys():
					self.commands["beginpoint"] = command
					self.state = 1
					self.Information()
				else:
					self.StateLabel.setText(QString.fromUtf8("输入错误，请输入显示为起点的数字"))
			elif self.state == 1:
				if command >= 45:
					self.commands["width1"] = command
					self.state = 2
					self.Information()
				else:
					self.StateLabel.setText(QString.fromUtf8("输入错误，请输入大于等于45的数字"))
					return
			elif self.state == 2:
				if command > 0 and command <= 15:
					self.commands["angle_u"] = command
					self.state = 3
					self.Information()
				else:
					self.StateLabel.setText(QString.fromUtf8("输入错误，请输入大于0小于等于15的数字"))
			elif self.state == 3:
				if command < 1500:
					self.commands["length_u"] = command
					self.state = 4
					self.Information()
				else:
					self.StateLabel.setText(QString.fromUtf8("输入错误，坡道总长不能大于1500"))
			elif self.state == 4:
				if command > 0 and command <= 15:
					self.commands["angle_d"] = command
					self.state = 5
					self.Information()
				else:
					self.StateLabel.setText(QString.fromUtf8("输入错误，请输入大于0小于等于15的数字"))
			elif self.state == 5:
				if command + self.commands["length_u"] < 1500:
					self.commands["length_d"] = command
					self.state = 6
					self.Information()
				else:
					self.StateLabel.setText(QString.fromUtf8("输入错误，坡道总长不能大于1500"))
			elif self.state == 6:
				if command  + self.commands["length_u"] + self.commands["length_d"] < 1500:
					self.commands["length"] = command
					graphs = LineUnit(self.BeginPoint_list[self.commands["beginpoint"]].x_, self.BeginPoint_list[self.commands["beginpoint"]].y_, \
						self.commands["width1"], self.commands["width2"], self.commands["last_slope"][self.commands["beginpoint"]][1], self.commands["x2"],  \
						self.commands["y2"], self.commands["length_u"] + self.commands["length"] + self.commands["length_d"], \
						self.commands["last_slope"][self.commands["beginpoint"]][0], self.commands["length_u"], self.commands["length"])
					for points in graphs.getBeginPoint():
						if points[0] < 0 or points[1] < 0:
							self.StateLabel.setText(QString.fromUtf8("超出边界，绘制失败"))
							self.state = 0
							self.tool = -1
							self.CrossButton.setChecked(False)
							return
					line1 = RampUnit(graphs.getInLine()[0][0], graphs.getInLine()[1][0], graphs.getInLine()[0][1], graphs.getInLine()[1][1], graphs)
					line2 = RampUnit(graphs.getMid1()[0][0], graphs.getMid1()[1][0], graphs.getMid1()[0][1], graphs.getMid1()[1][1], graphs)
					line3 = RampUnit(graphs.getMid2()[0][0], graphs.getMid2()[1][0], graphs.getMid2()[0][1], graphs.getMid2()[1][1], graphs)
					line4 = RampUnit(graphs.getOutLine()[0][0], graphs.getOutLine()[1][0], graphs.getOutLine()[0][1], graphs.getOutLine()[1][1], graphs)
					word1 = BeginPointUnit(QString.fromUtf8(str(self.commands["angle_u"]) + "°上坡"), (graphs.getInLine()[0][0] + graphs.getMid1()[1][0])/2.0, (graphs.getInLine()[0][1] + graphs.getMid1()[1][1])/2, graphs)
					word2 = BeginPointUnit(QString.fromUtf8(str(self.commands["angle_d"]) + "°下坡"), (graphs.getOutLine()[0][0] + graphs.getMid2()[1][0])/2.0, (graphs.getOutLine()[0][1] + graphs.getMid2()[1][1])/2, graphs)
					self.ramp_list.append(line1)
					self.ramp_list.append(line2)
					self.ramp_list.append(line3)
					self.ramp_list.append(line4)
					self.ramp_list.append(word1)
					self.ramp_list.append(word2)
					self.scene1.addItem(line1)
					self.scene1.addItem(line2)
					self.scene1.addItem(line3)
					self.scene1.addItem(line4)
					self.scene1.addItem(word1)
					self.scene1.addItem(word2)
					self.tableWidget.insertRow(self.tableWidget.rowCount())
					self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 0, QTableWidgetItem(QString.fromUtf8("坡道")))
					self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 1, QTableWidgetItem(QString.fromUtf8("(%d, %d)" %(self.BeginPoint_list[self.commands["beginpoint"]].x_, self.BeginPoint_list[self.commands["beginpoint"]].y_))))
					self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 2, QTableWidgetItem(QString.fromUtf8("(%d, %d)" %(graphs.getBeginPoint()[0][0], graphs.getBeginPoint()[0][1]))))
					self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 3, QTableWidgetItem(QString.fromUtf8("%d" %self.commands["width1"])))	
					has = False
					self.scene1.removeItem(self.BeginPoint_list[self.commands["beginpoint"]])
					for unit in self.BeginPoint_list.values():
						if abs(unit.x_ - graphs.getBeginPoint()[0][0]) <= 2 and abs(unit.y_ - graphs.getBeginPoint()[0][1]) <= 2:
							has = True
							for k in self.BeginPoint_list.keys():
								if self.BeginPoint_list[k] == unit:
									self.scene1.removeItem(self.BeginPoint_list[k])
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
					self.RampButton.setChecked(False)
					self.tool = -1

				else:
					self.StateLabel.setText(QString.fromUtf8("输入错误，坡道总长不能大于1500"))				
		elif self.tool == 5:
			if self.state == 0:
				if command in self.BeginPoint_list.keys():
					self.commands["beginpoint"] = command
					self.state = 1
					self.Information()
				else:
					self.StateLabel.setText(QString.fromUtf8("输入错误，请输入显示为起点的数字"))
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
					if self.mode == 0:
						graphs = RightAngleUnit(self.BeginPoint_list[self.commands["beginpoint"]].x_, self.BeginPoint_list[self.commands["beginpoint"]].y_, self.commands["width1"], self.commands["width2"], self.commands["last_slope"][self.commands["beginpoint"]][0], self.commands["last_slope"][self.commands["beginpoint"]][1], self.commands["position"])
						for points in graphs.getBeginPoint():
							if points[0] < 0 or points[1] < 0:
								self.StateLabel.setText(QString.fromUtf8("超出边界，绘制失败"))
								self.state = 0
								self.tool = -1
								self.RightAngleButton.setChecked(False)
								return
						pos = graphs.getPos()
						print "input num:",self.commands["last_slope"][self.commands["beginpoint"]][0], self.commands["position"], [-self.commands["last_slope"][self.commands["beginpoint"]][1][0], -self.commands["last_slope"][self.commands["beginpoint"]][1][1]]
						black1 = BlackAreaUnit(pos[0], self.commands["width1"], self.commands["last_slope"][self.commands["beginpoint"]][0], self.commands["position"], [-self.commands["last_slope"][self.commands["beginpoint"]][1][0], -self.commands["last_slope"][self.commands["beginpoint"]][1][1]], graphs)
						black1.setTransformOriginPoint(QPointF(pos[0][0], pos[0][1]))
						black1.setRotation(black1.getTheta())
						print "input num2:",graphs.getSlope(), self.commands["position"], graphs.getDirection()
						black2 = BlackAreaUnit(pos[1], self.commands["width1"], graphs.getSlope(), self.commands["position"], graphs.getDirection(), graphs)
						black2.setTransformOriginPoint(QPointF(pos[1][0], pos[1][1]))
						black2.setRotation(black2.getTheta())
						self.scene1.addItem(black1)
						self.scene1.addItem(black2)
						self.black_list.append(black1)
						self.black_list.append(black2)
						self.tableWidget.insertRow(self.tableWidget.rowCount())
						self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 0, QTableWidgetItem(QString.fromUtf8("直角弯道")))
						self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 1, QTableWidgetItem(QString.fromUtf8("(%d, %d)" %(self.BeginPoint_list[self.commands["beginpoint"]].x_, self.BeginPoint_list[self.commands["beginpoint"]].y_))))
						self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 2, QTableWidgetItem(QString.fromUtf8("(%d, %d)" %(graphs.getBeginPoint()[0][0], graphs.getBeginPoint()[0][1]))))
						self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 3, QTableWidgetItem(QString.fromUtf8("%d" %self.commands["width1"])))
						has = False
						self.scene1.removeItem(self.BeginPoint_list[self.commands["beginpoint"]])
						for unit in self.BeginPoint_list.values():
							if abs(unit.x_ - graphs.getBeginPoint()[0][0]) <= 2 and abs(unit.y_ - graphs.getBeginPoint()[0][1]) <= 2:
								has = True
								for k in self.BeginPoint_list.keys():
									if self.BeginPoint_list[k] == unit:
										self.scene1.removeItem(self.BeginPoint_list[k])
										del self.BeginPoint_list[k]
										break
								break
						if not has:
							bg = BeginPointUnit("%d" %self.commands["beginpoint"], graphs.getBeginPoint()[0][0], graphs.getBeginPoint()[0][1])
							self.BeginPoint_list[self.commands["beginpoint"]] = bg
							self.scene1.addItem(bg)
							self.last_slope[self.commands["beginpoint"]] = (graphs.getSlope(), graphs.getDirection())
						self.scene1.addItem(graphs)
						self.element_list.append(graphs)
						self.RightAngleButton.setChecked(False)
						self.tool = -1
					else:
						self.commands["width1"] = command
						self.state = 3
						self.Information()
				else:
					self.StateLabel.setText(QString.fromUtf8("输入错误，请输入大于等于45的数字"))
					return
			elif self.state == 3:
				if command >= 90 and command < 180:
					self.commands["arc"] = command
					graphs = AngleUnit(self.BeginPoint_list[self.commands["beginpoint"]].x_, self.BeginPoint_list[self.commands["beginpoint"]].y_, self.commands["width1"], self.commands["width2"], self.commands["last_slope"][self.commands["beginpoint"]][0], self.commands["last_slope"][self.commands["beginpoint"]][1], self.commands["position"], self.commands["arc"])
					print "x1 y1:",self.BeginPoint_list[self.commands["beginpoint"]].x_, self.BeginPoint_list[self.commands["beginpoint"]].y_
					for points in graphs.getBeginPoint():
						if points[0] < 0 or points[1] < 0:
							self.StateLabel.setText(QString.fromUtf8("超出边界，绘制失败"))
							self.state = 0
							self.tool = -1
							self.RightAngleButton.setChecked(False)
							return
					self.tableWidget.insertRow(self.tableWidget.rowCount())
					self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 0, QTableWidgetItem(QString.fromUtf8("折角弯道")))
					self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 1, QTableWidgetItem(QString.fromUtf8("(%d, %d)" %(self.BeginPoint_list[self.commands["beginpoint"]].x_, self.BeginPoint_list[self.commands["beginpoint"]].y_))))
					self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 2, QTableWidgetItem(QString.fromUtf8("(%d, %d)" %(graphs.getBeginPoint()[0][0], graphs.getBeginPoint()[0][1]))))
					self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 3, QTableWidgetItem(QString.fromUtf8("%d" %self.commands["width1"])))
					has = False
					self.scene1.removeItem(self.BeginPoint_list[self.commands["beginpoint"]])
					for unit in self.BeginPoint_list.values():
						if abs(unit.x_ - graphs.getBeginPoint()[0][0]) <= 2 and abs(unit.y_ - graphs.getBeginPoint()[0][1]) <= 2:
							has = True
							for k in self.BeginPoint_list.keys():
								if self.BeginPoint_list[k] == unit:
									self.scene1.removeItem(self.BeginPoint_list[k])
									del self.BeginPoint_list[k]
									break
							break
					if not has:
						bg = BeginPointUnit("%d" %self.commands["beginpoint"], graphs.getBeginPoint()[0][0], graphs.getBeginPoint()[0][1])
						print graphs.getBeginPoint()[0][0], graphs.getBeginPoint()[0][1], graphs.getSlope(), graphs.getDirection()
						self.BeginPoint_list[self.commands["beginpoint"]] = bg
						self.scene1.addItem(bg)
						self.last_slope[self.commands["beginpoint"]] = (graphs.getSlope(), graphs.getDirection())
					self.scene1.addItem(graphs)
					self.element_list.append(graphs)
					self.RightAngleButton.setChecked(False)
					self.tool = -1
				else:
					self.StateLabel.setText(QString.fromUtf8("输入错误，请输入大于等于90且小于180的数字"))
					return
		elif self.tool == 7:
			if command in range(1, len(self.element_list) + 1):
				used_ = False
				if len(self.element_list) > 1:
					start_point = (self.element_list[command - 1].x1, self.element_list[command - 1].y1)
					for bg in self.BeginPoint_list.values():
						if bg.x_ == start_point[0] and bg.y_ == start_point[1]:
							used_ = True
							self.scene1.removeItem(bg)
							for key_ in self.BeginPoint_list.keys():
								if self.BeginPoint_list[key_] == bg:
									del self.BeginPoint_list[key_]
									print "after delete:"
									if len(self.BeginPoint_list.keys()) == 0:
										self.last_slope = None
									break
							break
					last_point = self.element_list[command - 1].getBeginPoint()
					for lp in last_point:
						used = False
						for bg in self.BeginPoint_list.values():
							if bg.x_ == lp[0] and bg.y_ == lp[1]:
								used = True
								self.scene1.removeItem(bg)
								for key_ in self.BeginPoint_list.keys():
									if self.BeginPoint_list[key_] == bg:
										del self.BeginPoint_list[key_]
										print "after delete:"
										if len(self.BeginPoint_list.keys()) == 0:
											self.last_slope = None
										break
								break
						if not used:
							print "I know that not used2"
							for i in range(100):
								if i not in self.BeginPoint_list.keys():
									new_bg = BeginPointUnit("%d" %i, self.element_list[command - 1].getBeginPoint()[last_point.index(lp)][0], self.element_list[command - 1].getBeginPoint()[last_point.index(lp)][1])
									self.BeginPoint_list[i] = new_bg
									self.scene1.addItem(new_bg)
									print "show beginpoint"
									if len(last_point) == 1:
										self.last_slope[i] = (self.element_list[command - 1].getSlope(), [-self.element_list[command - 1].getDirection()[0], -self.element_list[command - 1].getDirection()[1]])
									else:
										self.last_slope[i] = (self.element_list[command - 1].getSlope()[last_point.index(lp)], [-self.element_list[command - 1].getDirection()[last_point.index(lp)][0], -self.element_list[command - 1].getDirection()[last_point.index(lp)][1]])
									break
					if not used_:
						print "I know that not used"
						for i in range(100):
							if i not in self.BeginPoint_list.keys():
								new_bgs = BeginPointUnit(QString("%d" %i), self.element_list[command - 1].x1, self.element_list[command - 1].y1)
								self.BeginPoint_list[i] = new_bgs
								self.scene1.addItem(new_bgs)
								print "show beginpoint"
								self.last_slope[i] = (self.element_list[command - 1].theta, self.element_list[command - 1].direction)
								break

				else:
					for bg in self.BeginPoint_list.values():
						self.scene1.removeItem(bg)
					self.BeginPoint_list = {}
					bg = BeginPointUnit("0", 0, 0)
					self.BeginPoint_list[0] = bg
					self.last_slope = None
				self.tableWidget.removeRow(command - 1)
				delete_list = []
				if isinstance(self.element_list[command - 1], RightAngleUnit):
					for ba in self.black_list:
						print len(self.black_list)
						print "ba:", ba.id == self.element_list[command - 1]
						if ba.id == self.element_list[command - 1]:
							self.scene1.removeItem(ba)
							delete_list.append(ba)
				for ba in delete_list:
					self.black_list.remove(ba)
				delete_list = []
				if isinstance(self.element_list[command - 1], LineUnit):
					for br in self.barrier_list:
						if br.id == self.element_list[command - 1]:
							self.scene1.removeItem(br)
							self.barrier_list.remove(br)
					for rp in self.ramp_list:
						if rp.id == self.element_list[command - 1]:
							self.scene1.removeItem(rp)
							delete_list.append(rp)
				for rp in delete_list:
					self.ramp_list.remove(rp)
				self.scene1.removeItem(self.element_list[command - 1])
				del self.element_list[command - 1]
			else:
				self.StateLabel.setText(QString.fromUtf8("输入错误"))

		else:
			self.StateLabel.setText("")

	@pyqtSlot()
	def on_DeleteButton_clicked(self):
		self.tool = 7
		self.state = 0
		self.Information()

if __name__ == "__main__":
	app = QApplication(sys.argv)
	form = Path()
	form.show()
	app.exec_()