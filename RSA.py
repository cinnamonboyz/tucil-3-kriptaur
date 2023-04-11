from typing import Tuple, IO
from io import StringIO, BytesIO
from SHA3_256 import hash_message

def find_mod_inverse(e: int, totient_n: int) -> int:
    u1, u2, u3 = 1, 0, e
    v1, v2, v3 = 0, 1, totient_n
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3

    return u1 % totient_n

def generate_public_key(p: int, q: int, e: int) -> Tuple[int, int]:
    return e, p * q

def generate_private_key(p: int, q: int, e: int) -> Tuple[int, int]:
    totient_n = (p - 1)*(q - 1)
    d = find_mod_inverse(e, totient_n)

    return d, p * q

def encrypt(message: str, d: int, n: int) -> str: 
    return ''.join(hex(pow(ord(m), d, n)) for m in message)

    cipher = []

    for m in message: 
        cipher.append(pow(ord(m), d, n)) 

    return ''.join(hex(x) for x in cipher)

def decrypt(cipher: str, e: int, n: int) -> str:
    cipher = [int(x, 16) for x in cipher.split('0x')[1:]]

    return ''.join(chr(pow(c, e, n)) for c in cipher)

    message = "" 
    for c in cipher: 
        message += chr(pow(c, e, n))

    return message

def create_signature(text: str, private_key: Tuple[int, int]) -> str:
    d, n = private_key
    # print(text)
    return encrypt(hash_message(text), d, n)


def sign_in_file(file: IO, private_key: Tuple[int, int]) -> StringIO:
    s = StringIO(file.read())

    signature = create_signature(s.getvalue(), private_key)

    s.writelines(['*** Begin of digital signature ****\n', f'{signature}\n', '*** End of digital signature ****'])
    return s

def sign_separate_file(file: IO, private_key: Tuple[int, int]) -> StringIO:
    signature = create_signature(file.read().decode('latin-1'), private_key)

    s = StringIO()
    s.writelines(['\n*** Begin of digital signature ****\n', f'{signature}\n', '*** End of digital signature ****'])
    return s

def verify_in_file(file: IO, public_key: Tuple[int, int]) -> bool:
    e, n = public_key

    lines = file.readlines()
    try:
        if lines[-1] == '*** End of digital signature ****' and lines[-3] == '*** Begin of digital signature ****\n':
            signature = lines[-2][:-1]
        else:
            raise Exception('File doesn\'t have signature')
    except:
        raise Exception('File doesn\'t have signature')

    decrypted = decrypt(signature, e, n)

    return hash_message(''.join(lines[:-3])[:-1]) == decrypted

def verify_separate_file(file: IO, signature_file: IO, public_key: Tuple[int, int]) -> bool:
    e, n = public_key
    s = file.read().decode('latin-1')

    lines = signature_file.readlines()
    try:
        if lines[-1] == '*** End of digital signature ****' and lines[-3] == '*** Begin of digital signature ****\n':
            signature = lines[-2][:-1]
        else:
            raise Exception('File doesn\'t have signature')
    except:
        raise Exception('File doesn\'t have signature')
    
    return decrypt(signature, e, n) == hash_message(s)




# def encrypt(pk,plaintext):
#     # Unpack the key into it's components
#     key, n = pk
#     # Convert each letter in the plaintext to numbers based on the character using a^b mod m
#     cipher = [pow(ord(char), key, n) for char in plaintext]
#     # Return the array of bytes
#     return cipher


# def decrypt(pk, ciphertext):
#     # Unpack the key into its components
#     key, n = pk
#     # Generate the plaintext based on the ciphertext and key using a^b mod m
#     aux = [str(pow(char, key, n)) for char in ciphertext]
#     # Return the array of bytes as a string
#     plain = [chr(int(char2)) for char2 in aux]
#     return ''.join(plain)

# if __name__ == '__main__':
#     message = "hello reza"
#     n = 3337
#     e = 79
#     d = 1019

#     cipher = encrypt(message, d, n)
#     text = decrypt(cipher, e, n)

#     print(cipher)
#     print(text)