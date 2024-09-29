import random

def is_prime(n):
    """
    >>> is_prime(2)
    True
    >>> is_prime(11)
    True
    >>> is_prime(8)
    False
    """
    dividers = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            dividers.append(i)
            dividers.append(n//i)
    if len(dividers) == 2:
        return True
    return False

def gcd(a, b):
    a, b = sorted([a, b], reverse=True)

    while b:
        a, b = b, a%b
    return a


def multiplicative_inverse(e, phi):
    """
    >>> multiplicative_inverse(7, 40)
    23
    """

    tablo = []
    a, b = sorted([e, phi], reverse=True)

    while a % b != 0:
        tablo.append([a, b, a % b, a // b, None, None])
        a, b = b, a % b

    tablo[-1][-2], tablo[-1][-1] = 0, 1


    for i in range(len(tablo)-2, -1, -1):
        prev_x, prev_y, a_div_b = tablo[i+1][-2], tablo[i+1][-1], tablo[i][3]
        x = tablo[i+1][-1]
        y =  prev_x - prev_y * a_div_b

        tablo[i][-2], tablo[i][-1] = x, y

    return tablo[0][-1]


def generate_keypair(p, q):

    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')

    n = p * q

    phi = (p - 1) * (q - 1)

    e = random.randrange(1, phi)

    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)


    d = multiplicative_inverse(e, phi)

    return ((e, n), (d, n))


# не знаю зачем следующий код (его в задании изначально не было), но раз был пусть будет

def encrypt(pk: tp.Tuple[int, int], plaintext: str) -> tp.List[int]:
    # Unpack the key into it's components
    key, n = pk
    # Convert each letter in the plaintext to numbers based on
    # the character using a^b mod m
    cipher = [(ord(char) ** key) % n for char in plaintext]
    # Return the array of bytes
    return cipher


def decrypt(pk: tp.Tuple[int, int], ciphertext: tp.List[int]) -> str:
    # Unpack the key into its components
    key, n = pk
    # Generate the plaintext based on the ciphertext and key using a^b mod m
    plain = [chr((char ** key) % n) for char in ciphertext]
    # Return the array of bytes as a string
    return "".join(plain)


if __name__ == "__main__":
    print("RSA Encrypter/ Decrypter")
    p = int(input("Enter a prime number (17, 19, 23, etc): "))
    q = int(input("Enter another prime number (Not one you entered above): "))
    print("Generating your public/private keypairs now . . .")
    public, private = generate_keypair(p, q)
    print("Your public key is ", public, " and your private key is ", private)
    message = input("Enter a message to encrypt with your private key: ")
    encrypted_msg = encrypt(private, message)
    print("Your encrypted message is: ")
    print("".join(map(lambda x: str(x), encrypted_msg)))
    print("Decrypting message with public key ", public, " . . .")
    print("Your message is:")
    print(decrypt(public, encrypted_msg))
