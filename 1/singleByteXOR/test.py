import singleByteXOR
from binascii import unhexlify

test_input = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
expected_output = 'ETAOIN SHRDLU'

if __name__ == '__main__':
	status = '[*]testing singleByteXOR...'

	test_output = singleByteXOR.solve(unhexlify(test_input)).decode('utf-8')
	status += '\n\t' + test_output

	print status
