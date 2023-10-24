encypted_text = open('./output.txt',"r").read()
xor_key = open('./messages.txt',"r").read()

null_payload = b''
for i in range(128):
    null_payload += b'\x00'
    result = bytes([a ^ b for a, b in zip(null_payload, xor_key)])
    print(result.decode())