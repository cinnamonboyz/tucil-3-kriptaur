# from io import StringIO, BytesIO

# with open('test_file.txt', 'r') as f:
#     s = StringIO(f.read())
#     s.seek(0, 2)
#     s.writelines(['\n*** Begin of digital signature ****\n', 'SIGNATUREE\n', '*** End of digital signature ****'])
    
#     with open('test_file_signed.txt', 'w') as fw:
#         fw.write(s.read())

from RSA import encrypt
from SHA3_256 import hash_message

with open('foto.jpg', 'rb') as f:
    hashed_file = hash_message(f.read().decode('latin-1'))
    print(hashed_file)
    encrypt(hashed_file)