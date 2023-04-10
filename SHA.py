import hashlib

# def hash_message(message: str) -> str:
#     return hashlib.sha3_256(message.encode()).hexdigest()

b = 1600
r = 1088
c = b-r
w = 64
d = 256
rounds = 24

ROT =  [[0,36,3,41,18],
        [1,44,10,45,2],
        [62,6,43,15,61],
        [28,55,25,21,56],
        [27,20,39,8,14]]

RC = [
    0x0000000000000001, 0x0000000000008082, 0x800000000000808A,
    0x8000000080008000, 0x000000000000808B, 0x0000000080000001,
    0x8000000080008081, 0x8000000000008009, 0x000000000000008A,
    0x0000000000000088, 0x0000000080008009, 0x000000008000000A,
    0x000000008000808B, 0x800000000000008B, 0x8000000000008089,
    0x8000000000008003, 0x8000000000008002, 0x8000000000000080,
    0x000000000000800A, 0x800000008000000A, 0x8000000080008081,
    0x8000000000008080, 0x0000000080000001, 0x8000000080008008,
]

def to_bits(s):
    result = []
    for c in s:
        bits = bin(ord(c))[2:]
        bits = '00000000'[len(bits):] + bits
        bits = bits[::-1]
        result.extend([int(b) for b in bits])
    return result

def bits_to_hex(bits):
    chars = []
    for b in range(len(bits) // 8):
        byte = bits[b*8:(b+1)*8]
        byte = byte[::-1]
        chars.append("{:02x}".format(int(''.join([str(bit) for bit in byte]), 2)))
    return ''.join(chars)

def rotate(l, n):
    return l[-n:] + l[:-n]

def str_to_array_state(S):
    A = [[[0 for z in range(w)] for x in range(5)] for y in range(5)]
    for x in range(5):
        for y in range(5):
            for z in range(w):
                A[x][y][z] = S[w*(5*y+x)+z]
    return A
    
def array_state_to_str(A):
    S = [0 for i in range(b)]
    for x in range(5):
        for y in range(5):
            for z in range(w):
                S[w*(5*y+x)+z] = A[x][y][z]
    return S

def pre_processing(m):
    lenB_m = len(m)*8
    M = to_bits(m)
    N = M + [0,1]
    P = N + [1] + [0 for i in range((-4-lenB_m)%r)] + [1]
    n = len(P)//r
    P = [P[i*r:r+i*r] for i in range(n)]
    return P,n

def theta(A):
    B = [[0 for z in range(w)] for x in range(5)]
    C = [[0 for z in range(w)] for x in range(5)]
    D = [[0 for z in range(w)] for x in range(5)]
    for x in range(5):
        for z in range(w):
            C[x][z] = A[x][0][z] ^ A[x][1][z] ^ A[x][2][z] ^ A[x][3][z] ^ A[x][4][z]
    
    for x in range(5):
        B[x] = rotate(list(C[x]),1)
    
    for x in range(5):
        for z in range(w):
            D[x][z] = C[(x-1)%5][z] ^ B[(x+1)%5][z]
       
    for x in range(5):
        for y in range(5):
            for z in range(w):
                A[x][y][z] = A[x][y][z] ^ D[x][z]   
    return A
        
def rho(A):
    for x in range(5):
        for y in range(5):
            A[x][y] = rotate(A[x][y],ROT[x][y])
    return A

def pi(A):
    B = [[[0 for z in range(w)] for x in range(5)] for y in range(5)]
    for x in range(5):
        for y in range(5):
            B[x][y] = A[(x+3*y)%5][x]
    return B
    
def chi(A):
    B = [[[0 for z in range(w)] for x in range(5)] for y in range(5)]
    for x in range(5):
        for y in range(5):
            for z in range(w):
                B[x][y][z] = A[x][y][z] ^ ((A[(x+1)%5][y][z] ^ 1) & A[(x+2)%5][y][z])
    return B

def chi(A):
    B = [[[0 for z in range(w)] for x in range(5)] for y in range(5)]
    for x in range(5):
        for y in range(5):
            for z in range(w):
                B[x][y][z] = A[x][y][z] ^ ((A[(x+1)%5][y][z] ^ 1) & A[(x+2)%5][y][z])
    return B

    
def iota(A,r):
    rc = list(format((RC[r]),'064b'))
    rc = [int(rc[i]) for i in range(w)]
    rc = rc[::-1]
    for z in range(w):
        A[0][0][z] = A[0][0][z] ^ rc[z]
    return A
    
def rnd(A, ir):
    return iota(chi(pi(rho(theta(A)))),ir)

def f(s):
    A = str_to_array_state(s)
    for ir in range(rounds):
        A = rnd(A, ir)
    s = array_state_to_str(A)
    s = s[:d]
    return s
    
def sponge(P,n):
    s = [0 for i in range(b)]
    for i in range(n):
        Pb = P[i] + [0 for i in range(c)]
        s = f([a^b for a,b in zip(s,Pb)])
    return s
    
def hash_message(m):
    P,n = pre_processing(m)
    return bits_to_hex(sponge(P,n))