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

pub_key = [3233,17]
priv_key = [3233, 2753]

print(encrypt("Hello",pub_key))

print(decrypt("ஸԡ˩˩ࢉ",priv_key))
