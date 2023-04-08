from typing import Tuple
import hashlib

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

def encrypt(message, key):
    ...








'''
RSA (Rivest-Shamir-Adleman) Algorithm

Encryption
'''

from typing import List
import math

def baseEncrypt(m: int, d: int, n: int) -> int:
    '''
    Fungsi basis enkripsi RSA menggunakan kunci private (d,n)
    '''
    return pow(m, d, n)
    
def convertBytetoIntArray(bytesInput: bytes, digitDiv: int) -> List[int]:
    '''
    Konversi Byte ke Array of Integer
    '''
    result = []
    binInput = bin(int.from_bytes(bytesInput, "big"))[2:]

    for index in range(0, len(binInput), digitDiv):
        result.append(int(binInput[index : index + digitDiv], 2))
    result.append(len(binInput) % digitDiv)

    return result
    
def convertIntArraytoByte(inputList: List[int], digit: int) -> bytes:
    '''
    Konversi Array of Integer menjadi Byte
    '''
    binary = ''.join([bin(val)[2:].zfill(digit) for val in inputList]) 
    
    intResult = int(binary, 2)
    result = intResult.to_bytes((len(binary) + 7) // 8, "big")

    return result

def digitDivider(n: int) -> int:
    '''
    Menentukan panjang digit/bit untuk membagi binary file
    '''
    return math.floor(math.log2(n))

def maxBitLength(n: int) -> int:
    '''
    Menentukan panjang bit maksimal untuk menyimpan enkripsi [0...n-1]
    '''
    return (n-1).bit_length()

def encryptBytes(message: bytes, d: int, n: int) -> bytes:
    '''
    Operasi enkripsi file berdasarkan kunci publik (e,n)
    File disimpan dalam direktori /files/
    '''
    plainBytes = message
    
    digitDiv = digitDivider(n)
    intValue = convertBytetoIntArray(plainBytes, digitDiv)
    cipherInt = [baseEncrypt(val, d, n) for val in intValue]
    cipherBytes = convertIntArraytoByte(cipherInt, maxBitLength(n))

    return cipherBytes


'''
RSA (Rivest-Shamir-Adleman) Algorithm

Decryption
'''

from typing import List
import math

def baseDecrypt(c: int, e: int, n: int) -> int:
    '''
    Fungsi basis dekripsi RSA menggunakan kunci privat (d,n)
    '''
    try:
        return pow(c, e, n)
    except Exception as E:
        raise(E)

def binaryPadding(bits: str, n: int) -> str :
    '''
    Menambahkah padding '0' sebanyak n bit.
    '''
    try:
        while len(bits) % n != 0:
            bits = '0'+bits
        return bits
    except Exception as E:
        raise(E)
    
def convertBytetoIntArray(bytesInput: bytes, digitDiv: int) -> List[int]:
    '''
    Konversi Byte ke Array of Integer
    '''
    try:
        result = []
        binInput = bin(int.from_bytes(bytesInput, "big"))[2:]
        binInput = binaryPadding(binInput, digitDiv)

        for index in range(0, len(binInput), digitDiv):
            result.append(int(binInput[index : index + digitDiv], 2))

        return result
    except Exception as E:
        raise(E)

def convertIntArraytoByte(inputList: List[int], digit: int) -> bytes:
    '''
    Konversi Array of Integer menjadi Byte
    '''
    try:
        binary = ''
        for i, val in enumerate(inputList):
            if i != len(inputList)-2 :
                binary+=bin(val)[2:].zfill(digit)
            else:
                binary+=bin(val)[2:].zfill(inputList[-1])
                break

        intResult = int(binary, 2)
        result = intResult.to_bytes((len(binary) + 7) // 8, "big", signed=False)

        return result
    except Exception as E:
        raise(Exception("kunci tidak cocok!"))

def digitDivider(n: int) -> int:
    '''
    Menentukan panjang digit/bit awal
    '''
    try:
        return math.floor(math.log2(n))
    except Exception as E:
        raise(E)

def maxBitLength(n: int) -> int:
    '''
    Menentukan panjang bit maksimal membagi enkripsi binary [0...n-1]
    '''
    try:
        return (n-1).bit_length()
    except Exception as E:
        raise(E)

def decryptBytes(message: bytes, e: int, n: int):
    '''
    Operasi dekripsi file berdasarkan kunci publik (d,n)
    File disimpan dalam direktori /files/
    '''
    try:
        cipherBytes = message
        digitDiv = digitDivider(n)
        intValue = convertBytetoIntArray(cipherBytes, maxBitLength(n))
        plainInt = [baseDecrypt(val, e, n) for val in intValue]
        plainBytes = convertIntArraytoByte(plainInt, digitDiv)

        return plainBytes
    except Exception as E:
        raise(E)