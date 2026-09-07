# Installation

## Prérequis

- Python 3.11
- Poetry
- Git

## Installation du projet

```bash
git clone https://github.com/<ton-repo>/desp.git
cd desp
poetry install


docs/installation.md

markdown
# Installation — DESP (Classification DESP + Graphique + Rapport)

Ce document explique comment installer et exécuter l’application **DESP** depuis GitHub ou via pip lorsque le package sera publié sur PyPI.

---

## 1. Prérequis

### Python
DESP nécessite **Python 3.11 ou supérieur**.

Vérifier votre version :

```bash
python --version
pip
pip doit être installé :

bash
pip --version
Poetry (installation via GitHub)
Poetry permet une installation propre et isolée.

Installer Poetry :

bash
curl -sSL https://install.python-poetry.org | python3 -
Vérifier :

bash
poetry --version
2. Installation via GitHub (version de développement)
Cloner le dépôt :

bash
git clone https://github.com/christophepy/DESP_final.git
cd DESP_final
Installer les dépendances :

bash
poetry install
Activer l’environnement :

bash
poetry shell
3. Installation via PyPI (lorsque publié)
bash
pip install desp
Mettre à jour :

bash
pip install --upgrade desp
4. Lancer l'application
Via PyPI
bash
desp
Via GitHub / Poetry
bash
poetry run python -m desp.main
5. Vérification de l'installation
Tester l’import Python
python
import desp
print("DESP installé avec succès")
Vérifier les dépendances principales
Python ≥ 3.11

PyQt6

pandas

matplotlib

openpyxl

reportlab

6. Dépannage
PyQt6 ne s’installe pas
Assurez-vous d’utiliser Python 3.11+.

Le script desp n’est pas reconnu
Réinstaller :

bash
pip install desp --force-reinstall
Ou via Poetry :

bash
poetry install
poetry run desp
Problème d’environnement Poetry
Réinitialiser :

bash
poetry env remove python
poetry install
7. Désinstallation
Via pip
bash
pip uninstall desp
Via GitHub
Supprimer simplement le dossier :

bash
rm -rf DESP_final
8. Ressources
Dépôt GitHub : https://github.com/YannickDev/DESP_final

Documentation : dossier docs/

PyPI : sera actif après publication