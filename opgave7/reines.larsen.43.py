#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
	Implementation af Integration ved Riemannsummer
"""
from __future__ import division

import pylab
import numpy
import math as m

makePlot = False

def rInt(f, a, b, n):
	u''' Beregner Riemannsummen givet funktionen f, et start punkt, a, et slutpunkt, b,
		og et antal knudepunkter n
		args:
			f - funktion
			a - startpunk
			b - slutpunkt
			n - antal equidistante knudepunkter 
		return:
			Riemannsummen, summen af arealer paa rektangler for hvert interval, 1 ... n'''
	n_list = partition(a, b, n)
	n_list.reverse()
	ti = n_list.pop()
	res = 0.0
	while len(n_list):
		ti_1 = ti
		ti = n_list.pop()
		midres = abs(ti - ti_1)*f(ti)
		if makePlot:
			pylab.plot(ti, midres, 'co', color="g")
		res += midres
	return res

def rIntMid(f, a, b, n):
	u''' Beregner Riemannsummen givet funktionen f, et start punkt, a, et slutpunkt, b,
		og et antal knudepunkter n
		args:
			f - funktion
			a - startpunk
			b - slutpunkt
			n - antal knudepunkter 
		return:
			Riemannsummen, middelsummen af arealet paa rektangler for hvert interval, 1 ... n'''
	n_list = partition(a, b, n)
	n_list.reverse()
	ti = n_list.pop()
	res = 0.0
	while len(n_list):
		ti_1 = ti
		ti = n_list.pop()
		midres = abs(ti - ti_1)*0.5*(f(ti)+f(ti_1))
		if makePlot:
			pylab.plot(ti, midres, 'co', color="r")
		res += midres
	return res

def partition(a, b, n):
	u''' Partitionerer intervallet [a ... b] op i n lige store summer '''
	return [(numpy.float)(n*a + i*(b-a))/float(n) for i in xrange(n+1)]


def f(x):
	''' returnerer Cos(x) '''
	return numpy.cos(x)

def o(x):
	''' returnerer 1/sqrt(2pi)*(x^2/2) '''
	return (1/(numpy.sqrt(2*numpy.pi))*numpy.exp(-1*((x**2)/2)))

def g(x):
	''' returnerer sin(1/x) '''
	return numpy.sin(1/x)

def testPartition():
	''' Tester partition-funktionen '''
	print partition(3, 7 , 10)
	return partition(0, 10 , 10)  == [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]

def testf():
	''' Tester og plotter f(x) '''
	pylab.figure()
	print "rInt, f(x): "+ str(rInt(f, 0, 10, 10))
	print "rIntMid, f(x): "+ str(rIntMid(f, 0, 10, 10))
	x = numpy.array(partition(0,10,100))
	pylab.plot(x, f(x))

def testo():
	''' Tester og plotter o(x) '''
	pylab.figure()
	print "rInt, o(x): "+ str(rInt(o, -10, 10, 20))
	print "rIntMid, o(x): "+ str(rIntMid(o, -10, 10, 20))
	x = numpy.array(partition(-10,10,100))
	pylab.plot(x, o(x))

def testg():
	''' Tester og plotter g(x) '''
	pylab.figure()
	print "rInt, g(x): "+ str(rInt(g, 0.001, 10, 10))
	print "rIntMid, g(x): "+ str(rIntMid(g, 0.001, 10, 10))
	x = numpy.array(partition(0.001,10,100))
	pylab.plot(x, g(x))
	
def testConstant():
	''' tester integralet af en konstant '''
	return abs(rInt(lambda m: 1, 0, 1, 2) - 1.0) < 0.00001 and abs(rIntMid(lambda m: 1, 0, 1, 2) - 1.0) < 0.00001

def test2ndDPoly():
	''' tester integralet af et andengradspolynomium  '''
	return abs(rInt(lambda m: m**2, 0, 1, 10000) - 1/3) < 0.0001 and abs(rIntMid(lambda m: m**2, 0, 1, 1000) - 1/3) < 0.0001
	
def test1OverX():
	''' tester integralet af 1 over x '''
	return abs(rInt(lambda m: 1/m, 1, 2, 100000) - m.log(2)) < 0.0001 and abs(rIntMid(lambda m: 1/m, 1, 2, 100000) - m.log(2)) < 0.0001
	
if __name__ == '__main__':
	print "Partitiontest, works: "+str(testPartition())
	global makePlot
	makePlot = True
	testf()
	testo()
	testg()
	makePlot = False
	print "Integral of a constant, test: "+str(testConstant())
	print "Integral of a 2nd degr poly, test: "+str(test2ndDPoly())
	print "Integral of 1 over x, test: "+str(test1OverX())
	pylab.show()