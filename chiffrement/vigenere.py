import string
alphabet = string.ascii_uppercase

def chiffrement_vigenere(message: str, cle: str) -> str:
    message_chiffre = ""
    cle = cle.upper()
    for i in range(len(message)):
        if message[i] in alphabet:
            indice_lettre = alphabet.index(message[i])
            indice_cle = alphabet.index(cle[i % len(cle)])
            indice_chiffre = (indice_lettre + indice_cle) % len(alphabet)
            message_chiffre += alphabet[indice_chiffre]
        else:
            message_chiffre += message[i]
    return message_chiffre

def dechiffrement_vigenere(message: str, cle: str) -> str:
    message_dechiffre = ""
    cle = cle.upper()
    for i in range(len(message)):
        if message[i] in alphabet:
            indice_lettre = alphabet.index(message[i])
            indice_cle = alphabet.index(cle[i % len(cle)])
            indice_dechiffre = (indice_lettre - indice_cle) % len(alphabet)
            message_dechiffre += alphabet[indice_dechiffre]
        else:
            message_dechiffre += message[i]
    return message_dechiffre