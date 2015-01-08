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

def testScale():
	return scale(Vektor(1,1), 2) == Vektor(2,2)

def testAlle():
	if not testScale():
		return "testGetItem mislykkedes"
	else:
		return "Alle tests er vellykket"

if __name__ == '__main__':
	print testAlle()