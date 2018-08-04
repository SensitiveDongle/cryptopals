#!/usr/bin/env python3

import repeatingKeyXOR_break
import base64
from binascii import hexlify, unhexlify

test_input = base64.b64decode(open('6.txt').read().strip())
expected_output = 'x'

if __name__ == '__main__':
	status = '[*] testing repeatingKeyXOR_break...'

	test_output = repeatingKeyXOR_break.solve(bytearray(test_input))

	if not test_output == expected_output:
		status += 'FAIL\n\tgot: {0}\n\texpected: {1}'.format(test_output,
		expected_output)
	else:
		status += 'OK.'
	
	print(status)
