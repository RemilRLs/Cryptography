import base64
from Crypto.Util.number import *

# Encoding: ASCII

byte_list = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]


ascii_string = bytes(byte_list).decode('ascii')

print(ascii_string)

# Encoding: HEX

hex_str = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"

byte_list = bytes.fromhex(hex_str)

print(byte_list.decode('ascii'))

# Encoding: BASE64
hex_str = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

# Encoding : HEX

byte_data = bytes.fromhex(hex_str)

base64_encoded = base64.b64encode(byte_data)

ascii_result = base64_encoded.decode('ascii')

print(ascii_result.replace('+', '_'))


n = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
decoded_bytes = long_to_bytes(n)

decoded_message = decoded_bytes.decode('ascii')

print(decoded_message)
