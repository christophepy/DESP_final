# desp_excel.py
# ---------------------------------------------------------
# Chargement du fichier DESP.ods via importlib.resources
# ---------------------------------------------------------

import pandas as pd
from importlib.resources import files


def charger_donnees():
    """
    Charge le fichier DESP.ods situé dans desp/data/.
    Utilise importlib.resources pour garantir :
    - compatibilité packaging
    - compatibilité pip install
    - compatibilité tests
    - compatibilité CI/CD
    - compatibilité Windows / Linux / macOS
    """

    # Localisation du fichier dans le package
    fichier = files("desp.data").joinpath("DESP.ods")

    try:
        df = pd.read_excel(fichier, engine="odf")
    except Exception as e:
        raise ImportError(
            f"Impossible de lire le fichier DESP.ods : {e}\n"
            "Vérifiez que le fichier est présent dans desp/data/"
        )

    return df





