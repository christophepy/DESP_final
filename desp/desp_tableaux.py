# desp_tableaux.py
# ---------------------------------------------------------
# Détermination du tableau DESP (Annexe II – Directive 2014/68/UE)
# ---------------------------------------------------------

def determiner_tableau(type_eq: str, groupe: int, etat: str) -> int:
    """
    Détermine le numéro du tableau DESP (1 à 9) selon :
    - type d'équipement : Récipients / Générateurs / Tuyauteries
    - groupe de fluide : 1 ou 2
    - état du fluide : Gaz / Liquide

    Retourne :
        Un entier entre 1 et 9 correspondant au tableau de l'annexe II.
    """

    # Récipients
    if type_eq == "Récipients":
        if etat == "Gaz":
            return 1 if groupe == 1 else 2
        else:
            return 3 if groupe == 1 else 4

    # Générateurs de vapeur
    if type_eq == "Générateurs":
        return 5

    # Tuyauteries
    if type_eq == "Tuyauteries":
        if etat == "Gaz":
            return 6 if groupe == 1 else 7
        else:
            return 8 if groupe == 1 else 9

    # Sécurité : cas non prévu
    return None
