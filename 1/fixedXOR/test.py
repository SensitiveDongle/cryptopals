from fixedXOR import fixedXOR
from binascii import hexlify, unhexlify

test_input_a = '1c0111001f010100061a024b53535009181c'
test_input_b = '686974207468652062756c6c277320657965'
expected_output = '746865206b696420646f6e277420706c6179'

if __name__ == '__main__':
	status = '[*] testing fixed XOR...{0}'

	test_output = hexlify(fixedXOR(unhexlify(test_input_a),	unhexlify(test_input_b)))

	if test_output == expected_output:
		status = status.format('OK')
	else:
		status = status.format('FAIL.\n\tgot: {0}\n\texpected{1}'.format(test_output,
		expected_output))

	print(status)
