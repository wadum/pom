#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
	Opgave 10

	Dette bibliotek er implementeret med alle for løkker
	omskrevet til list comprehension i stedet.

	Jeg var allerede bekendt med for løkker, og har
	prøvet at gøre opgaven en smule mere lærerig for
	mig selv.
"""

class SimpleMatrix :
	def __init__(self, m = None, n = None, values = None):
		""" Konstruktor til SimpleMatrix.

			SimpleMatrix() konstruerer en 0 x 0 matrice.

			SimpleMatrix(m, n) konstruerer en m x n matrice, hvor 
			alle felter er lig 0.

			SimpleMatrix(m, n, values) konstruerer en m x n matrice, 
			og lægger værdierne fra values linært ind i matricen.

		"""
		if m is None and n is None and values is None:
			self.matrix = []
		if m is not None and n is not None and values is None:
			self.matrix = [[0 for i in range(n)] for i in range(m)]
		if m is not None and n is not None and values is not None:
			self.matrix = [[values[j*n+i] for i in range(n)] for j in range(m)]
		self.versionId = "2793527429"

	def __str__(self):
		""" Returnere en streng-repræsentation af matricen.

		"""
		s = "";
		for row in self.matrix:
			for element in row:
				s += str(element) + " "
			s += "\n"
		return s.strip()

	def read(self, filename):
		""" Opdaterer indholdet af matricen med værdierne fra filen.

			Funktionen forventer at filen er skrevet med SimpleMatrix.write().
		"""
		with open(filename, "r") as f:
			if f.readline().strip() == self.versionId: # Hvis den første linje indholder versionId,
				self.__init__(                         # forventes det at resten af filen er korrekt
					int(f.readline()),                 # formateret.
					int(f.readline()), 
					[int(value) for value in f.readline().strip().split()]
					)
			else:
				Exception("Filen indholder ikke en matrice.")

	def write(self, filename):
		""" Skriver matricen til filen.

			Denne funktion er destruktiv. Indholdet af filename overskrives!
		"""
		with open(filename, "w") as f:
			f.write(self.versionId + "\n")
			f.write(str(self.getM()) + "\n")
			f.write(str(self.getN()) + "\n")
			for value in self.getValues():
				f.write(str(value) + " ")
	
	def __add__(self, other):
		""" Adderer to matricer.

			Dette er en immutabel funktion.
		"""
		if not (self.getM() == other.getM() and self.getN() == other.getN()):
			return Exception("Matricerne har ikke samme størrelse.")
		else:
			return	SimpleMatrix(
						self.getM(), 
						self.getN(), 
						[s + o for (s, o) in zip(self.getValues(),other.getValues())]
					)
	def __mul__(self, other):
		""" Multiplicerer to matricer

			Dette er en immutabel funktion.
		"""
		if self.getM() == other.getN():
			return  SimpleMatrix(
						self.getM(),
						other.getN(),
						[sum([self.matrix[i][k] * other.matrix[k][j] for k in range(other.getM())])
							for j in range(other.getN())
							for i in range(self.getM())]
					)
		else:
			return Exception("Søjlerne i første matrice har ikke samme størrelse som rækkerne i anden matrice.")
	
	def __eq__(self, other):
		""" Sammenligner to matricer.

			Returnere true hvis begge matricer indeholder samme værdier.
		"""
		return	self.getM() == other.getM() and self.getN() == other.getN() and all(
				[s == o for (s, o) in zip(self.getValues(),other.getValues())])
	def __ne__(self, other):
		""" Sammenligner to matricer.

			Returnere true hvis begge matricer er forskellige fra hinanden.
		"""
		return not self == other

	def getM(self):
		""" Returnere m for matricen.

		"""
		return len(self.matrix)

	def getN(self):
		""" Returnere n for matricen.

		"""
		return len(self.matrix[0])

	def getValues(self):
		""" Returnere en liste af værdierne i matricen.

		"""
		return [item for row in self.matrix for item in row]

if __name__ == '__main__':
	matrixA = SimpleMatrix(2, 3, [1,2,3,4,5,6])
	matrixA.write("test.mt")
	matrixB = SimpleMatrix()
	matrixB.read("test.mt")
	matrixC = SimpleMatrix(2, 3, [2,4,6,8,10,12])
	matrixD = SimpleMatrix(3, 2, [1,2,3,4,5,6])
	matrixE = SimpleMatrix(3,3,[9,19,29,12,26,40,15,33,51])
	print "Printer en matrice:\n%s" % matrixA
	print "Tjekker at == og != fungere: %s" % (matrixA == matrixA and not matrixA != matrixA)
	print "Tjekker at write og read fungere: %s" % (matrixA == matrixB)
	print "Tjekker at + fungere: %s" % (matrixA + matrixA == matrixC)
	print "Tjekker at * fungere: %s" % ((matrixD * matrixA) == matrixE)