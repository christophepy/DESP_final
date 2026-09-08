# desp_categories.py
# ----------------------------------------------------------------
# Détermination de la catégorie DESP (I, II, III, IV ou Règles de l'Art)
# ----------------------------------------------------------------

def determiner_categorie(
    tableau: int,
    ps: float,
    v: float | None = None,
    dn: float | None = None
) -> str:
    """
    Détermine la catégorie DESP (I à IV, RÈGLES DE L'ART, ou non applicable)
    """

    # -------------------------------
    # Validation du tableau
    # -------------------------------
    if tableau not in range(1, 10):
        return "Erreur: tableau inconnu"

    # -------------------------------
    # Calcul du produit PS·V ou PS·DN
    # -------------------------------
    if tableau in [1, 2, 3, 4, 5]:
        if v is None:
            return "Erreur: volume V manquant pour tableau PS·V"
        prod = ps * v
        # mypy: à partir d'ici, v est garanti non-None
        assert isinstance(v, float)

    elif tableau in [6, 7, 8, 9]:
        if dn is None:
            return "Erreur: DN manquant pour tableau PS·DN"
        prod = ps * dn
        # mypy: à partir d'ici, dn est garanti non-None
        assert isinstance(dn, float)

    # ============================================================
    # TABLEAU 1 - Récipients de GAZ GROUPE 1
    # ============================================================
    if tableau == 1:
        if ps < 0.5:
            return "DESP non applicable"

        if v < 1:
            if ps <= 200:
                return "RÈGLES DE L'ART"
            elif ps <= 1000:
                return "III"
            else:
                return "IV"

        if prod <= 25:
            return "RÈGLES DE L'ART"
        elif prod <= 50:
            return "I"
        elif prod <= 200:
            return "II"
        elif prod <= 1000:
            return "III"
        else:
            return "IV"

    # ============================================================
    # TABLEAU 2 - Récipients de GAZ GROUPE 2
    # ============================================================
    if tableau == 2:
        if ps < 0.5:
            return "DESP non applicable"

        if v < 1:
            if ps <= 1000:
                return "RÈGLES DE L'ART"
            elif ps <= 3000:
                return "III"
            else:
                return "IV"

        if prod <= 50:
            return "RÈGLES DE L'ART"
        elif prod <= 200:
            return "I"
        elif prod <= 1000:
            return "II"
        elif (prod <= 3000 and v <= 750) or ps <= 4:
            return "III"
        else:
            return "IV"

    # ============================================================
    # TABLEAU 3 - Récipients de LIQUIDES GROUPE 1
    # ============================================================
    if tableau == 3:
        if ps < 0.5:
            return "DESP non applicable"

        if v < 1:
            if ps <= 500:
                return "RÈGLES DE L'ART"
            else:
                return "II"

        if prod <= 200:
            return "RÈGLES DE L'ART"
        elif ps <= 10 and v > 20:
            return "I"
        elif ps <= 500:
            return "II"
        else:
            return "III"

    # ============================================================
    # TABLEAU 4 - Récipients de LIQUIDES GROUPE 2
    # ============================================================
    if tableau == 4:
        if ps < 0.5:
            return "DESP non applicable"

        if v < 10:
            if ps <= 1000:
                return "RÈGLES DE L'ART"
            else:
                return "I"

        if (prod <= 10000 and v < 1000) or ps <= 10:
            return "RÈGLES DE L'ART"
        elif ps <= 500:
            return "I"
        else:
            return "II"

    # ============================================================
    # TABLEAU 5 - Générateurs de vapeur d'eau surchauffée
    # ============================================================
    if tableau == 5:
        if ps < 0.5:
            return "DESP non applicable"

        if v < 2:
            return "RÈGLES DE L'ART"

        if prod <= 50:
            return "I"
        elif prod <= 200 and ps < 32:
            return "II"
        elif prod <= 3000 and ps < 32 and v < 1000:
            return "III"
        else:
            return "IV"

    # ============================================================
    # TABLEAU 6 - Tuyauteries de GAZ GROUPE 1
    # ============================================================
    if tableau == 6:
        if ps < 0.5:
            return "DESP non applicable"

        if dn < 25:
            return "RÈGLES DE L'ART"
        elif prod < 1000 and dn < 100:
            return "I"
        elif prod < 3500 and dn < 350:
            return "II"
        else:
            return "III"

    # ============================================================
    # TABLEAU 7 - Tuyauteries de GAZ GROUPE 2
    # ============================================================
    if tableau == 7:
        if ps < 0.5:
            return "DESP non applicable"

        if dn < 32:
            return "RÈGLES DE L'ART"
        elif prod < 1000 and dn < 100:
            return "RÈGLES DE L'ART"
        elif prod < 3500 and dn < 250:
            return "I"
        elif prod < 5000 and dn < 250:
            return "II"
        else:
            return "III"

    # ============================================================
    # TABLEAU 8 - Tuyauteries de liquides GROUPE 1
    # ============================================================
    if tableau == 8:
        if ps < 0.5:
            return "DESP non applicable"

        if dn < 25:
            return "RÈGLES DE L'ART"
        elif prod < 2000:
            return "RÈGLES DE L'ART"
        elif ps < 10 and dn > 200:
            return "I"
        elif ps < 500:
            return "II"
        else:
            return "III"

    # ============================================================
    # TABLEAU 9 - Tuyauteries de liquides GROUPE 2
    # ============================================================
    if tableau == 9:
        if ps < 0.5:
            return "DESP non applicable"

        if dn < 200:
            return "RÈGLES DE L'ART"
        elif prod < 5000 and dn < 500:
            return "RÈGLES DE L'ART"
        elif prod > 5000 and dn < 500 and ps < 500:
            return "I"
        elif ps > 500:
            return "II"
        elif ps < 10 and dn > 500:
            return "RÈGLES DE L'ART"
        elif ps < 500 and dn > 500:
            return "I"
        else:
            return "II"

    # -------------------------------
    # Sécurité : cas non prévu
    # -------------------------------
    return "DESP non applicable"



