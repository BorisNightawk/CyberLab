import string
def analyse_passeword(passeword:str):
    score = 0
    longueur = len(passeword)
    recommandations = []
    # Analyse sur longueur
    if longueur >= 12:
        score += 30
    elif longueur >= 8:
        score += 15
    else:
        recommandations.append("Augmentez la longueur de votre mot de passe (minimum 12 caractères)")
    
    # Analyse sur lettre Majuscule
    if any(car.isupper() for car in passeword):
        score += 10
    else:
        recommandations.append("Ajoutez au moins une lettre majuscule")
    
    # Analyse sur lettre Miniscule
    if any(car.islower() for car in passeword):
        score += 10
    else:
        recommandations.append("Ajoutez au moins une lettre minuscule")
    
    # Analyse sur chiffre
    if any(car.isdigit() for car in passeword):
        score += 15
    else:
        recommandations.append("Ajoutez des chiffres")
    
    # Analyse sur des caractères spéciaux
    if any(car in string.punctuation for car in passeword):
        score += 20
    else:
        recommandations.append("Ajoutez des caractères spéciaux (!@#$€...)")
    
    # Evaluation sur répétition
    if longueur >= 12 and len(set(passeword)) > 6:
        score += 15
    
    # Classification
    if score < 40:
        niveau = "FAIBLE"
    elif score < 70:
        niveau = "MOYEN"
    else:
        niveau = "FORT"
    return score, niveau, recommandations
