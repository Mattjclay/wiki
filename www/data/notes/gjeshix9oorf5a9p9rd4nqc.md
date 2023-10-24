[[Link to flags|tags.Flags.Crypto]]

Below is the encoded flag found in **output.txt**
The top line is encoded in **HEX**
The bottom line is encoded in **BASE64**

**Please note**, you **do not** need to run the script **source.py** to solve this challenge.



**HEX** 
4854427b6b6e3077316e675f6830775f74305f3164336e743166795f336e633064316e675f736368336d33735f31735f6372756331346c5f6630725f615f

**BASE64**
Y3J5cHQwZ3I0cGgzcl9fXzRsczBfZDBfbjB0X2MwbmZ1czNfZW5jMGQxbmdfdzF0aF9lbmNyeXA1MTBuIX0=



By reading the source code it is fairly easy to see what the program does. There is a flag stored in the **secret.FLAG** array. The array is split in half then encoded. **On line 69** you can see that the program returns a string, the first string is encoded in **HEX** then a newline is inserted, the second string is then encoded in **BASE64**, the result is then written to the file **output.txt**

## Source Code
``` python
from secret import FLAG

HEX_CHARS = '0123456789abcdef'
B64_CHARS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'


def to_hex(data):
    data = int.from_bytes(data, 'big')
    encoded = ''
    while data:
        i = data % 16
        encoded = HEX_CHARS[i] + encoded
        data >>= 4
    return '0' * (len(encoded) % 2) + encoded


def to_base64(data):
    padding_length = 0

    if len(data) % 3 != 0:
        padding_length = (len(data) + 3 - len(data) % 3) - len(data)

    data += b'\x00' * padding_length
    bits = ''.join([bin(c)[2:].zfill(8) for c in data])
    blocks = [bits[i:i+6] for i in range(0, len(bits), 6)]

    encoded = ''
    for block in blocks:
        encoded += B64_CHARS[int(block, 2)]

    return encoded[:-padding_length] + '=' * padding_length


def main():
    first_half = FLAG[:len(FLAG)//2]
    second_half = FLAG[len(FLAG)//2:]

    hex_encoded = to_hex(first_half)
    base64_encoded = to_base64(second_half)

    with open('output.txt', 'w') as f:
        f.write(f'{hex_encoded}\n{base64_encoded}')

main()
```



## Solution Code
Create a script and run it in the same directory as the **output.txt** file from the challenge files. Your flag will be printed to the terminal and to a file called **flag.txt**
``` python
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

```