from key_generator import get_random_key
from RSA import generate_private_key, generate_public_key, encrypt, decrypt, sign_in_file, sign_separate_file, verify_separate_file, verify_in_file
from SHA3_256 import hash_message
from util import write_key_file, read_key_file
import hashlib

if __name__ == '__main__':
    # message = "Proses transformasi dalam biologi molekuler merujuk pada perubahan sifat genetik suatu organisme melalui pengambilan, penerimaan, atau transfer materi genetik. Ada beberapa jenis proses transformasi dalam biologi molekuler, termasuk transfer gen horizontal, transformasi, natural competence, artificial competence, dan zona adhesi."

    p, q, e = get_random_key()
    print(f'{p=}, {q=}, {e=}')


    # generate keys
    private_key = generate_private_key(p, q, e)
    write_key_file(private_key, 'my_private_key.pri')

    public_key = generate_public_key(p, q, e)
    write_key_file(public_key, 'my_public_key.pub')


    # with open('test_file.txt', 'r') as plain_file:
    #     buf = sign_in_file(plain_file, private_key)
    #     with open('test_file_signed.txt', 'w') as signed_file:
    #         signed_file.write(buf.getvalue())

    # with open('test_file_signed.txt', 'r') as signed_file:
    #     verified = verify_in_file(signed_file, public_key)
    #     print(verified)

    with open('foto.jpg', 'rb') as plain_file:
        with open('foto.jpg_signed.txt', 'w') as signature_file:
            buf = sign_separate_file(plain_file, private_key)
            signature_file.write(buf.getvalue())

    with open('foto.jpg', 'rb') as plain_file:
        with open('foto.jpg_signed.txt', 'r') as signature_file:
            verified = verify_separate_file(plain_file, signature_file, public_key)
            print(verified)