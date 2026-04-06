import string

ALPHABET_UPPER = string.ascii_uppercase
ALPHABET_LOWER = string.ascii_lowercase


def decalage_lettre(lettre: str, cle: int) -> str:
    if lettre.isupper():
        alphabet = ALPHABET_UPPER
    elif lettre.islower():
        alphabet = ALPHABET_LOWER
    else:
        return lettre

    indice = alphabet.index(lettre)
    nouvel_indice = (indice + cle) % len(alphabet)
    return alphabet[nouvel_indice]


def chiffrement_cesar(message: str, cle: int) -> str:
    cle = cle % 26
    return ''.join(decalage_lettre(lettre, cle) for lettre in message)


def dechiffrement_cesar(message: str, cle: int) -> str:
    return chiffrement_cesar(message, -cle)


def attaque_brute(message: str) -> dict[int, str]:
    return {cle: dechiffrement_cesar(message, cle) for cle in range(26)}


# Détection par mot français
def score_francais(texte: str) -> int:
    texte = texte.upper()
    mots_courants = [
        "LE", "LA", "DE", "ET", "UN", "UNE",
        "BONJOUR", "SALUT", "JE", "TU", "IL", "ELLE", "NOUS", "VOUS", "ILS", "ELLES",
        "EST", "SONT", "AVEC", "POUR", "DANS", "SUR", "SOUS", "ENTRE", "PAR", "COMME", "COMMENT",
        "QUAND", "OÙ", "POURQUOI", "PARCE QUE", "SI", "ALORS", "MAIS", "OU", "ET", "NI", "CA", "CE",
        "CET", "CETTE", "CES", "MON", "TON", "SON", "NOTRE", "VOTRE", "LEUR", "MES", "TES", "SES", "NOS", "VOS", "LEURS"
    ]
    return sum((10 + len(mot)) for mot in mots_courants if mot in texte)


def attaque_brute_mot_francais(message: str) -> tuple[int, str]:
    meilleur_score = -1
    meilleur_cle = 0
    meilleur_message = ""
    for cle in range(26):
        message_clair = dechiffrement_cesar(message, cle)
        score = score_francais(message_clair)
        if score > meilleur_score:
            meilleur_score = score
            meilleur_cle = cle
            meilleur_message = message_clair
    return meilleur_cle, meilleur_message


# Détection par analyse de fréquence des lettres
frequence_francais = {
    'E': 14.7, 'A': 7.6, 'S': 7.9, 'T': 7.0,
    'I': 7.5, 'N': 7.1, 'R': 6.5, 'U': 6.3,
    'L': 5.5, 'O': 5.2, 'D': 3.6, 'M': 2.7,
    'P': 2.5, 'C': 3.3, 'V': 1.6, 'Q': 1.4,
    'F': 1.1, 'B': 0.9, 'G': 1.0, 'H': 0.8,
    'J': 0.6, 'X': 0.4, 'Y': 0.3, 'Z': 0.1,
    'K': 0.05, 'W': 0.04
}

# Calcul de la fréquence des lettres dans un message donné
def frequence_message(message: str) -> dict[str, float]:
    message = message.upper()
    total = 0
    occurence: dict[str, int] = {}
    for lettre in message:
        if lettre.isalpha():
            occurence[lettre] = occurence.get(lettre, 0) + 1
            total += 1

    if total == 0:
        return {}

    return {lettre: (count / total) * 100 for lettre, count in occurence.items()}


def score_frequence_message(message: str) -> float:
    freq_message = frequence_message(message)
    return sum(abs(freq_message.get(lettre, 0) - frequence_francais[lettre]) for lettre in frequence_francais)


def attaque_brute_frequence_lettre(message: str) -> tuple[int, str]:
    meilleur_score = float('inf')
    meilleur_cle = 0
    meilleur_message = ""
    for cle in range(26):
        message_clair = dechiffrement_cesar(message, cle)
        score = score_frequence_message(message_clair)
        if score < meilleur_score:
            meilleur_score = score
            meilleur_cle = cle
            meilleur_message = message_clair
    return meilleur_cle, meilleur_message

# attaque intelligente hybridant les deux méthodes
def attaque_intelligente(message: str) -> tuple[int, str]:
    meilleur_score = float('inf')
    meilleur_cle = 0
    meilleur_message = ""
    for cle in range(26):
        message_clair = dechiffrement_cesar(message, cle)
        score_mot = score_francais(message_clair)
        score_freq = score_frequence_message(message_clair)
        score_total = score_freq - score_mot
        if score_total < meilleur_score:
            meilleur_score = score_total
            meilleur_cle = cle
            meilleur_message = message_clair
    return meilleur_cle, meilleur_message, meilleur_score