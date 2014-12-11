#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
	Opgave 13
"""
from __future__ import division
import os.path
import matplotlib.pyplot as plt

class Dataset:
	def __init__(self):
		""" Constructor til Dataset.

		"""
		self.dataPoints = []

	def __str__(self):
		""" Returns a string representation of the Dataset

		"""
		res = "["
		for dataPoint in self.dataPoints:
			res += str(dataPoint)
		return res + "]"

	def __len__(self):
		""" Returns the length of the Dataset

		"""
		return len(self.dataPoints)

	def readDataPoints(self, filePath):
		""" Reads data points from absolute filepath
		args:
			filepath: absolute filepath eg C:\Users\Name\Documents\file.txt
		returns:
			Dataset with points read from file
		"""
		self.__init__()
		if not os.path.isfile(filePath):
			raise IOError("File %s not found." % filePath)
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

	def __getitem__(self, index):
		""" Returns the DataPoint at Dataset[index]

		"""
		return self.dataPoints[index]

	def add(self, dataPoint):
		""" Adds a single DataPoint to the Dataset.

		"""
		self.dataPoints.append(dataPoint)
		return self

	def addAll(self, dataPoints):
		""" Adds a collection of DataPoint to the Dataset.

		"""
		for dataPoint in dataPoints:
			self.dataPoints.append(dataPoint)
		return self

	def getAll(self):
		""" Returns all DataPoint in the Dataset

		"""
		return self.dataPoints

	def x_max(self):
		""" Returns the largest x value in the Dataset.

		"""
		tmp = self[0]
		for dataPoint in self.getAll():
			if tmp.getX() < dataPoint.getX():
				tmp = dataPoint
		return tmp.getX()

	def x_min(self):
		""" Returns the smallest x value in the Dataset.

		"""
		tmp = self[0]
		for dataPoint in self.getAll():
			if tmp.getX() > dataPoint.getX():
				tmp = dataPoint
		return tmp.getX()
		
	def plot(self, in_plot, (regx, regy)):
		""" Plots this Dataset with the output of linearAnalysis.

			args:
				in_plot: The plot to add points to.
				(regx, regy):
					regx: List of x-values from a linearAnalysis.
					regy: List of y-values from a linearAnalysis.
		"""
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
		""" Constructor to DataPoint """
		self.x = x
		self.y = y

	def __str__(self):
		""" A stringrepresentation of the class DataPoint """
		return "(%s, %s)" % (self.x, self.y)

	def getX(self):
		""" 
		returns:
			x
		"""
		return self.x

	def getY(self):
		""" 
		returns:
			y
		"""
		return self.y

class Regression:
	def __init__(self, data):
		""" Constructor to Regression """
		if isinstance(data, Dataset):
			self.data = data
		else:
			raise TypeError("data is not a Dataset.")

	def __x_mid(self):
		""" 
		returns:
			Average value of all x-values 
		"""
		res = 0
		for dataPoint in self.data.getAll():
			res += dataPoint.getX()
		return res / len(self.data)

	def __y_mid(self):
		""" 
		returns:
			Average value of all y-values 
		"""
		res = 0
		for dataPoint in self.data.getAll():
			res += dataPoint.getY()
		return res / len(self.data)

	def __sak(self):
		""" 
		returns:
			Sum of quadrants of deviations
		"""
		x_mid = self.__x_mid()
		res = 0
		for dataPoint in self.data.getAll():
			res += (dataPoint.getX() - x_mid)**2
		return res

	def __sap(self):
		""" 
		returns:
			Sum of products of deviations
		"""
		x_mid = self.__x_mid()
		res = 0
		for dataPoint in self.data.getAll():
			res += (dataPoint.getX() - x_mid)*dataPoint.getY()
		return res

	def __a(self):
		""" 
		returns:
			sap/sak 
		"""
		return self.__sap()/self.__sak()

	def __f(self, x):
		""" 
		returns:
			a*(x-x_mid)+y_mid
		"""
		return self.__a() * (x - self.__x_mid()) + self.__y_mid()

	def linearAnalysis(self):
		""" Performs a linear regressionanalysis on the set of points in data 
		returns:
			 ([xmin, xmax], [f(xmin), f(xmax)])"""
		if len(self.data) < 2:
			raise RuntimeError("Too few arguments in dataset")
		return([self.data.x_min(), self.data.x_max()], [self.__f(self.data.x_min()), self.__f(self.data.x_max())])

if __name__ == '__main__':
	# File not exist
	print "Invalid filename:"
	try:
		dataset = Dataset().readDataPoints("sys32.deleteme")
	except IOError as ioe:
		print "Test succeeded"
	else:
		print "Test failed"
	
	# Wrong fileformat
	print "Invalid format in file:"
	try:
		dataset = Dataset().readDataPoints("flueaeg_fformat.txt")
	except ValueError as ve:
		print "Test succeeded"
	else:
		print "Test failed"
		
	# Too few datapoints in the set
	print "Too few datapoints in the set:"
	try:
		dataset = Dataset().addAll([])
		Regression(dataset).linearAnalysis()
	except RuntimeError as ve:
		print "Test succeeded"
	else:
		print "Test failed"
		
	try:
		dataset = Dataset().add(DataPoint(0.0, 0.0))
		Regression(dataset).linearAnalysis()
	except RuntimeError as ve:
		print "Test succeeded"
	else:
		print "Test failed"
		
	try:
		dataset = Dataset().addAll([DataPoint(0.0, 0.0),DataPoint(1.0, 1.0)])
		Regression(dataset).linearAnalysis()
	except RuntimeError as ve:
		print "Test failed"
	else:
		print "Test succeeded"


	# Test type checking of Regression
	print "Correct type as input to Regression constructor:"
	try:
		Regression(Dataset())
	except:
		print "Test failed"
	else:
		print "Test succeeded"

	try:
		Regression("")
	except TypeError as te:
		print "Test succeeded"
	else:
		print "Test failed"

	# Correct
	dataset = Dataset().readDataPoints("flueaeg.txt")
	dataset.plot(plt, Regression(dataset).linearAnalysis())
	plt.xlabel('x')
	plt.ylabel('y')
	plt.title('Linear regressionanalysis of dataset in flueaeg.txt')
	plt.show()