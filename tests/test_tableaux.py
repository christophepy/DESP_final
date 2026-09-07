from desp.desp_tableaux import determiner_tableau

def test_tableau_recipient_g1():
    assert determiner_tableau("Récipients", 1, "Gaz") == 1

def test_tableau_recipient_g2():
    assert determiner_tableau("Récipients", 2, "Gaz") == 2

def test_tableau_liquide_g1():
    assert determiner_tableau("Récipients", 1, "Liquide") == 3

def test_tableau_tuyauterie_g2():
    assert determiner_tableau("Tuyauteries", 2, "Gaz") == 7
