from desp.desp_validation import (
    valider_ps, valider_v, valider_dn,
    valider_type_eq, valider_fluide,
    valider_etat, valider_parametres
)

def test_valider_ps():
    assert valider_ps(10)[0]
    assert not valider_ps(-1)[0]

def test_valider_v():
    assert valider_v(5)[0]
    assert not valider_v(0)[0]

def test_valider_dn():
    assert valider_dn(50)[0]
    assert not valider_dn(-10)[0]

def test_valider_type_eq():
    assert valider_type_eq("Récipients")[0]
    assert not valider_type_eq("Inconnu")[0]

def test_valider_fluide():
    assert valider_fluide("Air comprimé")[0]
    assert not valider_fluide("")[0]

def test_valider_etat():
    assert valider_etat("Gaz")[0]
    assert not valider_etat("Plasma")[0]

def test_valider_parametres_ok():
    ok, err = valider_parametres(
        "Récipients", "Air comprimé", "Gaz", 10, 50, None
    )
    assert ok

def test_valider_parametres_bad():
    ok, err = valider_parametres(
        "Récipients", "Air comprimé", "Gaz", -1, 50, None
    )
    assert not ok
