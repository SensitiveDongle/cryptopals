import binascii
import base64

def hex2b64(hexinput):
	return base64.b64encode(binascii.unhexlify(hexinput))
