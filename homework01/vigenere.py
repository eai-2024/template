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
    # PUT YOUR CODE HERE
    keyword_length = len(keyword)
    
    for i in range(len(plaintext)):
        p = plaintext[i]
        k = keyword[i % keyword_length].upper()
        
        if p.isalpha():
            base = ord('A') if p.isupper() else ord('a')
            shift = ord(k) - ord('A')
            ciphertext += chr((ord(p) - base + shift) % 26 + base)
        else:
            ciphertext += p
            
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
    # PUT YOUR CODE HERE
    keyword_length = len(keyword)

    for i in range(len(ciphertext)):
        c = ciphertext[i]
        k = keyword[i % keyword_length].upper()

        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            shift = ord(k) - ord('A')
            plaintext += chr((ord(c) - base - shift) % 26 + base)
        else:
            plaintext += c
            
    return plaintext
