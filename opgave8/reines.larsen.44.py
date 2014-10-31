#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
	Opgave 8
"""
from __future__ import division

import matplotlib.pyplot as plt
from csvImageRead import csvImageRead
import math as m

imageList = csvImageRead("Cameraman.csv")

if not len([y for x in imageList for y in x if y < 0 or y > 255 or len(x) is not len(imageList)]):
	print "Alle værdier ligger imellem 0 og 255 samt højden er ens med bredden."

def gradient(V):
	N = len(V)
	imageListDx = [[0 for i in range(N)] for i in range(N)]
	imageListDy = [[0 for i in range(N)] for i in range(N)]
	for i in range(N):
		for j in range(N):
			if i < N-1:
				(imageListDx[i])[j] = (imageList[i+1])[j] - (imageList[i])[j]
			else:
				(imageListDx[i])[j] = 0.0
			if j < N-1:
				(imageListDy[i])[j] = (imageList[i])[j+1] - (imageList[i])[j]
			else:
				(imageListDy[i])[j] = 0.0
	return (imageListDx, imageListDy)

def gradNorm(V1, V2):
	N = len(V1)
	imageListNorm = [[0 for i in range(N)] for i in range(N)]
	for i in range(N):
		for j in range(N):
			(imageListNorm[i])[j] = m.sqrt((V1[i])[j]**2 + (V2[i])[j]**2)
	return imageListNorm

def divergence(V1, V2):
	N = len(V1)
	imageListDiv = [[0 for i in range(N)] for i in range(N)]
	for i in range(N):
		for j in range(N):
			if i < N-1 and i > 0:
				divx = (V1[i])[j] - (V1[i-1])[j]
			elif i is 0:
				divx = (V1[i])[j]
			elif i is N-1:
				divx = - (V1[i-1])[j]
			if j < N-1 and i > 0:
				divy = (V2[i])[j] - (V2[i])[j-1]
			elif j is 0:
				divy = (V2[i])[j]
			elif j is N-1:
				divy = - (V2[i])[j-1]
			(imageListDiv[i])[j] = divx + divy
	return imageListDiv

# plt.figure()
# plt.imshow(imageList)

# (dx, dy)  = gradient(imageList)

# plt.figure()
# plt.imshow(dx, cmap="Greys_r")

# plt.figure()
# plt.imshow(dy, cmap="Greys_r")

# dnorm = gradNorm(dx, dy)
# plt.figure()
# plt.imshow(dnorm, cmap="Greys_r")

# ddiv = divergence(dx, dy)
# plt.figure()
# plt.imshow(ddiv, cmap="Greys_r")

# plt.show()

y = csvImageRead("CameramanNoisy.csv")
N = len(y)
tau = 0.248
lambd = 0.08
w1 = [[0 for i in range(N)] for i in range(N)]
w2 = [[0 for i in range(N)] for i in range(N)]
divW = divergence(w1, w2)
ylambda = [[i*lambd for i in x] for x in y]
(ylambdaWx, ylambdaWy) = gradient(divW)
for i in range(200):
	(divWx, divWy) = gradient(divW)
	dWx = map(lambda m, n: map(lambda s, z: s+z, m, n), ylambdaWx, divWx)
	dWy = map(lambda m, n: map(lambda s, z: s+z, m, n), ylambdaWy, divWy)
	dWnorm = gradNorm(dWx, dWy)
	w1 = map(lambda m, n: map(lambda s, z: s-tau*z, m, n), w1, dWx)
	w2 = map(lambda m, n: map(lambda s, z: s-tau*z, m, n), w2, dWy)
	w1 = map(lambda m, n: map(lambda s, z: s/(1+tau*z), m, n), w1, dWnorm)
	w2 = map(lambda m, n: map(lambda s, z: s/(1+tau*z), m, n), w2, dWnorm)
	divW = divergence(w1, w2)

x = map(lambda m, n: map(lambda s, z: s-(0.5*z), m, n), y, divW)

plt.figure()
plt.imshow(y)

plt.figure()
plt.imshow(x)

plt.show()