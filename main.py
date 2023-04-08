from key_generator import get_random_key
from RSA import generate_private_key, generate_public_key
from SHA import hash_message
from util import write_key_file, read_key_file

if __name__ == '__main__':
    message = "Hello Fikri"

    p, q, e = get_random_key()
    print(f'{p=}, {q=}, {e=}')


    # generate keys
    private_key = generate_private_key(p, q, e)
    write_key_file(private_key, 'my_private_key.pri')

    public_key = generate_public_key(p, q, e)
    write_key_file(public_key, 'my_public_key.pub')

    
    # hash message
    hashed_message = hash_message(message)



    # read keys
    private_key = read_key_file('my_private_key.pri')
    public_key = read_key_file('my_public_key.pub')

