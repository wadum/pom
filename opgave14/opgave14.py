#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
	opgave 14
"""
from __future__ import division
from beholder import *
import matplotlib.pyplot as plt

def tegnPartikel(partikel, plot):
	plot.plot(partikel.positionsVektor["x"], partikel.positionsVektor["y"], 'ro', color="g")

def tegnBeholder(beholder, plot):
	fig = plot.gcf()
	fig.gca().add_artist(plot.Circle(beholder.centrumPos, beholder.radius, color='b', fill=False))
	(x,y) = beholder.centrumPos
	plot.ylim([x-beholder.radius-1,x+beholder.radius+1])
	plot.xlim([x-beholder.radius-1,x+beholder.radius+1])
	plot.axes().set_aspect(1./plot.axes().get_data_ratio())

if __name__ == '__main__':
	beholder = Beholder(5, (0,0), 1000, 0.5)
	for p in beholder.partikler:
		tegnPartikel(p, plt)
	tegnBeholder(beholder, plt)
