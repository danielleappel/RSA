import random
import math

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
    """Generate an RSA key pair given some minimum threshold 
    for the numbers"""
    p, q = get_prime(minimum), get_prime(minimum)
    while p == q:
        p = get_prime(minimum)
    n = p * q
    phi = (p - 1) * (q - 1)

    e = get_coprime(phi, minimum)

    d = multiplicative_inverse(e, phi)

    return (n,e), (n,d)

def gcd(a, b):
    """Calculate the greatest common divisor of a and b"""
    while b != 0:
        (a,b) = (b, a % b)
    return a

def gcd_extended(a, b):
    """Apply the extended gcd algorithm to a and b"""
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = gcd_extended(b % a, a)
        return (g, x - b//a * y, y)

def multiplicative_inverse(a, n):
    """Calculate the multiplicative inverse of a mod n"""
    g, x, y = gcd_extended(a, n)
    if g != 1:
        raise Exception("Modular inverse does not exist")
    else:
        return x % n

def get_prime(minimum):
    """Find a random prime number greater than some minimum 
    threshold"""
    p = random.randint(minimum, 10*minimum)
    while not is_prime(p):
        p = random.randint(minimum, 10*minimum)
    return p

def get_coprime(phi, minimum):
    """Find a random number greater than some minimum threshold 
    that is coprime with phi"""
    e = random.randint(minimum, 10*minimum)
    while gcd(phi, e) != 1:
        e = random.randint(minimum, 10*minimum)
    return e

def main():
    pub_key, priv_key = generate_keys(100)
    print(pub_key,priv_key)

    encrypted = encrypt("Hello",pub_key)
    print(encrypted)

    print(decrypt(encrypted,priv_key))

if __name__ == "__main__":
    main()