import random
import math

public_keys = {}

def add_public_key(name, key):
    """Add a public key to the list"""
    public_keys[name] = key

def is_prime(n):
    """Check if a number is prime"""
    if n == 2:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    for i in range(3, math.ceil((n)**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

def encrypt(M, pk):
    """Encrypts a message, M, given a public key pair (n and e)"""
    n, e = pk
    ciphertext = [chr(ord(char)**e % n) for char in M]
    return "".join(ciphertext)

def decrypt(c, pk):
    """Decrypt a ciphertext, c, using the private key"""
    n, d = pk
    message = [chr(ord(char)**d % n) for char in c]
    return "".join(message)

def generate_keys(minimum):
    p, q = get_prime(minimum), get_prime(minimum)
    n = p * q
    phi = (p - 1) * (q - 1)

    e = get_coprime(phi, minimum)
    print(e)

    d = multiplicative_inverse(e, phi)

    return (n,e), (n,d)

def gcd(a, b):
    while b != 0:
        (a,b) = (b, a % b)
    return a

def gcd_extended(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = gcd_extended(b % a, a)
        return (g, x - b//a * y, y)

def multiplicative_inverse(a, n):
    g, x, y = gcd_extended(a, n)
    if g != 1:
        raise Exception("Modular inverse does not exist")
    else:
        return x % n

def get_prime(minimum):
    p = random.randint(minimum, 10*minimum)
    while not is_prime(p):
        p = random.randint(minimum, 10*minimum)
    return p

def get_coprime(phi, minimum):
    e = random.randint(minimum, 10*minimum)
    while gcd(phi, e) != 1:
        e = random.randint(minimum, 10*minimum)
    return e

#pub_key, priv_key = generate_keys(100)
#print(pub_key,priv_key)

#pub_key = [3233,17]
#priv_key = [3233, 2753]

#print(encrypt("Hello",pub_key))
#print(decrypt("ஸԡ˩˩ࢉ",priv_key))

#pub_key = [175187,5]
#priv_key = [175187, 139373]

pub_key = [286271, 781]
priv_key = [286271, 240277]

print(encrypt("Purple Pimento",pub_key))
print(decrypt("𳶦񅯧𤟺𼻬𼌍𼃥𰚏𳶦𑋂𾄎𼃥𙊨𞅲񄗩",priv_key))
