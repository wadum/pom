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
	
def getCollisionPointWithContainer(partikel, beholder):
	u""" Forudtaget at partiklen vil kollidere med beholderens væg """
	xDiff = partikel.positionsVektor["x"] - beholder.centrumPos[0]
	yDiff = partikel.positionsVektor["y"] - beholder.centrumPos[1]
	a = partikel.hastighedsVektor["x"]**2 + partikel.hastighedsVektor["y"]**2
	b = 2 * (partikel.hastighedsVektor["x"] * (partikel.positionsVektor["x"] - beholder.centrumPos[0]) + partikel.hastighedsVektor["y"] * (partikel.positionsVektor["y"] - beholder.centrumPos[1]))
	c = xDiff * xDiff + yDiff * yDiff - beholder.radius**2
	disc = b * b - 4 * a * c;
	u = (-b + math.sqrt(disc)) / (2 * a)
	x = partikel.positionsVektor["x"] + partikel.hastighedsVektor["x"] * u
	y = partikel.positionsVektor["y"] + partikel.hastighedsVektor["y"] * u
	return (Vektor(x, y), u)

def getParticleAfterCollision(pc, u, c, partikel):
	v = partikel.hastighedsVektor
	p1 = partikel.positionsVektor
	vp = vec(p1, proj(p1, vec(Vektor(c[0], c[1]), pc)))
	p1m = add(p1, scale(cp, 2*len(vp)))
	v2 = scale(vec(pc, p1m),len(v))
	return (add(pc, scale(v, 1-u)), v2)

	
def willCollide(partikel, beholder):
	u""" Afgør om en partikel vil nå udenfor en beholder ved næste tidsiteration 
	args:
		partikel: partiklen det handler om
		beholder: beholder som indeholder partiklen """
	return len(vec(beholder.centrumPos, step(partikel, deltaT))) > beholder.radius
	
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