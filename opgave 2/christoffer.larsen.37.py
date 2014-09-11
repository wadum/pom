# -*- coding: utf-8 -*-
from __future__ import division;
import math as m;
import cmath as cm;

def cmod(z):
	return m.sqrt(z.real**2 + z.imag**2)

def carg(z):
	return m.atan2(z.imag, z.real)

def csqrt1(z):
	(r, phi) = (cmod(z), carg(z))
	return m.sqrt(r) * m.e**(1j*phi/2)

def csqrt2(z):
	(r, phi) = (cmod(z), carg(z))
	return m.sqrt(r) * (m.cos((phi+2*m.pi)/2) + m.sin((phi+2*m.pi)/2)*1j)

def polyrod1(a, b, c):
	return (-b + csqrt1(b**2 - 4*a*c))/(2*a)

def polyrod2(a, b, c):
	return (-b + csqrt2(b**2 - 4*a*c))/(2*a)

def polyrod(a, b, c):
	if b <= 0:
		x1 = (-b + csqrt1(b*b - 4*a*c))/(2*a)
	else:
		x1 = (-b - csqrt1(b*b - 4*a*c))/(2*a)
	if abs(x1) > 0.00000001:
		x2 = (c/a)/x1
	else:
		x2 = -b / a
	return x1, x2

print cmod(complex(-1.0, 0.0)) == abs(complex(-1.0, 0.0))
print carg(complex(1,1)) == cm.phase(complex(1,1))
print abs(csqrt1(complex(1,1)) - cm.sqrt(complex(1,1))) < 0.000000001
(x1, x2) = polyrod(1.0,1.0,1.0)
print abs(polyrod2(1.0,1.0,1.0) - x1) < 0.0000000001
print abs(polyrod1(1.0,1.0,1.0) - x2) < 0.0000000001