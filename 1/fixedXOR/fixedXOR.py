import binascii

def fixedXOR(a, b):
	a = bytearray(a)
	b = bytearray(b)
	return bytearray([a[x] ^ b[x % len(b)] for x in range(len(a))])
