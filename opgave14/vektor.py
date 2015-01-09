#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
	Vektor
"""
from __future__ import division
import math

class Vektor(object):
	def __init__(self, x, y):
		self.__x = float(x)
		self.__y = float(y)
	def __getitem__(self, key):
		if key is "x":
			return self.__x
		elif key is "y":
			return self.__y
		else:
			raise IndexError("%d is not a valid key" % key)
	def __len__(self):
		return float(math.sqrt(self["x"] ** 2.0 + self["y"] ** 2.0))
	def __str__(self):
		return "Vektor(%g, %g)" % (self["x"], self["y"])
	def __eq__(self, otherVektor):
		return self["x"] == otherVektor["x"] and self["y"] == otherVektor["y"]
	def __add__(self, otherVektor):
		return Vektor(self["x"] + otherVektor["x"], self["y"] + otherVektor["y"])

def testGetItem():
	vek = Vektor(1,2)
	return vek["x"] == 1 and vek["y"] == 2

def testLen():
	return len(Vektor(3,4)) == 5

def testStr():
	return str(Vektor(1.2,1)) == "(1.2, 1)"

def testEq():
	return Vektor(1,1) == Vektor(1,1) and Vektor(1,1) != Vektor(2,1)

def testAdd():
	return Vektor(1,1) + Vektor(1,1) == Vektor(2,2)

def testAlle():
	if not testGetItem():
		return "testGetItem mislykkedes"
	elif not testLen():
		return "testLen mislykkedes"
	elif not testStr():
		return "testStr mislykkedes"
	elif not testEq():
		return "testEq mislykkedes"
	elif not testAdd():
		return "testAdd mislykkedes"
	else:
		return "Alle tests er vellykket"

if __name__ == '__main__':
	print testAlle()