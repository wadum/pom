#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
	Implementation af Integration ved Riemannsummer
"""
from __future__ import division

import pylab
import numpy

def rInt(f, a, b, n):
	u''' Beregner Riemannsummen givet funktionen f, et start punkt, a, et slutpunkt, b,
		og et antal knudepunkter n
		args:
			f - funktion
			a - startpunk
			b - slutpunkt
			n - antal equidistante knudepunkter 
		return:
			Riemannsummen, summen af arealer på rektangler for hvert interval, 1 ... n'''
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
	u''' Beregner Riemannsummen givet funktionen f, et start punkt, a, et slutpunkt, b,
		og et antal knudepunkter n
		args:
			f - funktion
			a - startpunk
			b - slutpunkt
			n - antal knudepunkter 
		return:
			Riemannsummen, middelsummen af arealet på rektangler for hvert interval, 1 ... n'''
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
	u''' Partitionerer intervallet [a ... b] op i n lige store summer '''
	frc = (b-a)/n
	lst = [float(a)]
	for x in range(n):
		lst.append(float(lst[-1])+frc)
	return lst


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
	return partition(0, 10 , 10)  == [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]

def testf():
	''' Tester og plotter f(x) '''
	pylab.figure()
	print rInt(f, 0, 10, 10)
	print rIntMid(f, 0, 10, 10)
	x = numpy.linspace(0,10,100)
	pylab.plot(x, f(x))

def testo():
	''' Tester og plotter o(x) '''
	pylab.figure()
	print rInt(o, -10, 10, 20)
	print rIntMid(o, -10, 10, 20)
	x = numpy.linspace(-10,10,100)
	pylab.plot(x, o(x))

def testg():
	''' Tester og plotter g(x) '''
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