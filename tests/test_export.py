import os
from desp.desp_export import exporter_rapport

def test_export(tmp_path):
    resultats = {
        "type_eq": "Récipients",
        "fluide": "Air compeimé",
        "etat": "Gaz",
        "ps": 10,
        "v": 50,
        "dn": None,
        "tableau": 1,
        "groupe": 1,
        "categorie": "II",
        "x": 50,
        "label_x": "Volume (V)"
    }

    excel, pdf = exporter_rapport(resultats, tmp_path, "rapport_test")

    assert os.path.exists(excel)
    assert os.path.exists(pdf)

