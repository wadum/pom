#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
	Opgave 13
"""
from __future__ import division
import matplotlib.pyplot as plt

class Dataset:
	def __init__(self):
		self.dataPoints = []

	def __str__(self):
		res = "["
		for dataPoint in self.dataPoints:
			res += str(dataPoint)
		return res + "]"

	def __len__(self):
		return len(self.dataPoints)

	def readDataPoints(self, filePath):
		""" Reads data points from absolute filepath
		args:
			filepath: absolute filepath eg C:\Users\Name\Documents\file.txt
		returns:
			Dataset with points read from file
		"""
		self.__init__()
		with open(filePath, 'r') as f:
			num_lines = 0
			for line in f:
				num_lines += 1
				xy = line.strip().split(",")
				if len(xy) > 2:
					raise ValueError("Input file %s at line %d contains too many numbers." % (filePath, num_lines))
				try:
					self.add(DataPoint(float(xy[0]), float(xy[1])))
				except:
					raise ValueError("Input file %s at line %d is of wrong format." % (filePath, num_lines))
		return self

	def add(self, dataPoint):
		self.dataPoints.append(dataPoint)
		return self

	def addAll(self, dataPoints):
		for dataPoint in dataPoints:
			self.dataPoints.append(dataPoint)
		return self

	def get(self, index):
		return self.dataPoints[index]

	def getAll(self):
		return self.dataPoints

	def x_max(self):
		tmp = self.get(0)
		for dataPoint in self.getAll():
			if tmp.getX() < dataPoint.getX():
				tmp = dataPoint
		return tmp.getX()

	def x_min(self):
		tmp = self.get(0)
		for dataPoint in self.getAll():
			if tmp.getX() > dataPoint.getX():
				tmp = dataPoint
		return tmp.getX()
		
	def plot(self, in_plot, (regx, regy)):
		listx = []
		listy = []
		for dataPoint in self.getAll():
			listx.append(dataPoint.getX())
			listy.append(dataPoint.getY())
		in_plot.plot(listx, listy, 'ro', color="g")
		in_plot.plot(regx, regy, color="r")
		return in_plot

class DataPoint:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __str__(self):
		return "(%s, %s)" % (self.x, self.y)

	def getX(self):
		return self.x

	def getY(self):
		return self.y

class Regression:
	def __init__(self, data):
		self.data = data

	def __x_mid(self):
		res = 0
		for dataPoint in self.data.getAll():
			res += dataPoint.getX()
		return res / len(self.data)

	def __y_mid(self):
		res = 0
		for dataPoint in self.data.getAll():
			res += dataPoint.getY()
		return res / len(self.data)

	def __sak(self):
		x_mid = self.__x_mid()
		res = 0
		for dataPoint in self.data.getAll():
			res += (dataPoint.getX() - x_mid)**2
		return res

	def __sap(self):
		x_mid = self.__x_mid()
		res = 0
		for dataPoint in self.data.getAll():
			res += (dataPoint.getX() - x_mid)*dataPoint.getY()
		return res

	def __a(self):
		return self.__sap()/self.__sak()

	def __f(self, x):
		return self.__a() * (x - self.__x_mid()) + self.__y_mid()

	def linearAnalysis(self):
		return([self.data.x_min(), self.data.x_max()], [self.__f(self.data.x_min()), self.__f(self.data.x_max())])

if __name__ == '__main__':
	dataset = Dataset().readDataPoints("flueaeg.txt")
	print dataset
	regression = Regression(dataset)
	result = regression.linearAnalysis()
	print result
	dataset.plot(plt, result)
	plt.show()