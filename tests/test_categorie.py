from desp.desp_categories import determiner_categorie

def test_categorie_tableau_1():
    cat = determiner_categorie(1, ps=10, v=50)
    assert cat in ["I", "II", "III", "IV", "RÈGLES DE L’ART"]

def test_categorie_tableau_6():
    cat = determiner_categorie(6, ps=5, dn=40)
    assert cat in ["I", "II", "III", "RÈGLES DE L’ART"]
