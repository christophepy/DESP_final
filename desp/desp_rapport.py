# desp_rapport.py
# ---------------------------------------------------------
# Résumé des implications réglementaires DESP par catégorie
# ---------------------------------------------------------

DESP_CATEGORIES = {
    "I": {
        "risque": "Faible",
        "marquage_CE": True,
        "organisme_notifie": "Non obligatoire",
        "modules": ["A"],
        "implications": [
            "Auto-certification possible",
            "Documentation technique simplifiée",
            "Essais internes autorisés",
            "Conception selon normes harmonisées recommandée"
        ],
        "exemples": [
            "Petits réservoirs d'air",
            "Tuyauteries basse pression DN > 25"
        ]
    },

    "II": {
        "risque": "Modéré",
        "marquage_CE": True,
        "organisme_notifie": "Intervention partielle",
        "modules": ["A2", "D1", "E1"],
        "implications": [
            "Contrôle de production ou contrôle final par organisme notifié",
            "Documentation technique renforcée",
            "Essais de pression obligatoires"
        ],
        "exemples": [
            "Récipients liquides PS·V moyen",
            "Tuyauteries gaz groupe 2 PS·DN > 1000"
        ]
    },

    "III": {
        "risque": "Élevé",
        "marquage_CE": True,
        "organisme_notifie": "Intervention importante",
        "modules": ["B + D", "B + F", "H"],
        "implications": [
            "Examen UE de type obligatoire",
            "Audit qualité du fabricant",
            "Contrôles non destructifs (RT, UT...)",
            "Soudeurs et procédures de soudage qualifiés",
            "Traçabilité des matériaux"
        ],
        "exemples": [
            "Chaudières vapeur > 110°C",
            "Récipients gaz groupe 1 PS·V élevé"
        ]
    },

    "IV": {
        "risque": "Très élevé",
        "marquage_CE": True,
        "organisme_notifie": "Intervention maximale",
        "modules": ["B + D", "B + F", "G", "H1"],
        "implications": [
            "Supervision complète par organisme notifié",
            "Examen complet du design",
            "Contrôles non destructifs systématiques",
            "Surveillance continue de la production",
            "Documentation technique exhaustive"
        ],
        "exemples": [
            "Réservoirs haute pression gaz groupe 1",
            "Tuyauteries liquides groupe 1 PS·DN très élevé"
        ]
    },

    # ---------------------------------------------------------
    # AJOUT : RÈGLES DE L'ART
    # ---------------------------------------------------------
    "RÈGLES DE L'ART": {
        "risque": "Très faible",
        "marquage_CE": False,
        "organisme_notifie": "Non requis",
        "modules": ["A (hors DESP)"],
        "implications": [
            "Équipement hors catégories I à IV",
            "Application des règles de l'art uniquement",
            "Pas de marquage CE DESP",
            "Pas d'intervention d'un organisme notifié"
        ],
        "exemples": [
            "Petits récipients gaz (PS·V < 50 bar·L)",
            "Petites tuyauteries (PS·DN < 1000)",
            "Équipements basse pression"
        ]
    },

    # ---------------------------------------------------------
    # AJOUT : DESP NON APPLICABLE
    # ---------------------------------------------------------
    "DESP NON APPLICABLE": {
        "risque": "Néant",
        "marquage_CE": False,
        "organisme_notifie": "Non requis",
        "modules": [],
        "implications": [
            "Équipement hors champ de la directive DESP",
            "Aucune exigence réglementaire DESP",
            "Pas de marquage CE"
        ],
        "exemples": [
            "Équipements PS < 0.5 bar",
            "Récipients très faibles volumes",
            "Tuyauteries très petits diamètres"
        ]
    }
}


def resume_categorie(categorie: str) -> dict:
    """
    Retourne un dictionnaire structuré contenant :
        - niveau de risque
        - marquage CE
        - rôle de l'organisme notifié
        - modules applicables
        - implications réglementaires
        - exemples typiques
    """

    # Normalisation
    cat = str(categorie).strip().upper()

    # Normalisation stricte : uniquement les deux formes possibles
    if cat == "RÈGLES DE L'ART" or cat == "REGLES DE L'ART":
        cat = "RÈGLES DE L'ART"

    if cat == "DESP NON APPLICABLE":
        cat = "DESP NON APPLICABLE"

    if cat not in DESP_CATEGORIES:
        raise ValueError(f"Catégorie DESP inconnue : {categorie}")

    return DESP_CATEGORIES[cat]


def afficher_resume(categorie: str):
    """
    Affiche un résumé lisible dans la console (mode CLI).
    Utilisé uniquement pour les tests ou exécutions directes.
    """
    data = resume_categorie(categorie)

    print(f"\n=== Catégorie DESP {categorie} ===")
    print(f"Niveau de risque : {data['risque']}")
    print(f"Marquage CE : {'Oui' if data['marquage_CE'] else 'Non'}")
    print(f"Organisme notifié : {data['organisme_notifie']}")
    print(f"Modules applicables : {', '.join(data['modules'])}")

    print("\nImplications :")
    for imp in data["implications"]:
        print(f"  - {imp}")

    print("\nExemples typiques :")
    for ex in data["exemples"]:
        print(f"  - {ex}")

