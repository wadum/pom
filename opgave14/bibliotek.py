#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
	Bibliotek
"""
from __future__ import division
import math
from vektor import Vektor

def scale(v, s):
	""" Scalering af en vektor ud fra dens enhedsvektor """
	return Vektor(v["x"]/v.lenght()*s, v["y"]/v.lenght()*s)

def vec((p1x, p1y), (p2x, p2y)):
	""" Omdanner to punkter til en vektor """
	return Vektor(p2x - p1x, p2y - p1y)

def dot(v1, v2):
	""" Beregner prik produktet af to vektore """
	return v1["x"] * v2["x"] + v1["y"] * v2["y"]
	
def mul(v, s):
	""" Multiplicere en vektor og en scalar """
	return Vektor(v["x"] * s, v["y"] * s)

def proj((p1, p2), v):
	""" Projektere et punkt på en vektor """
	return mul(v, dot(Vektor(p1, p2), v)/dot(v,v))


# Tests
def testScale():
	""" Test af skaleringsfunktionen """
	return scale(Vektor(3,3), 2) == Vektor(1.5,1.5)

def testVec():
	""" Test af vec funktionen """
	return vec((0,0), (1,1)) == Vektor(1,1)

def testDot():
	""" Test af prik produktet """
	return dot(Vektor(2,2), Vektor(2,2)) == 8

def testMul():
	""" Test af mulitplication """
	return mul(Vektor(4,4), 2) == Vektor(8,8)

def testProj():
	""" Test af projektion af et punkt på en vektor """
	return proj((4,1), Vektor(2,2)) == Vektor(2.5, 2.5)

def testAlle():
	""" Kører alle tests """
	if not testVec():
		return "testVec mislykkedes"
	elif not testScale():
		return "testScale mislykkedes"
	elif not testDot():
		return "testDot mislykkedes"
	elif not testMul():
		return "testMul mislykkedes"
	elif not testProj():
		return "testProj mislykkedes"
	else:
		return "Alle tests er vellykket"

# Main
if __name__ == '__main__':
	print testAlle()