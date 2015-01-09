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
		self.masse = 10.0**(-23.0)
		
	def hastighed(self):
		""" Returnerer partiklens hastighed	"""
		return self.hastighedsVektor.lenght()
	
	def retning(self):
		""" Returnerer partiklens retningsvektor """
		return self.hastighedsVektor;


	def willCollide(self, nextStep, beholder):
		u""" Afgør om en partikel vil nå udenfor en beholder ved næste tidsiteration 
		args:
			partikel: partiklen det handler om
			beholder: beholder som indeholder partiklen """
		res = vec(beholder.centrumPos, nextStep).lenght()
		return res > beholder.radius

	def step(self, beholder, deltaT):
		u""" Beregner partiklens position i næste iteration """
		x = self.positionsVektor["x"]+deltaT*self.hastighedsVektor["x"]
		y = self.positionsVektor["y"]+deltaT*self.hastighedsVektor["y"]
		if self.willCollide((x,y), beholder):
			(pc, u) = self.getCollisionPointWithContainer(beholder)
			(p, v) = self.getParticleAfterCollision(pc, u, beholder.centrumPos)
			self.positionsVektor = p
			self.hastighedsVektor = v
		else:
			self.positionsVektor = Vektor(x, y)

	def getCollisionPointWithContainer(self, beholder):
		u""" Forudtaget at partiklen vil kollidere med beholderens væg """
		xDiff = self.positionsVektor["x"] - beholder.centrumPos[0]
		yDiff = self.positionsVektor["y"] - beholder.centrumPos[1]
		a = self.hastighedsVektor["x"]**2.0 + self.hastighedsVektor["y"]**2.0
		b = 2.0 * (self.hastighedsVektor["x"] * (self.positionsVektor["x"] - beholder.centrumPos[0]) + self.hastighedsVektor["y"] * (self.positionsVektor["y"] - beholder.centrumPos[1]))
		c = xDiff * xDiff + yDiff * yDiff - beholder.radius**2.0
		disc = abs(b * b - 4.0 * a * c)
		u = (-b + math.sqrt(disc)) / (2.0 * a)
		x = self.positionsVektor["x"] + self.hastighedsVektor["x"] * u
		y = self.positionsVektor["y"] + self.hastighedsVektor["y"] * u
		return ((x, y), u)

	def getParticleAfterCollision(self, pc, u, c):
		v = self.hastighedsVektor
		p1 = self.positionsVektor
		prj = proj((p1["x"], p1["y"]), vec(c, pc))
		vp = vec((p1["x"], p1["y"]), (prj["x"], prj["y"]))
		pcv = Vektor(pc[0], pc[1])
		p1m = p1 + scale(vp, 2.0*vp.lenght())
		v2 = scale(vec(pc, (p1m["x"], p1m["y"])),v.lenght())
		return (pcv + scale(v, v.lenght()*(1.0-u)), v2)

def testHastighed():
	partikel = Partikel(Vektor(0,0), Vektor(3,4))
	return partikel.hastighed() is 5
	
def testAlle():
	if not testHastighed():
		return "testHastighed mislykkedes"
	else:
		return "Alle tests er vellykket"
		
if __name__ == '__main__':
	print testAlle()