from string import ascii_lowercase, ascii_uppercase

a_upper, z_upper = ord("A"), ord("Z")
a_lower, z_lower = ord("a"), ord("z")

def encrypt_caesar(plaintext):

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

    global a_upper, a_lower, z_upper, z_lower

    ciphertext = []
    for symbol in plaintext:

        if symbol in ascii_uppercase:

            sm_code = (ord(symbol) + 3) % z_upper
            symbol =  chr(sm_code) if sm_code >= a_upper else chr(sm_code + a_upper - 1)

        elif symbol in ascii_lowercase:

            sm_code = (ord(symbol) + 3) % z_lower
            symbol = chr(sm_code) if sm_code >= a_lower else chr(sm_code + a_lower - 1)

        ciphertext.append(symbol)

    ciphertext = "".join(ciphertext)

    return ciphertext


def decrypt_caesar(ciphertext):

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

    global a_upper, a_lower, z_upper, z_lower

    plaintext = []
    for symbol in ciphertext:

        if symbol in ascii_uppercase:

            sm_code = (ord(symbol) - 3)
            symbol = chr(sm_code) if sm_code >= a_upper else chr(z_upper + 1 - (a_upper - sm_code))

        elif symbol in ascii_lowercase:

            sm_code = (ord(symbol) - 3)
            symbol = chr(sm_code) if sm_code >= a_lower else chr(z_lower + 1 - (a_lower - sm_code))

        plaintext.append(symbol)

    plaintext = "".join(plaintext)

    return plaintext


