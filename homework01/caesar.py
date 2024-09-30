import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

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
    for i in range(0,len(plaintext)):
        if plaintext[i].isalpha():
            if plaintext[i] in "xyzXYZ":
                ciphertext+=(chr(ord(plaintext[i]) - 26 + shift))
            else:
                ciphertext+=(chr(ord(plaintext[i]) + shift))
        else:
            ciphertext+=(plaintext[i])
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

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
    for e in range(0, len(ciphertext)):
        if ciphertext[e].isalpha():
            if ciphertext[e] in "abcABC":
                plaintext+=(chr(ord(ciphertext[e]) + 26 - shift))
            else:
                plaintext+=(chr(ord(ciphertext[e]) - shift))
        else:
            plaintext+=(ciphertext[e])
    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    # PUT YOUR CODE HERE
    return best_shift