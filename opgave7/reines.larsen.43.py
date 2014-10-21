#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
	Implementation af Integration ved Riemannsummer
"""
from __future__ import division

import pylab
import numpy

def rInt(f, a, b, n):
	n_list = partition(a, b, n)
	n_list.reverse()
	ti = n_list.pop()
	res = 0.0
	while len(n_list):
		ti_1 = ti
		ti = n_list.pop()
		midres = abs(ti - ti_1)*f(ti)
		pylab.plot(ti, midres, 'co', color="g")
		res += midres
	return res

def rIntMid(f, a, b, n):
	n_list = partition(a, b, n)
	n_list.reverse()
	ti = n_list.pop()
	res = 0.0
	while len(n_list):
		ti_1 = ti
		ti = n_list.pop()
		midres = abs(ti - ti_1)*0.5*(f(ti)+f(ti_1))
		pylab.plot(ti, midres, 'co', color="r")
		res += midres
	return res

def partition(a, b, n):
	frc = (b-a)/n
	lst = [float(a)]
	for x in range(n):
		lst.append(float(lst[-1])+frc)
	return lst


def f(x):
	return numpy.cos(x)

def o(x):
	return (1/(numpy.sqrt(2*numpy.pi))*numpy.exp(-1*((x**2)/2)))

def g(x):
	return numpy.sin(1/x)

def testPartition():
	return partition(0, 10 , 10)  == [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]

def testf():
	pylab.figure()
	print rInt(f, 0, 10, 10)
	print rIntMid(f, 0, 10, 10)
	x = numpy.linspace(0,10,100)
	pylab.plot(x, f(x))

def testo():
	pylab.figure()
	print rInt(o, -10, 10, 20)
	print rIntMid(o, -10, 10, 20)
	x = numpy.linspace(-10,10,100)
	pylab.plot(x, o(x))

def testg():
	pylab.figure()
	print rInt(g, 0.001, 10, 10)
	print rIntMid(g, 0.001, 10, 10)
	x = numpy.linspace(0.001,10,100)
	pylab.plot(x, g(x))

if __name__ == '__main__':
	print testPartition()
	testf()
	testo()
	testg()
	pylab.show()