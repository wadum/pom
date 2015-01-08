#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
	Bibliotek
"""
from __future__ import division
import math
from vektor import Vektor

def scale(v, s):
	return Vektor(v["x"]/len(v)*s, v["y"]/len(v)*s)

def vec((p1x, p1y), (p2x, p2y)):
	return Vektor(p2x - p1x, p2y - p1y)

def dot(v1, v2):
	return v1["x"] * v2["x"] + v1["y"] * v2["y"]

def step(partikel, deltaT):
	x = partikel.positionsVektor["x"]+deltaT*partikel.hastighedsVektor["x"]
	y = partikel.positionsVektor["y"]+deltaT*partikel.hastighedsVektor["y"]
	return Vektor(x, y)
	
def mul(v, s):
	return Vektor(v["x"] * s, v["y"] * s)

def proj((p1, p2), v):
	return mul(v, dot(Vektor(p1, p2), v)/dot(v,v))

def testScale():
	return scale(Vektor(3,3), 2) == Vektor(1.5,1.5)

def testVec():
	return vec((0,0), (1,1)) == Vektor(1,1)

def testDot():
	return dot(Vektor(2,2), Vektor(2,2)) == 8

def testMul():
	return mul(Vektor(4,4), 2) == Vektor(8,8)

def testProj():
	return proj((4,1), Vektor(2,2)) == Vektor(2.5, 2.5)

def testAlle():
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

if __name__ == '__main__':
	print testAlle()