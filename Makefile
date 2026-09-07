# ============================================================
# Makefile — Projet DESP (Directive 2014/68/UE)
# ============================================================

# Commandes Poetry
POETRY = poetry
RUN = $(POETRY) run

# Répertoires
SRC = desp
TESTS = tests

# ============================================================
# Installation & environnement
# ============================================================

install:
    $(POETRY) install

update:
    $(POETRY) update

venv:
    $(POETRY) shell

# ============================================================
# Lancement de l'application
# ============================================================

run:
    $(RUN) desp-gui

# ============================================================
# Qualité du code
# ============================================================

lint:
    $(RUN) ruff check $(SRC)

format:
    $(RUN) black $(SRC)

typecheck:
    $(RUN) mypy $(SRC)

quality: lint format typecheck

# ============================================================
# Tests
# ============================================================

test:
    $(RUN) pytest -q

test-verbose:
    $(RUN) pytest -vv

# ============================================================
# Build & publication
# ============================================================

build:
    $(POETRY) build

publish:
    $(POETRY) publish --build

# ============================================================
# Nettoyage
# ============================================================

clean:
    find . -type d -name "__pycache__" -exec rm -rf {} +
    find . -type d -name "*.egg-info" -exec rm -rf {} +
    rm -rf dist/

# ============================================================
# Mode développement (watch)
# ============================================================

dev:
    $(RUN) desp-gui

# ============================================================
# Aide
# ============================================================

help:
    @echo "Commandes disponibles :"
    @echo "  make install      → installation du projet"
    @echo "  make run          → lancer l'application DESP"
    @echo "  make lint         → analyse statique (ruff)"
    @echo "  make format       → formatage (black)"
    @echo "  make typecheck    → typage (mypy)"
    @echo "  make quality      → lint + format + typecheck"
    @echo "  make test         → tests unitaires"
    @echo "  make build        → build du package"
    @echo "  make publish      → publication PyPI"
    @echo "  make clean        → nettoyage"
    @echo "  make dev          → mode développement"

