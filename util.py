from typing import Tuple

def is_relative_prime(a: int, b: int) -> bool:
    while b:
        a, b = b, a % b
    
    return a == 1

def write_key_file(key: Tuple[int, int], file_name: str) -> None:
    with open(file_name, 'w') as f:
        f.write(','.join(map(str, key)))

def read_key_file(file_name: str) -> Tuple[int, int]:
    with open(file_name, 'r') as f:
        return tuple(map(int, f.read().split(',')))