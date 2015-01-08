#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
	Partikel
"""
from __future__ import division
import math	
from vektor import *
from bibliotek import *

class Partikel(object):
	def __init__(self, positionsVektor, hastighedsVektor):
		""" Constructor til Partikel.

		"""
		self.positionsVektor = positionsVektor
		self.hastighedsVektor = hastighedsVektor
		self.masse = 10**(-23)
		
	def hastighed(self):
		""" Returnerer partiklens hastighed	"""
		return len(self.hastighedsVektor)
	
	def retning(self):
		""" Returnerer partiklens retningsvektor """
		return self.hastighedsVektor;

		
def testHastighed():
	partikel = Partikel(Vektor(0,0), Vektor(3,4))
	return partikel.hastighed() is 5

def testStep():
	partikel = Partikel(Vektor(0,0), Vektor(1,1))
	return step(partikel, 1) == Vektor(1,1)
	
def testAlle():
	if not testHastighed():
		return "testHastighed mislykkedes"
	elif not testStep():
		return "testStep mislykkedes"
	else:
		return "Alle tests er vellykket"
		
if __name__ == '__main__':
	print testAlle()