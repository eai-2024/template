def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    keyword = keyword.upper()
    key_index = 0

    for char in plaintext:
        if char.isalpha():
            if char.isupper():
                shift = ord(keyword[key_index]) - ord('A')
                encrypted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
                ciphertext+=encrypted_char
                key_index = (key_index + 1) % len(keyword)
            else:
                shift = ord(keyword[key_index]) - ord('A')
                encrypted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
                ciphertext += encrypted_char
                key_index = (key_index + 1) % len(keyword)
        else:
            ciphertext+=char

    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    keyword = keyword.upper()
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            if char.isupper():
                shift = ord(keyword[key_index]) - ord('A')
                decrypted_char = chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
                plaintext += decrypted_char
                key_index = (key_index + 1) % len(keyword)
            else:
                shift = ord(keyword[key_index]) - ord('A')
                decrypted_char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
                plaintext += decrypted_char
                key_index = (key_index + 1) % len(keyword)
        else:
            plaintext += char

    return plaintext
