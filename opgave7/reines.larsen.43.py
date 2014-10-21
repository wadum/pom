#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
	Implementation af Integration ved Riemannsummer
"""
from __future__ import division
import math as m

def rInt(f, a, b, n):
	n_list = partition(a, b, n)
	n_list.reverse()
	ti = n_list.pop()
	res = 0.0
	while len(n_list):
		ti_1 = ti
		ti = n_list.pop()
		res += abs(ti - ti_1)*f(ti)
	return res

def rIntMid(f, a, b, n):
	n_list = partition(a, b, n)
	n_list.reverse()
	ti = n_list.pop()
	res = 0.0
	while len(n_list):
		ti_1 = ti
		ti = n_list.pop()
		res += abs(ti - ti_1)*0.5*(f(ti)+f(ti_1))
	return res

def partition(a, b, n):
	frc = (b-a)/n
	lst = [float(a)]
	for x in range(n):
		lst.append(float(lst[-1])+frc)
	return lst


def f(x):
	return m.cos(x)

def testPartition():
	print partition(0, 10 , 10)

if __name__ == '__main__':
	testPartition()
	print rInt(f, 0, 10, 1000)
	print rIntMid(f, 0, 10, 1000)