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
import time
from bibliotek import *

# Variable
deltaT = 1

def drawfigure(i, beholder, plot):
	plot.cla()
	plt.axes().add_artist(plt.Circle(beholder.centrumPos, beholder.radius, color='b', fill=False))

	xs = []
	ys = []

	for p in beholder.partikler:
		p.positionsVektor = step(p, deltaT)
		xs.append(p.positionsVektor["x"])
		ys.append(p.positionsVektor["y"])

	frame = plot.plot(xs, ys, 'ro', color="g")

	(x,y) = beholder.centrumPos
	plt.ylim([x-beholder.radius-1,x+beholder.radius+1])
	plt.xlim([x-beholder.radius-1,x+beholder.radius+1])
	plt.axes().set_aspect(1./plt.axes().get_data_ratio())
	return frame

def willCollide(partikel, beholder):
	u""" Afgør om en partikel vil nå udenfor en beholder ved næste tidsiteration 
	args:
		partikel: partiklen det handler om
		beholder: beholder som indeholder partiklen """
	return len(vec(beholder.centrumPos, step(partikel, deltaT))) > beholder.radius
	

if __name__ == '__main__':
	beholder = Beholder(5, (0,0), 100, 0.5)
	fig = plt.figure()
	ax = plt.subplot(111)
	plt.text(4, 1, "hey", ha='left', rotation=15)
	ani = animation.FuncAnimation(fig, drawfigure, frames=xrange(100), fargs=(beholder, ax), interval=1)
	plt.show()
