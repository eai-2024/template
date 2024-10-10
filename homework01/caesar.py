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
    flag_size = "big"
    shift = int(shift)
    for i in range(len(plaintext)):
        if (
                plaintext[i] != plaintext[i].upper()
        ):  # для каждого символа запоминаем прописной или строчной
            flag_size = "small"
        if (
                64 < ord((plaintext[i]).upper()) < 91
        ):  # зашифровываю только если это буква лат. алфавита
            new_order = (
                    ord(plaintext[i].upper()) + shift
            )  # нахожу новый номер в алфавите (шифровка)
            if (
                    new_order > 90
            ):  # если новый номер выпадает за пределы алфавита, вычитаю длину алфавита
                new_order -= 26
            if flag_size == "small":
                ciphertext += (chr(new_order)).lower()
            else:
                ciphertext += chr(new_order)
        else:  # если не буква лат. алфавита, то оставляю как есть
            ciphertext += plaintext[i]
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
    shift = int(shift)
    plaintext = ""
    flag_size = "big"
    for i in range(len(ciphertext)):
        if (
                ciphertext[i] != ciphertext[i].upper()
        ):  # для каждого символа запоминаем прописной или строчной
            flag_size = "small"
        if (
                64 < ord((ciphertext[i]).upper()) < 91
        ):  # зашифровываю только если это буква лат. алфавита
            new_order = (
                    ord(ciphertext[i].upper()) - shift
            )  # нахожу новый номер в алфавите (шифровка)
            if (
                    new_order < 65
            ):  # если новый номер выпадает за пределы алфавита, вычитаю длину алфавита
                new_order += 26
            if flag_size == "small":
                plaintext += (chr(new_order)).lower()
            else:
                plaintext += chr(new_order)
        else:  # если не буква лат. алфавита, то оставляю как есть
            plaintext += ciphertext[i]
    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    # PUT YOUR CODE HERE
    return best_shift
