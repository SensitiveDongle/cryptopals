import hex2b64

test_input ='49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
expected_output = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

if __name__ == '__main__':
	print('[*] testing hex to base64 conversion...', end='')

	test_output = hex2b64.hex2b64(test_input)

	if test_output == expected_output:
		print('OK.')
	else:
		print('FAIL.\n\tgot: {0}\n\texpected{1}'.format(test_output,
		expected_output))
