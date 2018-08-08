import base64
import ImplementECB

from IPython import embed

test_input = bytearray(base64.b64decode((open('7.txt').read().strip())))
key = b'YELLOW SUBMARINE'
expected_output = ''

if __name__ == '__main__':
	status = '[*]testing implement AES_ECB...'

	test_output = ImplementECB.solve(key, test_input, 1).decode('utf-8')
	status += '\n\t' + test_output

	print(status)
