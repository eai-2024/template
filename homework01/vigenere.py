def match_keyword_len(keyword, target_len):
    final_keyword = ""
    tmp_keyword_len = len(keyword)

    final_keyword = (
        keyword * (target_len // tmp_keyword_len) + keyword[: target_len % tmp_keyword_len]
    )

    return final_keyword


def is_capital(letter):
    char_num = ord(letter)

    if ord("A") <= char_num <= ord("Z"):
        return True
    else:
        return False


def encrypt_vigenere(plaintext, keyword):
    """
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """

    ciphertext = ""
    matched_keyword = match_keyword_len(keyword, len(plaintext))

    for i in range(len(plaintext)):
        char_num = ord(plaintext[i])
        key_num = ord(matched_keyword[i])

        if matched_keyword[i].isalpha():
            if is_capital(matched_keyword[i]):
                tmp_shift = key_num - ord("A")
            else:
                tmp_shift = key_num - ord("a")

        if plaintext[i].isalpha():
            if is_capital(plaintext[i]):
                ciphertext += chr(ord("A") + (char_num - ord("A") + tmp_shift) % 26)
            else:
                ciphertext += chr(ord("a") + (char_num - ord("a") + tmp_shift) % 26)
        else:
            ciphertext += chr(char_num)

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

    plaintext = ""
    matched_keyword = match_keyword_len(keyword, len(ciphertext))

    for i in range(len(ciphertext)):
        char_num = ord(ciphertext[i])
        key_num = ord(matched_keyword[i])

        if is_capital(matched_keyword[i]):
            tmp_shift = key_num - ord("A")
        else:
            tmp_shift = key_num - ord("a")

        if is_capital(ciphertext[i]):
            plaintext += chr(ord("A") + (char_num - ord("A") - tmp_shift) % 26)
        else:
            plaintext += chr(ord("a") + (char_num - ord("a") - tmp_shift) % 26)

    return plaintext


if __name__ == "__main__":
    print(encrypt_vigenere("Hello World!+_-=", "python"))
