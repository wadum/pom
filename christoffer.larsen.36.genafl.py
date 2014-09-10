# -*- coding: utf-8 -*-
from __future__ import division;
import math as m;

def findRodder(a, b, c):
	u""" Beregn rødder i et andengradspolynomium
	
	Udregner rødderne i et andengradspolynomium med formen
	ax²+bx+c=0
	
	Returnere x1 og x2.
	"""
	if b <= 0:
		x1 = ((0-b) + m.sqrt(b*b - 4*a*c))/(2*a)
	else:
		x1 = ((0-b) - m.sqrt(b*b - 4*a*c))/(2*a)
	if abs(x1) > 0.00000001:
		x2 = (c/a)/x1
	else:
		x2 = -b / a
	return x1, x2

def getInputNumber(message):
	try:
		number = float(raw_input(message))
	except ValueError:
		print "Fejl i indtastningen. Angiv venligst et tal i base 10."
		getInputNumber(message)
	return number

def main():
	u""" Beregn rødder i et andengradspolynomium
	
	Lader brugeren indtaste koefficienterne på et andengradspolynomie.
	
	Printer rødderne hvis de findes.
	"""
	a = getInputNumber('Angiv a: ')
	b = getInputNumber('Angiv b: ')
	c = getInputNumber('Angiv c: ')
	try:
		(x1, x2) = findRodder(a, b, c)
		print "Rødderne for andengradspolynomiumet %fx²+%fb+%f=0 er \n\t x1 = %f, x2 = %f" % (a, b, c, x1, x2)
	except ZeroDivisionError:
		print "For at være et andengradspolynomium skal a være forskellig fra 0"
	except ValueError:
		print "D < 0, så der findes ingen løsning."

if __name__ == "__main__":
	main()
