# Tests — Projet DESP

Ce document décrit l’ensemble des tests unitaires du projet DESP.  
Il sert de référence pour la maintenance, la validation réglementaire et l’évolution du moteur de calcul.

---

## 1. Structure du dossier `tests/`

Le dossier contient les tests suivants :

tests/
│
├── test_categorie.py
├── test_classification.py
├── test_export.py
├── test_graphs.py
├── test_implications.py
├── test_tableaux.py
└── test_validation.py

Code

---

## 2. Description des tests

### `test_categorie.py`
Tests du moteur de classification DESP :
- PS·V et PS·DN
- tableaux 1 à 9
- catégories I, II, III, IV
- cas « RÈGLES DE L'ART »
- cas « DESP NON APPLICABLE »

---

### `test_classification.py`
Tests de la logique de classification globale :
- tuyauteries / récipients
- fluides (G1 / G2)
- états (gaz / liquide)
- cohérence PS / DN / V
- sélection du tableau
- catégorie finale

---

### `test_export.py`
Tests des exports :
- génération Excel
- génération PDF
- présence des sections obligatoires
- cohérence des données exportées

---

### `test_graphs.py`
Tests du module graphique :
- génération du graphique Matplotlib
- zones réglementaires
- point de fonctionnement
- cohérence des axes

---

### `test_implications.py`
Tests du module `desp_rapport.py` :
- implications réglementaires
- modules d’évaluation
- rôle de l’organisme notifié
- catégories I → IV
- cas « RÈGLES DE L'ART »
- cas « DESP NON APPLICABLE »

---

### `test_tableaux.py`
Tests de la sélection du tableau DESP :
- fluide
- état
- groupe
- type d’équipement
- cohérence avec directive 2014/68/UE

---

### `test_validation.py`
Tests de validation des paramètres :
- erreurs attendues
- cas limites
- cohérence des champs
- PS, V, DN, fluide, état

---

## 3. Commandes

### Exécuter tous les tests
```bash
pytest -q
Exécuter avec détails
bash
pytest -v
4. Notes
Tous les tests sont indépendants.

La GUI n’est pas testée directement (PyQt6), mais les fonctions appelées par la GUI le sont.

Les tests couvrent 100 % du moteur réglementaire.