from string import ascii_lowercase, ascii_uppercase

a_upper, z_upper = ord("A"), ord("Z")
a_lower, z_lower = ord("a"), ord("z")

def encrypt_vigenere(plaintext, keyword):
    """

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'

    >>> encrypt_vigenere("python", "a")
    'python'

    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'

    """

    global a_upper, a_lower, z_upper, z_lower

    start_len = len(keyword)
    pointer = 0
    while len(keyword) < len(plaintext):
        keyword += keyword[pointer % start_len]
        pointer += 1

    ciphertext = []
    for symbol_index in range(len(plaintext)):

        symbol = plaintext[symbol_index]

        if symbol in ascii_uppercase:

            step = ord(keyword[symbol_index]) - a_upper

            sm_code = (ord(symbol) + step) % z_upper

            symbol = chr(sm_code) if sm_code >= a_upper else chr(sm_code + a_upper - 1)

        elif symbol in ascii_lowercase:

            step = ord(keyword[symbol_index]) - a_lower
            sm_code = (ord(symbol) + step) % z_lower
            symbol = chr(sm_code) if sm_code >= a_lower else chr(sm_code + a_lower - 1)
        ciphertext.append(symbol)

    ciphertext = "".join(ciphertext)

    return ciphertext


def decrypt_vigenere(ciphertext, keyword):

    """
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """

    global a_upper, a_lower, z_upper, z_lower

    start_len = len(keyword)
    pointer = 0
    while len(keyword) < len(ciphertext):
        keyword += keyword[pointer % start_len]
        pointer += 1

    plaintext = []

    for symbol_index in range(len(ciphertext)):

        symbol = ciphertext[symbol_index]

        if symbol in ascii_uppercase:
            step = ord(keyword[symbol_index]) - a_upper
            sm_code = (ord(symbol) - step)
            symbol = chr(sm_code) if sm_code >= a_upper else chr(z_upper + 1 - (a_upper - sm_code))

        elif symbol in ascii_lowercase:
            step = ord(keyword[symbol_index]) - a_lower
            sm_code = (ord(symbol) - step)
            symbol = chr(sm_code) if sm_code >= a_lower else chr(z_lower + 1 - (a_lower - sm_code))
        plaintext.append(symbol)

    plaintext = "".join(plaintext)

    return plaintext
