#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
	Vektor
"""
from __future__ import division

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

def testGetItem():
	vek = Vektor(1,2)
	return vek["x"] is 1 and vek["y"] is 2

def testAll():
	if not testGetItem():
		return "testGetItem mislykkedes"
	if testGetItem():
		return "Alle tests er vellykket"

if __name__ == '__main__':
	print testAll()