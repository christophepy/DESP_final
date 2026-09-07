# desp_validation.py
# ---------------------------------------------------------
# Validation des paramètres DESP
# ---------------------------------------------------------

def valider_ps(ps):
    """PS doit être un nombre positif."""
    if ps is None:
        return False, "La pression PS est manquante."
    try:
        ps = float(ps)
    except Exception:
        return False, "La pression PS doit être un nombre."
    if ps <= 0:
        return False, "La pression PS doit être strictement positive."
    return True, None


def valider_v(v):
    """V doit être un nombre positif (uniquement pour Récipients / Générateurs)."""
    if v is None:
        return False, "Le volume V est manquant."
    try:
        v = float(v)
    except Exception:
        return False, "Le volume V doit être un nombre."
    if v <= 0:
        return False, "Le volume V doit être strictement positif."
    return True, None


def valider_dn(dn):
    """DN doit être un nombre positif (uniquement pour Tuyauteries)."""
    if dn is None:
        return False, "Le diamètre DN est manquant."
    try:
        dn = float(dn)
    except Exception:
        return False, "Le diamètre DN doit être un nombre."
    if dn <= 0:
        return False, "Le diamètre DN doit être strictement positif."
    return True, None


def valider_type_eq(type_eq):
    """Type d'équipement doit être reconnu."""
    types_valides = ["Récipients", "Générateurs", "Tuyauteries"]
    if type_eq not in types_valides:
        return False, f"Type d'équipement invalide : {type_eq}"
    return True, None


def valider_fluide(fluide):
    """Fluide doit être renseigné."""
    if not fluide or fluide.strip() == "":
        return False, "Le fluide doit être renseigné."
    return True, None


def valider_etat(etat):
    """État doit être Liquide ou Gaz."""
    if etat not in ["Liquide", "Gaz"]:
        return False, "L'état du fluide doit être 'Liquide' ou 'Gaz'."
    return True, None


def valider_parametres(type_eq, fluide, etat, ps, v, dn):
    """
    Validation complète des paramètres utilisateur.
    Retourne (True, None) si tout est OK,
    sinon (False, message d’erreur).
    """

    # Type d'équipement
    ok, err = valider_type_eq(type_eq)
    if not ok: return ok, err

    # Fluide
    ok, err = valider_fluide(fluide)
    if not ok: return ok, err

    # État
    ok, err = valider_etat(etat)
    if not ok: return ok, err

    # Pression PS
    ok, err = valider_ps(ps)
    if not ok: return ok, err

    # Volume ou DN selon type
    if type_eq in ["Récipients", "Générateurs"]:
        ok, err = valider_v(v)
        if not ok: return ok, err

    if type_eq == "Tuyauteries":
        ok, err = valider_dn(dn)
        if not ok: return ok, err

    return True, None
