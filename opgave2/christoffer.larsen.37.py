#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Dokumentation for opgave 2"""
from __future__ import division;
import math as m;
import cmath as cm;

### Funktioner
def cmod(z):
	u""" Beregn modulus af et komplekst tal

	args:
		z : Det komplekse tal

	return:
		|z|
	"""
	return m.sqrt(z.real**2 + z.imag**2)

def carg(z):
	u""" Beregn argumentet for et komplekst tal

	args:
		z : Det komplekse tal

	return:
		arg(z)
	"""
	return m.atan2(z.imag, z.real)

def csqrt1(z):
	u""" Beregn den ene kvadratrod, w1, for et komplekst tal.

	args:
		z : Det komplekse tal

	return:
		w1 = sqrt(r)*e^(i*phi/2)

	exception:
		Exception hvis z == 0
	"""
	if z == 0:
		return Exception("z == 0")
	(r, phi) = (cmod(z), carg(z))
	return m.sqrt(r) * m.e**(1j*phi/2)

def csqrt2(z):
	u""" Beregn den ene kvadratrod, w2, for et komplekst tal.

	args:
		z : Det komplekse tal

	return:
		w2 = sqrt(r)*e^(i*(phi+2*pi)/2)

	exception:
		Exception hvis z == 0
	"""
	if z == 0:
		return Exception("z == 0")
	(r, phi) = (cmod(z), carg(z))
	return m.sqrt(r) * (m.cos((phi+2*m.pi)/2) + m.sin((phi+2*m.pi)/2)*1j)

def polyrod1(a, b, c):
	u""" Beregn den ene rod, x1, for et komplekst polynomium ax^2+bx+c = 0.

	args:
		Koefficienter for et polynomium paa formen ax^2+bx+c = 0. Dvs. a, b og c.

	return:
		x1 = (-b + csqrt1(b**2 - 4*a*c))/(2*a)
	"""
	return (-b + csqrt1(b**2 - 4*a*c))/(2*a)

def polyrod2(a, b, c):
	u""" Beregn den ene rod, x1, for et komplekst polynomium ax^2+bx+c = 0.

	args:
		Koefficienter for et polynomium paa formen ax^2+bx+c = 0. Dvs. a, b og c.

	return:
		x1 = (-b + csqrt2(b**2 - 4*a*c))/(2*a)
	"""
	return (-b + csqrt2(b**2 - 4*a*c))/(2*a)

def polyrod(a, b, c):
	u""" Beregner begge rodder, x1 og x2, i et polynomium, ax^2+bx+c = 0, ud fra omskrivningen fra Opgave 1.

	Denne funktion bruges som reference for at kunne teste polyrod1 og polyrod2.

	For at sikre korrekthed bruges sqrt() fra cmath.

	args:
		Koefficienter for et polynomium paa formen ax^2+bx+c = 0. Dvs. a, b og c.

	return:
		(x1, x2)
	"""
	if b <= 0:
		x1 = (-b + cm.sqrt(b*b - 4*a*c))/(2*a)
	else:
		x1 = (-b - cm.sqrt(b*b - 4*a*c))/(2*a)
	if abs(x1) > 0.00000001:
		x2 = (c/a)/x1
	else:
		x2 = -b / a
	return x1, x2


### Tests
def testCmod():
	u""" Unit test af cmod

	"""
	return cmod(complex(-1.0, 0.0)) == abs(complex(-1.0, 0.0))

def testCarg():
	u""" Unit test af carg

	"""
	return carg(complex(1,1)) == cm.phase(complex(1,1))

def testCsqrt():
	u""" Unit test af csqrt1

	"""
	return abs(csqrt1(complex(1,1)) - cm.sqrt(complex(1,1))) < 0.000000001

def testPolyrod():
	u""" Unit test af polyrod1 og polyrod2

	"""
	(x1, x2) = polyrod(1.0,1.0,1.0)
	return abs(polyrod2(1.0,1.0,1.0) - x1) < 0.0000000001 and abs(polyrod1(1.0,1.0,1.0) - x2) < 0.0000000001

def testAlle():
	u""" Korer alle tests

	"""
	if not testCmod():
		print "testCmod fejlede"
	if not testCarg():
		print "testCarg fejlede"
	if not testCsqrt():
		print "testCsqrt fejlede"
	if not testPolyrod():
		print "testPolyrod fejlede"
	if testCmod() == testCarg() == testCsqrt() == testPolyrod():
		print "Alle tests returnede vellykket."

### Main
if __name__ == "__main__":
	testAlle()