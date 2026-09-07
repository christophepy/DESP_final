# desp_core.py
# ----------------------------------------------------------------
# Calcul complet DESP : tableau, groupe, catégorie, point de fonctionnement
# ----------------------------------------------------------------

from desp.desp_tableaux import determiner_tableau
from desp.desp_groups import determiner_fluide_groupe
from desp.desp_categories import determiner_categorie
from desp.desp_excel import charger_donnees


def calculer_desp(type_eq: str, fluide: str, etat: str,
                  ps: float, v: float, dn: float) -> dict:
    """
    Calcule l'ensemble des résultats DESP :
    - groupe fluide
    - tableau DESP
    - catégorie DESP
    - point de fonctionnement (x = V ou DN)

    Retourne un dictionnaire prêt pour l'interface, le graphique et l'export.
    """

    # Chargement des données depuis DESP.ods
    df = charger_donnees()

    # Détermination du groupe fluide
    groupe = determiner_fluide_groupe(df, fluide, etat)

    # Détermination du tableau DESP
    tableau = determiner_tableau(type_eq, groupe, etat)

    # Détermination de la catégorie DESP
    categorie = determiner_categorie(tableau, ps, v, dn)

    # Détermination du point de fonctionnement
    if type_eq in ["Récipients", "Générateurs"]:
        x = v
        label_x = "V"
    else:
        x = dn
        label_x = "DN"

    return {
        "type_eq": type_eq,
        "fluide": fluide,
        "etat": etat,
        "ps": ps,
        "v": v,
        "dn": dn,
        "groupe": groupe,
        "tableau": tableau,
        "categorie": categorie,
        "x": x,
        "label_x": label_x
    }
