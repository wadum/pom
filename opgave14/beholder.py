#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
	Beholder
"""
from __future__ import division
import math	
from vektor import *
from vektorlib import *
import random as rndm
from partikel import *

class Beholder(object):
	def __init__(self, radius, centrumPos, antalPartikler):
		""" Constructor til Beholder.
		args:
			radius: beholderens radius
			centrumPos: beholderens centrumPos. Default er (0,0)
			antalPartikler: antal partikler der skal instantieres i beholderen
		"""
		self.radius = radius
		self.centrumPos = centrumPos
		self.partikler = self.genererPartikler(antalPartikler)

	def genererPartikler(self, antalPartikler):
		""" Generere en mængde partikler i beholderen.
		args:
			antalPartikler: Antal af partikler der skal genereres tilfældigt
		"""
		partikler = []
		for x in range(0, antalPartikler):
			t = 2*math.pi*rndm.random()
			u = rndm.random()+rndm.random()
			r = u
			if u>1:
				r = 2-u 
			p = Vektor(r*math.cos(t), r*math.sin(t))
			v = Vektor(0,0)
			partikler.append(Partikel(p, v))
		return partikler
	
def testPartiklersPositionIBeholder():
	""" Tester om de genererede partikler er indeholdt i beholderen
		eller om de er blevet genereret ude for beholderen.
		Vi antager her at beholderen er en cirkel """
	beholder = Beholder(3, (0,0), 300)
	for p in beholder.partikler:
		x = p.positionsVektor["x"]
		y = p.positionsVektor["y"]
		if (x - beholder.centrumPos[0])**2 + (y - beholder.centrumPos[1])**2 > beholder.radius**2 :
			return False
	return True
	
def testAlle():
	if not testPartiklersPositionIBeholder():
		return "testPartiklersPositionIBeholder mislykkedes"
	else:
		return "Alle tests er vellykket"
		
if __name__ == '__main__':
	print testAlle()