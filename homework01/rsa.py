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


print(multiplicative_inverse(7, 40))