#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
	Opgave 8
"""
from __future__ import division

import matplotlib.pyplot as plt
from csvImageRead import csvImageRead
import math as m

# Indlæs billedet Cameraman
imageList = csvImageRead("Cameraman.csv")

# Afprøv at samtlige værdier i Cameraman ligger imellem 0 og 255 samt at bredden er det samme som højden
if not len([y for x in imageList for y in x if y < 0 or y > 255 or len(x) is not len(imageList)]):
	print "Alle værdier ligger imellem 0 og 255 samt højden er ens med bredden."

def gradient(V):
	""" Beregn gradienten af billedet V

	args:
		V - billedet
	res:
		(vDx, vDy) - de to gradient billeder
	"""
	N = len(V)
	vDx = [[0 for i in range(N)] for i in range(N)]
	vDy = [[0 for i in range(N)] for i in range(N)]
	for i in range(N):
		for j in range(N):
			if i < N-1:
				(vDx[i])[j] = (V[i+1])[j] - (V[i])[j]
			else:
				(vDx[i])[j] = 0.0
			if j < N-1:
				(vDy[i])[j] = (V[i])[j+1] - (V[i])[j]
			else:
				(vDy[i])[j] = 0.0
	return (vDx, vDy)

def gradNorm(V1, V2):
	""" Beregner normen af en gradient

	args:
		V1 - x komponenten af gradienten
		V2 - y komponenten af gradienten
	res:
		VNorm
	"""
	N = len(V1)
	VNorm = [[0 for i in range(N)] for i in range(N)]
	for i in range(N):
		for j in range(N):
			(VNorm[i])[j] = m.sqrt((V1[i])[j]**2 + (V2[i])[j]**2)
	return VNorm

def divergence(V1, V2):
	""" Beregner divergencen af en gradient

	args:
		V1 - x komponenten af gradienten
		V2 - y komponenten af gradienten
	res:
		VDiv
	"""
	N = len(V1)
	VDiv = [[0 for i in range(N)] for i in range(N)]
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
			(VDiv[i])[j] = divx + divy
	return VDiv

# Plot Cameraman
plt.figure()
plt.title("Opgave a - plot Cameraman")
plt.imshow(imageList, cmap="Greys_r")

# Beregn gradienten af Cameraman
(dx, dy)  = gradient(imageList)

# Plot gradientbillederne for Cameraman
plt.figure()
plt.title("Opgave b - x komponenten af gradienten")
plt.imshow(dx, cmap="Greys_r")

plt.figure()
plt.title("Opgave b - y komponenten af gradienten")
plt.imshow(dy, cmap="Greys_r")

#Beregn normen
dnorm = gradNorm(dx, dy)

# Plot normen
plt.figure()
plt.title("Opgave c - normen af gradienten")
plt.imshow(dnorm, cmap="Greys_r")

# Beregn divergencen
ddiv = divergence(dx, dy)

# Plot divergencen
plt.figure()
plt.title("Ogpave d - divergencen af gradienten")
plt.imshow(ddiv, cmap="Greys_r")

def __itera__(f, a, b):
	""" Hjælpefunktion

	Udfører f(a(i,j), b(i,j)) - equivalent til map(lambda x, y: map(f, x, y), a, b)

	"""
	N = len(a)
	res = [[0 for i in range(N)] for i in range(N)]
	for i in range(N):
		for j in range(N):
			(res[i])[j] = f((a[i])[j], (b[i])[j])
	return res

# Indlæs det støjfyldte billed
y = csvImageRead("CameramanNoisy.csv")
N = len(y)

# Initialiser variabler
tau = 0.248
lambd = 0.08
w1 = [[0 for x in range(N)] for i in range(N)]
w2 = [[0 for x in range(N)] for i in range(N)]
divW = divergence(w1, w2)
ylambda = [[i*lambd for i in x] for x in y]
(ylambdaWx, ylambdaWy) = gradient(ylambda)
y9 = list()

# Udfør glatningsprocessen
for i in range(200):
	(dWx, dWy) = gradient(__itera__(lambda m, n: m-n, ylambda, divW))
	dWnorm = gradNorm(dWx, dWy)
	w1 = __itera__(lambda s, z: s-tau*z, w1, dWx)
	w2 = __itera__(lambda s, z: s-tau*z, w2, dWy)
	w1 = __itera__(lambda s, z: s/(1+tau*z), w1, dWnorm)
	w2 = __itera__(lambda s, z: s/(1+tau*z), w2, dWnorm)
	divW = divergence(w1, w2)
	y9.append(m.fsum(reduce(lambda s, x: s + x, __itera__(lambda v, w: (v-w)**2, w1, w2))))

x = __itera__(lambda s, z: s-((1/lambd)*z), y, divW)

# Vis billedet før og efter glatningsprocessen
plt.figure()
plt.title("Opgave e - stoejfyldt Cameraman")
plt.imshow(y, cmap="Greys_r")

plt.figure()
plt.title("Opgave e - stoejreduceret Cameraman")
plt.imshow(x, cmap="Greys_r")

# Vis grafen til opgave f
plt.figure()
plt.title("Opgave f")
plt.plot(y9)

plt.show()