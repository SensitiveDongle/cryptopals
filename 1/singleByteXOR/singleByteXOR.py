import string

frequencyScores = {'E':12.02,'T':9.10,'A':8.12,'O':7.68,'I':7.31,'N':6.95,'S':6.28,'R':6.02,'H':5.92,'D':4.32,'L':3.98,'U':2.88,'C':2.71,'M':2.61,'F':2.30,'Y':2.11,'W':2.09,'G':2.03,'P':1.82,'B':1.49,'V':1.11,'K':0.69,'X':0.17,'Q':0.11,'J':0.10,'Z':0.07,' ':1}


def englishness(a):
	'''
	determine how close to an english phrase this string might be
	'''
	rawScore = 0

	a = bytearray(a)

	for char in a:
		if chr(char).upper() in frequencyScores:
			rawScore += frequencyScores[chr(char).upper()]
		elif chr(char) not in string.printable:
			rawScore = -1000000
			return rawScore
		else:
			rawScore -= 100

	return rawScore / len(a)


def xor(a, b):
	'''
	'''
	a = bytearray(a)
	b = bytearray(b)
	return bytearray([a[x] ^ b[x % len(b)] for x in range(len(a))])


def solve(x):
	'''
	'''

	topscore = -1000000000
	topstring = x

	for val in range(0,256):
		newstring = xor(x, bytearray([val]))
		newscore = englishness(newstring)

		if newscore > topscore:
			topscore = newscore
			topstring = newstring

	return topstring
