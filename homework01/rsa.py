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

    for div in range(2, int(n**0.5) + 1):
        if n % div == 0:
            return False
    else:
        return True


def gcd(a, b):
    """
    >>> gcd(12, 15)
    3
    >>> gcd(3, 7)
    1
    """
    greatest_div = 1

    for potential_div in range(2, min(a, b)):
        if a % potential_div == 0 and b % potential_div == 0:
            greatest_div = potential_div

    return greatest_div


def multiplicative_inverse(e, phi):
    """
    >>> multiplicative_inverse(7, 40)
    23
    """

    table = [[phi, e, phi % e, phi // e]]
    tmp_row_num = 0

    tmp_row = [table[tmp_row_num][1], table[tmp_row_num][2]]
    tmp_row.append(tmp_row[0] % tmp_row[1])
    tmp_row.append(tmp_row[0] // tmp_row[1])
    table.append(tmp_row)
    tmp_row_num += 1

    while tmp_row[2] != 0:
        tmp_row = [table[tmp_row_num][1], table[tmp_row_num][2]]
        tmp_row.append(tmp_row[0] % tmp_row[1])
        tmp_row.append(tmp_row[0] // tmp_row[1])
        table.append(tmp_row)
        tmp_row_num += 1

    x, y = [0], [1]
    for i in range(1, len(table)):
        x.append(y[i - 1])
        y.append(x[i - 1] - y[i - 1] * table[len(table) - i - 1][3])

    return y[-1] % phi


def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("Both numbers must be prime.")
    elif p == q:
        raise ValueError("p and q cannot be equal")

    # n = pq
    n = p * q

    # phi = (p-1)(q-1)
    phi = (p - 1) * (q - 1)

    # Choose an integer e such that e and phi(n) are coprime
    e = random.randrange(1, phi)

    # Use Euclid's Algorithm to verify that e and phi(n) are comprime
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    # Use Extended Euclid's Algorithm to generate the private key
    d = multiplicative_inverse(e, phi)
    # Return public and private keypair
    # Public key is (e, n) and private key is (d, n)
    return ((e, n), (d, n))


if __name__ == "__main__":
    print(generate_keypair(23, 43))
