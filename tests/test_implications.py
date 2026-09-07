import pytest
from desp.desp_rapport import resume_categorie

def test_resume_categorie_I():
    data = resume_categorie("I")
    assert data["risque"] == "Faible"
    assert "A" in data["modules"]

def test_resume_categorie_IV():
    data = resume_categorie("IV")
    assert data["risque"] == "Très élevé"
    assert "H1" in data["modules"]

def test_resume_categorie_invalide():
    with pytest.raises(ValueError):
        resume_categorie("Z")
