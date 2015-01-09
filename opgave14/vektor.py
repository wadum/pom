#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
	Vektor
"""
from __future__ import division
import numpy

class Vektor(object):
	def __init__(self, x, y):
		""" Contructor til en Vektor """
		self.__x = float(x)
		self.__y = float(y)
	def __getitem__(self, key):
		""" x og y kan bruges til at indeksere ind i en Vektor """
		if key is "x":
			return self.__x
		elif key is "y":
			return self.__y
		else:
			raise IndexError("%d is not a valid key" % key)
	def lenght(self):
		""" Returnere længden af en Vektor """
		return numpy.sqrt(self["x"] ** 2.0 + self["y"] ** 2.0)
	def __str__(self):
		""" En streng repræsentation af en Vektor """
		return "Vektor(%g, %g)" % (self["x"], self["y"])
	def __eq__(self, otherVektor):
		""" Sammenligning af to Vektore """
		return self["x"] == otherVektor["x"] and self["y"] == otherVektor["y"]
	def __add__(self, otherVektor):
		""" Addition af to Vektore """
		return Vektor(self["x"] + otherVektor["x"], self["y"] + otherVektor["y"])

# Tests
def testGetItem():
	""" Test indeksering ind i en vektor """
	vek = Vektor(1,2)
	return vek["x"] == 1 and vek["y"] == 2

def testLen():
	""" Test af lenght metoden """
	return Vektor(3,4).lenght() == 5

def testStr():
	""" Test af str metoden """
	return str(Vektor(1.2,1)) == "Vektor(1.2, 1)"

def testEq():
	""" Test af eq metoden """
	return Vektor(1,1) == Vektor(1,1) and Vektor(1,1) != Vektor(2,1)

def testAdd():
	""" Test af additionsmetoden """
	return Vektor(1,1) + Vektor(1,1) == Vektor(2,2)

def testAlle():
	""" Kører alle tests """
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

# Main
if __name__ == '__main__':
	print testAlle()