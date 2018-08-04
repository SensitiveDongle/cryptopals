import itertools, math
import singleByteXOR

from IPython import embed

HAM_BLOCKS = 5		# number of blocks of KEYSIZE bytes to ham and compare
MAX_KEYSIZE = 40	#

def ham(s1, s2):
	'''
		calculate the hamming distance between two bytearrays
	'''
	assert len(s1) == len(s2)
	return sum(bin(s1[i]^s2[i]).count('1') for i in range(len(s1)))


def getKeySize(ciphertext):
	'''
	'''
	min_ham = 9
	key_len = 0

	for i in range(1, MAX_KEYSIZE):
		ham_blocks = []

		for j in range(HAM_BLOCKS):
			ham_blocks.append(ciphertext[i*j:i*j+i])

		perms = itertools.combinations(ham_blocks, 2)

		total_ham = 0
		for p in perms:
			total_ham += ham(bytearray(p[0]), bytearray(p[1]))
		ham_avg = (total_ham / (math.factorial(HAM_BLOCKS)/(2*math.factorial(HAM_BLOCKS-2)))) / i
		print(ham_avg)

		if ham_avg < min_ham:
			min_ham = ham_avg
			key_len = i


	print(key_len)

	return key_len

def solve(ciphertext):
	'''
		1 - divide the ciphertext into len(ciphertext)/key_len blocks ("key_blocks")
		2 - create arrays comprising the first byte of each block, the second byte
		of each block, etc. ("byte_blocks")
		3 - solve each of those arrays as single byte XOR
		4 - reassemble 
	'''

	# step 1
	key_len = getKeySize(ciphertext)
	key_blocks = []
	for i in range(len(ciphertext) // key_len):
		key_blocks.append(ciphertext[i*key_len : i*key_len + key_len])
	if len(ciphertext) % key_len:
		key_blocks.append(ciphertext[ key_len*(len(ciphertext)//key_len) : ])

	# step 2
	byte_blocks = [ [] for x in range(key_len) ]
	for i in range(key_len):
		for block in key_blocks:
			if i < len(block):
				byte_blocks[i].append(block[i])
	
	# step 3
	plaintext_blocks = []
	for b in byte_blocks:
		plaintext_blocks.append(singleByteXOR.solve(b))

	# step 4
	plaintext = []
	while(len(plaintext) < len(ciphertext)):
		for b in plaintext_blocks:
			if len(b) > 0:
				plaintext.append(b.pop(0))

	return bytearray(plaintext)
