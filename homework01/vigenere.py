def decrypt_vigenere(plaintext, keyword):
    ciphertext = ""
    key_code = []
    keyword = keyword.lower()
    for i in keyword:
        key_code.append(ord(i) - 97)  # добавляю в key_code ключ(сдвиг) для каждой буквы
    for i in range(len(plaintext)):
        flag_size = "small"
        if (
                plaintext[i] != plaintext[i].lower()
        ):  # для каждого символа запоминаем прописной или строчной
            flag_size = "big"
        key_number = i % len(keyword)  # индекс ключа, если слово длиннее слова-ключа
        new_order = (
                ord(plaintext[i].lower()) - key_code[key_number]
        )  # составляю новый индекс (зашифрованного эл-та)
        if new_order < 97:  # проверка чтобы не выпрыгивать за алфавит прописных латинских
            new_order += 26
        if flag_size == "big":
            ciphertext += (chr(new_order)).upper()
        else:
            ciphertext += chr(new_order)
    return ciphertext


def encrypt_vigenere(ciphertext, keyword):
    plaintext = ""
    key_code = []
    keyword = keyword.lower()
    for i in keyword:
        key_code.append(ord(i) - 97)  # добавляю в key_code ключ(сдвиг) для каждой буквы
    for i in range(len(ciphertext)):
        flag_size = "small"
        if (
                ciphertext[i] != ciphertext[i].lower()
        ):  # для каждого символа запоминаем прописной или строчной
            flag_size = "big"
        key_number = i % len(keyword)  # индекс ключа, если слово длиннее слова-ключа
        new_order = key_code[key_number] + ord(
            ciphertext[i].lower()
        )  # составляю новый индекс (зашифрованного эл-та)
        if new_order > 122:  # проверка чтобы не выпрыгивать за алфавит прописных латинских
            new_order -= 26
        if flag_size == "big":
            plaintext += (chr(new_order)).upper()
        else:
            plaintext += chr(new_order)
        return plaintext
