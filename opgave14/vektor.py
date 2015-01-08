#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
	Vektor
"""
from __future__ import division
import math

class Vektor(object):
	def __init__(self, x, y):
		self.__x = x
		self.__y = y
	def __getitem__(self, key):
		if key is "x":
			return self.__x
		elif key is "y":
			return self.__y
		else:
			raise IndexError("%d is not a valid key" % key)
	def __len__(self):
		return math.sqrt(self.__x ** 2 + self.__y ** 2)
	def __str__(self):
		return "(%g, %g)" % (self.__x, self.__y)

def testGetItem():
	vek = Vektor(1,2)
	return vek["x"] == 1 and vek["y"] == 2

def testLen():
	return len(Vektor(3,4)) == 5

def testStr():
	return str(Vektor(1.2,1)) == "(1.2, 1)"

def testAlle():
	if not testGetItem():
		return "testGetItem mislykkedes"
	if not testLen():
		return "testLen mislykkedes"
	if not testStr():
		return "testStr mislykkedes"
	if testGetItem() and testLen() and testStr():
		return "Alle tests er vellykket"

if __name__ == '__main__':
	print testAlle()