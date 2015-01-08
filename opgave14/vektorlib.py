#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
	Vektor bibliotek
"""
from __future__ import division
import math
from vektor import Vektor

def scale(v, s):
	return Vektor(v["x"]/len(v)*s, v["y"]/len(v)*s)

def vec((p1x, p1y), (p2x, p2y)):
	return Vektor(p2x - p1x, p2y - p1y)

def testScale():
	return scale(Vektor(1,1), 2) == Vektor(2,2)

def testVec():
	return vec((0,0), (1,1)) == Vektor(1,1)

def testAlle():
	if not testVec():
		return "testVec mislykkedes"
	elif not testScale():
		return "testScale mislykkedes"
	else:
		return "Alle tests er vellykket"

if __name__ == '__main__':
	print testAlle()