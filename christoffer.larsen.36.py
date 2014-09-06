import math as m;

def findRodder(a, b, c):
	if a == 0:
		raise ZeroException("Ikke et andengradspolynomium.")
	if b <= 0:
		x1 = (-b + m.sqrt(b*b - 4*a*c))/(2*a)
	else:
		x1 = (-b - m.sqrt(b*b - 4*a*c))/(2*a)
	if x1 != 0:
		x2 = (c/a)/x1
	else:
		x2 = -b / a
	return x1, x2

class ZeroException(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)

def main():
	try:
		print "x1 = %f, x2 = %f" % findRodder(1, 1000.001, 1)
	except ZeroException as e:
		print e


if __name__ == "__main__":
	main()