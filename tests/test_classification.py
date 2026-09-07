from desp.desp_core import calculer_desp

def test_classification_recipient_gaz_g1():
    res = calculer_desp(
        type_eq="Récipients",
        fluide="Air comprimé",
        etat="Gaz",
        ps=10,
        v=50,
        dn=None
    )
    assert res["groupe"] == 2
    assert res["tableau"] == 2
    assert res["categorie"] in ["I", "II", "III", "RÈGLES DE L'ART"]



def test_classification_tuyauterie_liquide_g2():
    res = calculer_desp(
        type_eq="Tuyauteries",
        fluide="Eau douce",
        etat="Liquide",
        ps=8,
        v=None,
        dn=150
    )
    assert res["groupe"] == 2
    assert res["tableau"] == 9
    assert res["categorie"] in ["I", "II", "III", "RÈGLES DE L'ART"]



