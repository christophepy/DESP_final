**DESP — Classification DESP, Graphique & Rapport réglementaire**

    DESP est une application Python permettant :
        - la classification réglementaire DESP (Directive Équipements Sous Pression),
        - la visualisation graphique du point de fonctionnement,
        - la génération d’un rapport réglementaire (Excel + PDF),
        - une interface graphique PyQt6 ergonomique et modulaire.

    Ce projet est conçu pour un usage professionnel, industriel, et pédagogique.


**FONCTIONNALITES**

    Elles permettent 
        - la détermination du groupe du fluide (liquie ou gaz, groupe 1 ou 2)
        - la sélection automatique du tableau réglementaire
        - le calcul de la catégorie DESP (I, II, III, IV)
        - les implications réglementaires
    

**GRAPHIQUE DESP**

    - Visualisation du tableau applicable
    - affichage du point de fonctionnement
    - rapport des implications réglementaires simplifié
    - export Excel et export pdf

**INTERFACE PyQt6**

    - onglet Classification
    - onglet Graphique DESP
    - onglet Résultats / Rapport

**INSTALLATION**

    - via pip (PyPI)
        *Code*
        pip install desp
    - via Poetry (GitHub)
        *Code*
        git clone https://github.com/christophepy/DESP_final.git
        cd DESP_final
        poetry install


**UTILISATION**

    Lancer l’application:
        *Code*
            desp
    ou :
        *Code*
            poetry run python -m desp.main


**STRUCTURE DU PROJET**

    *Code*
        desp/
            main.py
            desp_core.py
            desp_excel.py
            desp_export.py
            desp_graphique.py
            desp_graphs.py
            desp_groups.py
            desp_tableaux.py
            desp_categories.py
            desp_validation.py
            desp_rapport.py
            data/
                desp_table.csv
                desp_table.xlsx
            ui/
                onglet_classification.py
                onglet_graphique.py
                onglet_resultats.py


**TESTS**

    Le dossier tests/ couvre :
        - la classification,
        - la validation,
        - les tableaux réglementaires,
        - les catégories,
        - les implications réglementaires,
        - le moteur graphique,
        - l'export Excel/PDF.

    Exécution :
        *Code*
            pytest
        ou :
        *Code*
            poetry run pytest


**DEPENDANCES PRINCIPALES**

    - Python ≥ 3.11,
    - PyQt6,
    - pandas,
    - matplotlib,
    - openpyxl,
    - reportlab.


**LICENCE**

    Ce projet est sous licence MIT.


**LIENS**

    GitHub : https://github.com/christophepy/DESP_final

    Documentation : docs/ dans le dépôt.
    PyPI : (sera actif après publication).


**CONTRIBUTIONS**

    Les contributions sont les bienvenues :
        - issues, pull requests, suggestions d’amélioration.


**CONTEXTE INDUSTRIEL**

    Ce logiciel est conçu pour :
        - les bureaux d’études,
        - les ingénieurs procédés,
        - les responsables conformité,
        - les formations techniques.

    Il permet une classification DESP fiable, rapide, traçable, et exportable, les partieimplications réglementaires étant à developper.
