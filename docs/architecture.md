# 📄 **docs/architecture.md**  
*(Version finale, claire, structurée, prête à coller)*

```markdown
# Architecture — Projet DESP

Ce document décrit l’architecture interne du projet DESP : modules, responsabilités, flux de données et interactions GUI ↔ moteur.

---

# 1. Vue d’ensemble

Le projet est structuré en trois couches :

+---------------------------+
|        Interface GUI      |
|  (PyQt6 : onglets)        |
+---------------------------+
|
v
+---------------------------+
|     Moteur DESP (core)    |
|  classification + tableau |
|  graphique + rapport      |
+---------------------------+
|
v
+---------------------------+
|      Exports (Excel/PDF)  |
+---------------------------+

Code

---

# 2. Modules principaux

## 2.1 `desp_core.py`
Moteur principal :
- sélection du tableau
- classification DESP
- détermination du groupe (G1/G2)
- construction du dictionnaire final
- appel du résumé réglementaire

Entrée : dictionnaire de paramètres  
Sortie : dictionnaire structuré

---

## 2.2 `desp_categories.py`
Classification réglementaire :
- tableaux 1 à 9
- calcul PS·V ou PS·DN
- catégories I → IV
- cas « RÈGLES DE L'ART »
- cas « DESP NON APPLICABLE »

---

## 2.3 `desp_graphique.py`
Graphique réglementaire :
- zones I → IV
- zone RÈGLES DE L'ART
- point de fonctionnement
- figure Matplotlib + axes

---

## 2.4 `desp_rapport.py`
Résumé réglementaire :
- dictionnaire `DESP_CATEGORIES`
- implications réglementaires
- modules d’évaluation
- rôle de l’organisme notifié
- normalisation stricte :
  - **uniquement “RÈGLES DE L'ART”**

---

## 2.5 `desp_export.py`
Exports :
- Excel (openpyxl)
- PDF (reportlab)
- intégration du graphique
- intégration des résultats

---

# 3. Interface graphique (PyQt6)

## 3.1 `onglet_classification.py`
- saisie des paramètres
- validation
- appel du moteur DESP

## 3.2 `onglet_graphique.py`
- affichage du graphique
- toolbar Matplotlib

## 3.3 `onglet_resultats.py`
- affichage des résultats
- affichage du résumé réglementaire
- export Excel/PDF

---

# 4. Flux de données

Utilisateur → OngletClassification → calculer_desp()
→ tableau, groupe, catégorie, x, ps
→ OngletGraphique → graphique
→ OngletResultats → résumé + export

Code

---

# 5. Tests

Les tests couvrent :
- catégorie
- classification
- tableaux
- implications réglementaires
- graphique
- exports
- validation

Voir : `docs/tests.md`

---

# 6. Notes importantes

- Normalisation stricte : **“RÈGLES DE L'ART” uniquement**
- Le moteur est pur, déterministe, testable
- La GUI ne doit jamais appeler directement les modules internes