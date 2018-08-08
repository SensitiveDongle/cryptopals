from Crypto.Cipher import AES

def solve(key, text, enc_dec=0):
	'''
		encrypt = 0
		decrypt = not 0
	'''

	output = b''
	cipher = AES.new(key, AES.MODE_ECB)

	if enc_dec == 0:
		output = cipher.encrypt(bytes(text))
	else:
		output = cipher.decrypt(bytes(text))

	return output
