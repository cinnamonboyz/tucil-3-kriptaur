import random
from typing import Tuple
from util import is_relative_prime

with open('prime_list.txt', 'r') as f:
    primes = list(map(int, f.read().split()))

def get_random_key() -> Tuple[int, int, int]:
    p, q, e = random.choices(primes, k=3)
    totient_n = (p - 1)*(q - 1)

    while not is_relative_prime(totient_n, e):
        p, q, e = random.choices(primes, k=3)

    return p, q, e


# def pickKeyforMe() -> Tuple:
#     '''
#     Pengacak kunci dari kumpulan bilangan prima terdefinisi
#     '''
#     try:
#         f = open("modules/primelist.txt","r")
#         primes = f.read().split()
#         p,q,e = random.choices(primes, k=3)
#         p = int(p)
#         q = int(q)
#         e = int(e)
#         while (not relativePrime((p-1)*(q-1),e)):
#             p,q,e = random.choices(primes, k=3)
#         return (p,q,e)
#     except Exception as e:
#         raise e

# def relativePrime(a:int, b:int) -> bool:
#     '''
#     Memeriksa apakah A dan B relatif prima
#     '''
#     try:
#         while (b):
#             a, b = b, a% b
#         return (a==1)
#     except Exception as e:
#         raise e