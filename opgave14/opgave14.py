#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
	opgave 14
"""
from __future__ import division
from beholder import *
import matplotlib.pyplot as plt
import time

def tegnPartikel(partikel, plot):
	plot.plot(partikel.positionsVektor["x"], partikel.positionsVektor["y"], 'ro', color="g")

def tegnBeholder(beholder, plot):
	plt.cla()
	fig = plot.gcf()
	fig.gca().add_artist(plot.Circle(beholder.centrumPos, beholder.radius, color='b', fill=False))

	for p in beholder.partikler:
		tegnPartikel(p, plt)

	(x,y) = beholder.centrumPos
	plot.ylim([x-beholder.radius-1,x+beholder.radius+1])
	plot.xlim([x-beholder.radius-1,x+beholder.radius+1])
	plot.axes().set_aspect(1./plot.axes().get_data_ratio())
	plt.draw()

if __name__ == '__main__':
	beholder = Beholder(5, (0,0), 1000, 0.5)
	plt.ion()
	for i in range(5):
		tegnBeholder(beholder, plt)
		time.sleep(5000)