# desp_groups.py
# ------------------------------------------------------------
# Détermination du groupe de fluide (1 ou 2)
# ------------------------------------------------------------

import pandas as pd


def determiner_fluide_groupe(df: pd.DataFrame, fluide: str, etat: str) -> int:
    """
    Détermine le groupe du fluide (1 ou 2) à partir du DataFrame DESP.
    Le DataFrame doit contenir les colonnes :
        - Fluides
        - Etat
        - Groupe

    Paramètres :
        df     : DataFrame chargé depuis DESP.ods
        fluide : nom du fluide (str)
        etat   : Gaz / Liquide

    Retour :
        int : groupe 1 ou 2
    """

    # Normalisation des entrées
    fluide_norm = fluide.strip().lower()
    etat_norm = etat.strip().lower()

    # Normalisation du DataFrame
    df_norm = df.copy()
    df_norm["Fluides"] = df_norm["Fluides"].astype(str).str.strip().str.lower()
    df_norm["Etat"] = df_norm["Etat"].astype(str).str.strip().str.lower()

    # Filtrage fluide
    df_fluide = df_norm[df_norm["Fluides"] == fluide_norm]
    if df_fluide.empty:
        raise ValueError(f"Fluide inconnu : {fluide}")

    # Filtrage état
    df_etat = df_fluide[df_fluide["Etat"] == etat_norm]
    if df_etat.empty:
        raise ValueError(f"État '{etat}' non trouvé pour le fluide '{fluide}'.")

    # Extraction du groupe
    groupe = df_etat["Groupe"].iloc[0]

    try:
        groupe = int(groupe)
    except Exception:
        raise ValueError(f"Groupe invalide dans le fichier : {groupe}")

    if groupe not in (1, 2):
        raise ValueError(f"Groupe non conforme (doit être 1 ou 2) : {groupe}")

    return groupe
