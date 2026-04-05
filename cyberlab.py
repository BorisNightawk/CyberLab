from interface import menu
from chiffrement import cesar
from chiffrement import vigenere
from analyse import passeword

while True:
    menu.afficher_menu()
    choix = input("Quel Module souhaitez-vous utiliser ? :\t")
    if choix == "1":
        print("\nModule du chiffrement César chargé\n")
        message = input("Entrez le message à chiffrer :\t").upper()
        cle = int(input("Entrez la clé de chiffrement :\t"))
        message_chiffre_cesar = cesar.chiffrement_cesar(message, cle)
        print(f"Le message chiffré est : {message_chiffre_cesar}.")

    elif choix == '2':
        print("\nModule déchiffrement César chargé\n")
        message = input("Entrez le message à déchiffrer :\t").upper()
        cle = int(input("Entrez la clé de déchiffrement :\t"))
        message_dechiffre_cesar = cesar.dechiffrement_cesar(message, cle)
        print(f"Le message déchiffré est : {message_dechiffre_cesar}.")

    elif choix == "3":
        print("\nModule du chiffrement Vigenère chargé")
        message = input("Entrez le message à chiffrer :\t").upper()
        cle = input("Entrez la clé de chiffrement :\t").upper()
        message_chiffre_vig = vigenere.chiffrement_vigenere(message, cle)
        print(f"Le message chiffré est : {message_chiffre_vig}.")

    elif choix == "4":
        print("\nModule du déchiffrement Vigenère chargé")
        message = input("Entrez le message à déchiffrer :\t").upper()
        cle = input("Entrez la clé de déchiffrement :\t").upper()
        message_dechiffre_vig = vigenere.dechiffrement_vigenere(message, cle)
        print(f"Le message déchiffré est : {message_dechiffre_vig}.")

    elif choix == "5":
        print("\nModule d'analyse de mot de passe chargé")
        mdp = input("Veuillez entrer votre mot de passe :\t")
        score, niveau, recommandations = passeword.analyse_passeword(mdp)
        print(f"\nScore : {score}/100")
        print(f"\nNiveau : {niveau}")
        if recommandations:
            print("\nRecommandations :")
            for recom in recommandations:
                print(f"- {recom}\n")
    
    elif choix == '6':
        print("\nModule attaque brute force César chargé")
        message = input("Entrez le message à décrypter :\t").upper()
        messages = cesar.attaque_brute(message)
        for cle in messages:
            print(f"Clé {cle} : {messages[cle]}.\n")
        meilleur_cle, message_clair = cesar.attaque_brute_mot_francais(message)
        print(f"La clé probable est : {meilleur_cle}")
        print(f"Le message probable est : {message_clair}.")

    elif choix == '7':
        print("\nModule Cryptanalyse César analyse par fréquence chargé")
        message = input("Entrez le message à décrypter :\t").upper()
        cle, message_clair = cesar.attaque_brute_frequence_lettre(message)
        print(f"Clé probable : {cle}")
        print(f"Message probable : {message_clair}.")
        
    elif choix == '8':
        print("\nModule Attaque intelligente hybridant les deux méthodes chargé")
        message = input("Entrez le message à décrypter :\t").upper()
        cle, message_clair, score = cesar.attaque_intelligente(message)
        print(f"Clé probable : {cle}")
        print(f"Message probable : {message_clair}.")
        print(f"Score : {score:.2f}")

    elif choix == "0":
        print("\nMerci d'avoir consulté le programme!")
        break
    else:
        print("\nVotre choix est invalide.\nVeuillez reconsulter le menu.")