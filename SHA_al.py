def sha3_256(msg):
    # Initialize the state
    state = bytearray([0] * 200)
    rate = 136
    capacity = 64
    block_size = 1088

    # Padding the message
    msg += b"\x06"
    msg += bytes((rate - (len(msg) % rate)) % rate)
    msg += b"\x80"

    # Absorbing phase
    c = 0
    for i in range(0, len(msg), rate):
        block = msg[i:i+rate]
        block += bytes(rate - len(block))
        for j in range(0, block_size, rate):
            for k in range(rate):
                state[k+j] ^= block[k]

        # Applying the Keccak permutation
        for r in range(24):
            state = keccak_f(state, c, capacity)
            c = (c + capacity) % block_size

    # Squeezing phase
    hash_bytes = bytearray()
    output_len = 32
    while output_len > 0:
        block = state[:rate]
        hash_bytes += block[:output_len]
        output_len -= len(block)
        state = keccak_f(state, c, capacity)
        c = (c + capacity) % block_size

    return bytes(hash_bytes)


def keccak_f(state, c, capacity):
    # Constants
    RC = [0x0000000000000001, 0x0000000000008082, 0x800000000000808a,
          0x8000000080008000, 0x000000000000808b, 0x0000000080000001,
          0x8000000080008081, 0x8000000000008009, 0x000000000000008a,
          0x0000000000000088, 0x0000000080008009, 0x000000008000000a,
          0x000000008000808b, 0x800000000000008b, 0x8000000000008089,
          0x8000000000008003, 0x8000000000008002, 0x8000000000000080,
          0x000000000000800a, 0x800000008000000a, 0x8000000080008081,
          0x8000000000008080, 0x0000000080000001, 0x8000000080008008]

    # Initialization
    A = [0] * 25
    for i in range(25):
        A[i] = state[i*8] | state[i*8+1] << 8 | state[i*8+2] << 16 | \
               state[i*8+3] << 24 | state[i*8+4] << 32 | state[i*8+5] << 40 | \
               state[i*8+6] << 48 | state[i*8+7] << 56

    # Rounds
    for i in range(24):
        # Theta
        C = [0] * 5
        for j in range(5):
            C[j] = A[j] ^ A[j+5] ^ A[j+10] ^ A[j+15] ^ A[j+20]
        D = [0] * 5
        for j in range(5):
            D[j] = C[(j+4) % 5] ^ ((C[(j+1) % 5] << 1) | (C[(j+1) % 5] >> 63))


message = "halo"
print(sha3_256(message.encode("utf-8")).hex())