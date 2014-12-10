#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
	Opgave 12
"""
import math
import matplotlib.pyplot as plt
import time


constant = 1.0
h = 1
k = 1

def u(x, t):
	return math.exp(-((x-8-constant*t)**2)/4)

def a(x, t):
	return u(x+h, t)

def b(x, t):
	return 2 * u(x, t)

def c(x, t):
	return u(x-h, t)

def e(x, t):
	return u(x, t-k)

def d(x, t):
	return (constant**2 * k**2 * (a(x,t)+c(x,t)) + b(x,t)*(h**2 - constant**2 * k**2) - e(x,t) * h**2)/h**2

if __name__ == '__main__':
	t = 0.0
	plt.ion()
	while t < 250:
		plt.cla()
		plt.axis([0, 250, 0, 1])
		x = 0.0;
		points = []
		while x < 250:
			points.append((x, u(x,t)))
			x += h
		plt.plot(points, 'co', color="g")
		plt.draw()
		t += k


	# Uncomment the following to get standing waves.

	# plt.figure()
	# plt.suptitle('t = 0')
	# plt.axis([0, 250, 0, 1])
	# points = []
	# x=0
	# for i in range(250):
	# 	points.append((i, u(x, 0.0)))
	# 	x += h
	# plt.plot(points, 'co', color="g")

	# plt.figure()
	# plt.suptitle('t = k')
	# plt.axis([0, 250, 0, 1])
	# points = []
	# x=0
	# for i in range(250):
	# 	points.append((i, u(x, k)))
	# 	x += h
	# plt.plot(points, 'co', color="g")

	# plt.figure()
	# plt.suptitle('halvejs')
	# plt.axis([0, 250, 0, 1])
	# points = []
	# x=0
	# for i in range(250):
	# 	points.append((i, u(x, 117.0)))
	# 	x += h
	# plt.plot(points, 'co', color="g")

	# plt.figure()
	# plt.suptitle('enden')
	# plt.axis([0, 250, 0, 1])
	# points = []
	# x=0
	# for i in range(250):
	# 	points.append((i, u(x, 242.0)))
	# 	x += h
	# plt.plot(points, 'co', color="g")
	# plt.show()

	# Viser midtpunkt og slutpunkt

	# t = 0
	# for j in range(250):
	# 	x = 0
	# 	for i in range(251):
	# 		if (x == 125.0 or x == 250) and u(x,t) == 1:
	# 			print "i = %d, x = %f, t = %d" % (i,u(x,t),t)
	# 		x += h
	# 	t += k