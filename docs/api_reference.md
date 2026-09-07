# Référence API — Projet DESP  
Classification • Graphique • Rapport • Export

Ce document décrit l’API interne du projet : modules, fonctions, classes, paramètres et valeurs retournées.  
Il sert de référence technique pour les développeurs et pour la maintenance du projet.

---

## 1. Module `desp_categories.py`

### Fonction : `determiner_categorie(tableau: int, ps: float, v: float = None, dn: float = None) -> str`

Détermine la catégorie DESP selon les tableaux réglementaires (1 à 9).

#### Paramètres
    - `tableau` : numéro du tableau DESP (1 à 9)
    - `ps` : pression maximale admissible (bar)
    - `v` : volume (litres) — tableaux 1 à 5
    - `dn` : diamètre nominal (mm) — tableaux 6 à 9

#### Retour
Chaîne parmi :
    - `"I"`
    - `"II"`
    - `"III"`
    - `"IV"`
    - `"RÈGLES DE L'ART"`
    - `"DESP non applicable"`
    - `"Erreur: tableau inconnu"`

#### Notes
    - Le calcul utilise `PS·V` ou `PS·DN` selon le tableau.
    - Les règles suivent strictement la directive DESP 2014/68/UE.

---

## 2. Module `desp_graphique.py`

### Fonction : `afficher_point_de_fonctionnement(tableau: int, x: float, ps: float, label_x: str) -> (Figure, Axes)`

Génère le graphique réglementaire correspondant au tableau DESP.

#### Paramètres
    - `tableau` : numéro du tableau DESP
    - `x` : valeur horizontale (V ou DN)
    - `ps` : pression maximale admissible
    - `label_x` : `"V"` ou `"DN"`

#### Retour
    - `fig` : objet `matplotlib.figure.Figure`
    - `ax` : objet `matplotlib.axes.Axes`

#### Notes
    - Le point de fonctionnement est affiché sur le graphique.
    - Les zones I, II, III, IV et Règles de l’Art sont représentées.
    - La toolbar Matplotlib (zoom, pan, reset, save) est intégrée via `OngletGraphique`.

---

## 3. Module `desp_rapport.py`

### Dictionnaire : `DESP_CATEGORIES`

Structure contenant les implications réglementaires pour chaque catégorie.

#### Clés
    - `"risque"`
    - `"marquage_CE"`
    - `"organisme_notifie"`
    - `"modules"`
    - `"implications"`
    - `"exemples"`

#### Catégories disponibles
    - `"I"`, `"II"`, `"III"`, `"IV"`
    - `"RÈGLES DE L'ART"`
    - `"DESP NON APPLICABLE"`

---

### Fonction : `resume_categorie(categorie: str) -> dict`

Retourne les implications réglementaires pour une catégorie DESP.

#### Paramètres
    - `categorie` : catégorie DESP (chaîne)

#### Retour
Dictionnaire structuré contenant :
    - niveau de risque  
    - marquage CE  
    - rôle de l’organisme notifié  
    - modules applicables  
    - implications réglementaires  
    - exemples typiques  

#### Notes
    - Normalisation automatique ("RÈGLES DE L'ART")
    - Erreur si la catégorie est inconnue.

---

## 4. Module `desp_core.py`

### Fonction : `calculer_desp(parametres: dict) -> dict`
Calcule l’ensemble des résultats DESP à partir des paramètres utilisateur.

#### Paramètres
Dictionnaire contenant :
    - `type_eq`
    - `fluide`
    - `etat`
    - `groupe`
    - `ps`
    - `v` ou `dn`

#### Retour
Dictionnaire :
    - `tableau`
    - `groupe`
    - `categorie`
    - `x` (V ou DN)
    - `label_x`
    - `ps`
    - `v` ou `dn`

---

## 5. Module GUI — `onglet_classification.py`

### Classe : `OngletClassification(QWidget)`

Gère l’onglet de saisie des paramètres DESP.

#### Méthodes principales
    - `valider_parametres()`  
    Valide les champs et déclenche le calcul DESP.

    - `get_parametres()`  
    Retourne les paramètres sous forme de dictionnaire.

---

## 6. Module GUI — `onglet_graphique.py`

### Classe : `OngletGraphique(QWidget)`

Affiche le graphique DESP.

#### Méthodes principales
    - `afficher_graphique(tableau, x, ps, label_x)`  
    Génère et affiche le graphique Matplotlib.  
    Inclut la toolbar (zoom, pan, reset, save).

---

## 7. Module GUI — `onglet_resultats.py`

### Classe : `OngletResultats(QWidget)`

Affiche les résultats DESP et les implications réglementaires.

#### Méthodes principales
    - `afficher_resultats(r: dict)`  
    Affiche les résultats calculés (catégorie, PS, V/DN, groupe…).

    - `_exporter()`  
    Exporte les résultats en Excel + PDF via `callback_export`.

---

## 8. Module `desp_export.py`

### Fonction : `exporter_excel(nom: str, data: dict)`

Génère un fichier Excel contenant :
    - paramètres  
    - résultats  
    - tableau réglementaire  
    - point de fonctionnement  

### Fonction : `exporter_pdf(nom: str, data: dict)`

Génère un rapport PDF DESP.

---

## 9. Tests — `tests/`

Structure réelle du dossier (selon ton dépôt GitHub) :

    - `test_categorie.py`  
    Tests du moteur de classification DESP (tableaux 1 à 9, PS·V, PS·DN, Règles de l’Art, DESP non applicable).
    - `test_classification.py`  
    Tests de la logique de validation des paramètres (type d’équipement, fluide, état, groupe, PS, V/DN).
    - `test_export.py`  
    Tests des exports Excel et PDF (structure des fichiers, cohérence des données).
    - `test_graphs.py`  
    Tests de génération des graphiques Matplotlib (zones, point de fonctionnement, cohérence des axes).
    - `test_implications.py`  
    Tests du module `desp_rapport.py` (catégories I–IV, RÈGLES DE L’ART, DESP NON APPLICABLE).
    - `test_tableaux.py`  
    Tests de la sélection du tableau DESP selon fluide, état, groupe, type d’équipement.
    - `test_validation.py`  
    Tests de la logique interne de validation (cohérence des paramètres, erreurs attendues, cas limites).

### Commande d’exécution

```bash
pytest -q
