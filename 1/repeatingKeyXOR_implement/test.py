import repeatingKeyXOR
from binascii import hexlify, unhexlify

test_input = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
expected_output = "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"

key = 'ICE'

if __name__ == '__main__':
	status = '[*] testing repeatingKeyXOR...'

	test_output = hexlify(repeatingKeyXOR.solve(bytearray(test_input), bytearray(key)))
	if not test_output == expected_output:
		status += 'FAIL\n\tgot: {0}\n\texpected: {1}'.format(test_output,
		expected_output)
	else:
		status += 'OK.'
	
	print(status)
