#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
	opgave 14
"""
from __future__ import division
from beholder import *
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import animation
from bibliotek import *

# Variable
deltaT = 1

def tegnBeholder(i, beholder, plot):
	""" Tegner en beholder og plotter tilhørende partikler """
	plot.cla()
	plt.axes().add_artist(plt.Circle(beholder.centrumPos, beholder.radius, color='b', fill=False))

	xs = []
	ys = []

	for p in beholder.partikler:
		p.step(beholder, deltaT)
		xs.append(p.positionsVektor["x"])
		ys.append(p.positionsVektor["y"])

	frame = plot.plot(xs, ys, 'ro', color="g")

	(x,y) = beholder.centrumPos
	plt.ylim([x-beholder.radius-2,x+beholder.radius+2])
	plt.xlim([x-beholder.radius-2,x+beholder.radius+2])
	plt.axes().set_aspect(1./plt.axes().get_data_ratio())
	return frame

# Main funktion
if __name__ == '__main__':
	beholder = Beholder(5.0, (0.0,0.0), 20, 0.2) # Opret en ny beholder
	fig = plt.figure() # Få fat i figuren
	ax = plt.subplot(111) # Lav et subplot
	ani = animation.FuncAnimation(fig, tegnBeholder, frames=xrange(100), fargs=(beholder, ax), interval=1) # Start animationen
	plt.show() # Vis plottet
