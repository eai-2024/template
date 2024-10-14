import typing as tp


def encrypt_caesar(plaintext, shift=3):
    """
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """

    ciphertext = ""

    for symbol in plaintext:
        char_num = ord(symbol)

        if ord("a") <= char_num <= ord("z"):
            ciphertext += chr(ord("a") + ((ord(symbol) - ord("a") + shift) % 26))

        elif ord("A") <= char_num <= ord("Z"):
            ciphertext += chr(ord("A") + ((ord(symbol) - ord("A") + shift) % 26))

        else:
            ciphertext += chr(char_num)

    return ciphertext


def decrypt_caesar(ciphertext, shift=3):
    """
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""

    for symbol in ciphertext:
        char_num = ord(symbol)

        if ord("a") <= char_num <= ord("z"):
            plaintext += chr(ord("a") + ((ord(symbol) - ord("a") - shift) % 26))

        elif ord("A") <= char_num <= ord("Z"):
            plaintext += chr(ord("A") + ((ord(symbol) - ord("A") - shift) % 26))

        else:
            plaintext += chr(char_num)

    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    # PUT YOUR CODE HERE
    return best_shift
