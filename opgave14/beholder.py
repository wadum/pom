#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
	Beholder
"""
from __future__ import division
import math	
from vektor import *
from vektorlib import *

class Beholder(object):
	def __init__(self, radius, centrumPos, partikler):
		""" Constructor til Beholder.
		args:
			radius: beholderens radius
			centrumPos: beholderens centrumPos. Default er (0,0)
			partikler: antal partikler der skal instantieres i beholderen
		"""
		self.radius = radius
		self.centrumPos = centrumPos
		self.partikler = genererPartikler(partikler)
		
	def genererPartikler(self, partikler):
		""" Generere en mængde partikler i beholderen.
		args:
			partikler: Antal af partikler der skal genereres tilfældigt
		"""
		
if __name__ == '__main__':
	print testAlle()