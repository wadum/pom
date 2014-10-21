#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Implementation af spillet Life. 

Vi har valgt at repræsenterer spillet med en liste af lister. 
Spillepladen har en statisk størrelse, men fungerer som en torus. 

Christoffer Wadum Larsen - fpj784
Toke Emil Heldbo Reines - bkx591
"""
from kursusuge6modul import *

# Konstanter
width = 40;
height = 40;

# Funktioner
def foerste():
	""" Initialiserer spillet Life med parametre fra opgaven.

	Return:
		(i_min, i_max, j_min, j_max)
	"""
	global nextBoard
	nextBoard = newBoard()
	createLifeForm([(10,6), (10,7), (10,8), (9,8), (8,7)])
	return (0, width, 0, height)
	
def naeste():
	""" Beregner næste diskrete skridt.

	Størrelsen af spillepladen er statisk.
	Vi har i stedet valgt overvejelse (c) fra opgaveteksten
	om at lade spillepladen være en torus.

	Return:
		(i_min, i_max, j_min, j_max)
	"""
	global nextBoard, prevBoard
	prevBoard = nextBoard
	nextBoard = newBoard()
	for x in range(width):
		for y in range(height):
			nextBoard[x][y] = newState(getNeighborsAlive(x,y), (x,y))
	return (0, width, 0, height)

def levende(i, j):
	""" Returnerer om cellen på positionen i, j er levende eller død.

	Args:
		i
		j

	Return:
		True | False
	"""
	return nextBoard[i][j]

# Hjælpefunktioner
def newBoard():
	""" Initialiserer et nyt board med alle værdier sat til False. """
	return [[False for i in range(width)] for i in range(height)]

def getNeighborsAlive(i, j):
	""" Beregner antallet af levende celler omkring cellen i (i,j). """
	result = 0
	for n in range(-1, 2):
		for m in range(-1, 2):
			if m == 0 and n == 0:
				continue
			if prevBoard[(i+n)%width][(j+m)%height]:
				result += 1
	return result

def newState(neighborsAlive, (x,y)):
	""" Beregner en celles nye state ud fra reglerne i Life. """
	if neighborsAlive == 2:
		return prevBoard[x][y]
	if neighborsAlive == 3:
		return True
	return False

def createLifeForm(liste):
	""" Initialiserer levende celler ud fra en liste af koordinater. """
	global nextBoard
	for (x,y) in liste:
		nextBoard[x][y] = True

# Test funktioner
def validateBoard(liste):
	""" Validerer en spilleplade op imod en liste af koordinater der indeholder alle levende celler. """
	for x in range(width):
		for y in range(height):
			if (x,y) in liste:
				if not nextBoard[x][y]:
					return False
			elif nextBoard[x][y]:
				return False
	return True

def testFoerste():
	""" Test om funktionen første returnerer den korrekte spilleplade. """
	foerste()
	return validateBoard([(10,6), (10,7), (10,8), (9,8), (8,7)])

def testLevende():
	""" Test om funktionen levende returnerer korrekte værdier. """
	foerste()
	return levende(10, 6) and not levende(11, 6)

def testNaeste():
	""" Test om naeste returnerer den korrekte spilleplade. """
	foerste()
	naeste()
	return validateBoard([(9, 6), (9, 8) ,(10, 7), (10, 8), (11, 7)])

def testSingleRule():
	""" Test reglen om at hvis kun 1 levende celle findes i spillet, så dør den. """
	global nextBoard
	nextBoard = newBoard()
	createLifeForm([(10,10)])
	prevBoardValdation = validateBoard([(10,10)])
	naeste()
	return prevBoardValdation and validateBoard([])

def testDoubleRule():
	""" Test reglen om at hvis der er to levende celler omkring en celle, så skifter den ikke state. """
	global nextBoard
	nextBoard = newBoard()
	liste = [(i,i) for i in range(width)]
	createLifeForm(liste)
	prevBoardValdation = validateBoard(liste)
	naeste()
	return prevBoardValdation and validateBoard(liste)
	

def testTripleRule():
	""" Test reglen om at en død celle med 3 levende celler omkring den kommer til live. """
	global nextBoard
	nextBoard = newBoard()
	liste1 = [(10, 9), (10, 10), (10, 11)]
	liste2 = [(9,10), (10, 10), (11, 10)]
	createLifeForm(liste1)
	prevBoardValidation1 = validateBoard(liste1)
	naeste()
	prevBoardValidation2 = validateBoard(liste2)
	naeste()
	return prevBoardValidation1 and prevBoardValidation2 and validateBoard(liste1)

def testAll():
	""" Kører alle tests. """
	if not testFoerste():
		print "testFoerste fejlede."
	if not testLevende():
		print "testLevende fejlede."
	if not testNaeste():
		print "testNaeste fejlede."
	if not testSingleRule():
		print "testSingleRule fejlede."
	if not testDoubleRule():
		print "testDoubleRule fejlede."
	if not testTripleRule():
		print "testTripleRule fejlede."
	if testSingleRule() and testDoubleRule() and testTripleRule() and testFoerste() and testLevende():
		print "Alle tests var vellykket.\nStarter Life."
		return True
	return False

# Main
if __name__ == "__main__": 
	if testAll():
		visLife(foerste, naeste, levende)