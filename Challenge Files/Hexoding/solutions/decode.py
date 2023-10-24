import base64


def decode_hex(string_to_decode):
    return str(bytes.fromhex(string_to_decode), 'utf-8')

def decode_base64(string_to_decode):
    return str(base64.b64decode(string_to_decode), 'utf-8')

with open('./output.txt', 'r') as file:
    flag_result = ""
    try:
        with open('./flag.txt', 'w') as out_file:
            flag_result += decode_hex(file.readline())
            flag_result += decode_base64(file.readline())
            out_file.write(flag_result)
            print(f"File flag.txt created with your flag in it! \n{flag_result}")

    except:
        pass
        


