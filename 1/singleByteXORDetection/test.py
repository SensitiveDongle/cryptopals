import singleByteXORDetection
from binascii import unhexlify

with open('ciphertext.txt') as f:
	test_input = [unhexlify(x.strip()) for x in f.readlines()]

if __name__ == '__main__':
	status = '[*]testing singleByteXORDetection...'

	test_output = singleByteXORDetection.solve(test_input).decode('utf-8')
	status += '\n\t' + test_output

	print status
