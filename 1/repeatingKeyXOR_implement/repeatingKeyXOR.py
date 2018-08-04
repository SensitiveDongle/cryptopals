
def solve(plaintext, key):
	'''
	'''
	return bytearray([plaintext[x] ^ key[x % len(key)] for x in	range(len(plaintext))])
