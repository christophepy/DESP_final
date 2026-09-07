markdown
# Guide d'utilisation — DESP (Classification DESP + Graphique + Rapport)

Ce document explique comment utiliser l'application **DESP**, son interface PyQt6, et les différentes fonctionnalités de classification, graphique et rapport réglementaire.

---
**1. Lancer l'application**

    Via PyPI
        ```bash
        desp
    Via GitHub / Poetry
        bash
        poetry run python -m desp.main

    Une fenêtre PyQt6 s'ouvre : elle contient les trois onglets principaux de l'application.

**2. Interface générale**

    L'application se compose de trois onglets :

        Classification
        Graphique DESP
        Résultats / Rapport

    Chaque onglet correspond à une étape du processus réglementaire DESP.

**3. Onglet Classification**

    Cet onglet permet de saisir les paramètres réglementaires nécessaires au calcul DESP.

    **3.1 Paramètres à renseigner**
        Type d'équipement  
            Récipient, générateur ou Tuyauterie.
        Fluide  
            Exemple : Air comprimé, Eau douce, Azote, Vapeur, etc.
        État du fluide  
            Liquide ou Gaz.
        Groupe du fluide  
            Déterminé automatiquement selon la réglementation (Groupe 1 ou 2).
        PS (Pression maximale admissible)  
            En bar.
        V (Volume) pour les récipients
            En litres.
        DN (Diamètre nominal) pour les tuyauteries
            Pas d'unité.

    **3.2 Fonctionnement**
        Une fois les paramètres saisis :
            le groupe du fluide est déterminé automatiquement,
            le tableau réglementaire applicable est sélectionné,
            la catégorie DESP est calculée (I, II, III, IV),
            les implications réglementaires sont générées (module en développement).

        Un bouton Valider permet de lancer le calcul.

**4. Onglet Graphique DESP**

    Cet onglet affiche le graphique réglementaire correspondant au tableau applicable.

    **4.1 Contenu du graphique**
        Le tableau DESP (zones I, II, III, IV)
        Le point de fonctionnement (PS, V ou DN)
        La zone réglementaire dans laquelle se situe l'équipement
        Un résumé des implications réglementaires

    **4.2 Actions disponibles**
        Zoom / dézoom

**5. Onglet Résultats / Rapport**

    Cet onglet regroupe toutes les informations calculées :

    **5.1 Résultats affichés**
        Type d'équipement
        Fluide et état
        Groupe réglementaire
        Tableau applicable
        Catégorie DESP
        Implications réglementaires (simplifiées)
        Point de fonctionnement

    **5.2 Export**
        Deux exports sont disponibles :
        Export Excel  
            Génère un fichier .xlsx contenant :
                les paramètres,
                les résultats,
                le tableau réglementaire,
                le point de fonctionnement.
        Export PDF  
            Génère un rapport réglementaire complet.

**6. Exemples d'utilisation**

    **6.1 Récipient sous pression**
        Paramètres :
            Fluide : Air comprimé
            État : Gaz
            PS : 12 bar
            Volume : 0.5 l
        Résultats :
            Groupe : 2
            Tableau : Gaz — Récipient - Groupe 2 : tableau 2
            Catégorie : Règles de l'art
            Graphique : point dans zone Règles de l'art
        Rapport : disponible en Excel + PDF

    **6.2 Tuyauterie**
        Paramètres :
            Fluide : Eau douce
            État : Liquide
            PS : 16 bar
            DN : 500
        Résultat :
            Groupe : 2
            Tableau : Liquide — Tuyauterie - groupe 2 : tableau 9
            Catégorie : II
        Rapport : disponible

**7. Dépannage**

    L'application ne se lance pas
        Vérifier l'installation :
            bash
            pip install desp
        Ou via GitHub :
            bash
            poetry install
            poetry run python -m desp.main
    Le graphique ne s'affiche pas
        Assurez-vous que les paramètres sont complets et valides.
    L'export PDF échoue
        Vérifier que reportlab est installé :
            bash
            pip install reportlab

**8. Ressources**

    Dépôt GitHub : https://github.com/christophepy/DESP_final
    Documentation : dossier docs/
    Installation : docs/installation.md
    Tests : docs/tests.md