from math import *
import random
from functools import reduce



def getSecondOperand(n1, opr, multiplyLimit = 100, numPDF=[1.0], numRange=[(1,9)] ):
	'''
	gets second operand given the first operand and operator
	'''
	if opr == '/':
		n2 = getNiceDivisor(n1)
	elif opr == '-':
		n2 = getPositiveMinus(n1)
	elif opr == '*':
		n2 = getDoableMultiply(n1, multiplyLimit)
	else:
		n2 = round(weightedRandomRange(numPDF, numRange))
	return int(n2)


def isPrime(n):
	'''
	is prime. return True for primes (including 1)
	'''
	if n<4: 
		return 1
	else:
		return all( n%i for i in range(2,n) )


def factors(n):
	'''
	get factors of a number
	http://stackoverflow.com/a/6800214/2295672
	'''
	return set(reduce(list.__add__,
				([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


def randint(a,b):
	return random.randint(a,b)


def getNiceDivisor(n):
	'''
	get a divisor for n which completely divides it
	'''
	x = sorted(factors(n))
	if len(x) > 2:
		prob = weightedRandomIndex([0.2, 0.8])
		if prob == 1:
			return x[ randint(1, len(x)-2) ]
		else:
			return x[ randint(0, len(x)-1) ]
	else:
		return x[ randint(0, len(x)-1) ]


def getPositiveMinus(n):
	if n==1:
		return 0
	x = randint(1, n-1)
	return x


def getDoableMultiply(n, limit=100):
	x = floor(limit/n)
	return randint(1,x)


def weightedRandomRange(pdf, ranges):
	'''
	get Weighted Random for a range
	Example - 
	pdf = [ 0.2 , 0.8 ]
	ranges = [ (1,2) , (2,3) ]
	Here number returned between 2 and 3 probability is 0.8
	'''
	r = weightedRandomIndex(pdf)
	num = (ranges[r][1] - ranges[r][0]) * random.random()
	return ranges[r][0] + num


def weightedRandom(pdf):
	'''
	Weighted random
	http://stackoverflow.com/a/4266278/2295672
	'''
	# pdf = [(1, 0.1), (2, 0.05), (3, 0.05), (4, 0.2), (5, 0.4), (6, 0.2)]
	cdf = [(i, sum(p for j,p in pdf if j < i)) for i,_ in pdf]
	R = max(i for r in [random.random()] for i,c in cdf if c <= r)
	return R


def weightedRandomIndex(pdf):
	'''
	returns the Index of probability array chosen by random
	pdf = [0.2, 0.4, 0.4]
	will return 0 or 1 or 2
	'''
	x = []
	for i in range(len(pdf)):
		x += [(i, pdf[i])]
	return weightedRandom(x)


if __name__ == '__main__':
	j = [0.2,0.6,0.2]
	for i in range(100):
		x = weightedRandomRange(j, [(-1,1) , (1,2) , (2,3)])
		print(x)
	print( sorted(factors(27)) )