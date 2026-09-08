import sys
import os
import pandas as pd

from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QTabWidget, QMessageBox
)


import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)


# --- Modules métier ---
from desp.desp_excel import charger_donnees
from desp.desp_groups import determiner_fluide_groupe
from desp.desp_tableaux import determiner_tableau
from desp.desp_categories import determiner_categorie
from desp.desp_export import exporter_rapport
from desp.desp_rapport import resume_categorie
from desp.desp_validation import valider_parametres

# --- Onglets UI ---
from desp.ui.onglet_classification import OngletClassification
from desp.ui.onglet_graphique import OngletGraphique
from desp.ui.onglet_resultats import OngletResultats

# --- Win32 API pour maximisation native Windows ---
import ctypes
SW_MAXIMIZE = 3

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class FenetreDESP(QMainWindow):
    """
    Fenêtre principale DESP (MVC)
    """

    def __init__(self):
        super().__init__()

        self.setWindowTitle("DESP – Classification")

        # Taille minimale pour éviter les réductions Windows
        self.setMinimumSize(1200, 800)

        # Chargement Excel
        try:
            self.df_desp = charger_donnees()
            print("Colonnes chargées :", self.df_desp.columns) #┌ a supprimer

        except Exception as e:
            QMessageBox.critical(self, "Erreur Excel", str(e))
            self.df_desp = pd.DataFrame()

        self.resultats = {}

        # --- Layout principal ---
        central = QWidget()
        layout = QVBoxLayout()

        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)

        self.tabs = QTabWidget()

        # --- Style des onglets (taille police, gras, majuscules) ---
        self.tabs.setStyleSheet("""
            QTabBar::tab {
                font-weight: bold;
                text-transform: uppercase;
                padding: 8px 20px;
                font-size: 15px;   /* ← taille de police */
                }
            QTabBar::tab:selected {
                font-size: 17px;   /* ← onglet actif légèrement plus grand */
                color: #0055aa;
            }
        """)
        # --- Instanciation des onglets ---
        self.onglet_classif = OngletClassification(self.df_desp, self.on_valider)
        self.onglet_graph = OngletGraphique()
        self.onglet_res = OngletResultats(self.on_export)

        # --- Ajout des onglets ---
        self.tabs.addTab(self.onglet_classif, "Classification")
        self.tabs.addTab(self.onglet_graph, "Graphique DESP")
        self.tabs.addTab(self.onglet_res, "Résultats / Rapport")

        layout.addWidget(self.tabs)

        central.setLayout(layout)
        self.setCentralWidget(central)


    # ----------------------------------------------------------------------
    def on_valider(self, type_eq, fluide, etat, ps, v, dn):
        try:
            groupe = determiner_fluide_groupe(self.df_desp, fluide, etat)
            tableau = determiner_tableau(type_eq, groupe, etat)

            ok, err = valider_parametres(type_eq, fluide, etat, ps, v, dn)
            if not ok:
                QMessageBox.warning(self, "Erreur paramètres", err)
                return

            if type_eq in ["Récipients", "Générateurs"]:
                x = v
                label_x = "Volume (V)"
            else:
                x = dn
                label_x = "Diamètre nominal (DN)"

            categorie = determiner_categorie(tableau, ps, v, dn)

            self.resultats = {
                "type_eq": type_eq,
                "fluide": fluide,
                "etat": etat,
                "ps": ps,
                "v": v,
                "dn": dn,
                "tableau": tableau,
                "groupe": groupe,
                "categorie": categorie,
                "x": x,
                "label_x": label_x,
            }

            self.onglet_graph.afficher_graphique(tableau, x, ps, label_x)
            self.onglet_res.afficher_resultats(self.resultats)

            QMessageBox.information(self, "OK", "Paramètres validés avec succès.")

        except Exception as e:
            QMessageBox.critical(self, "Erreur interne", repr(e))




    # ----------------------------------------------------------------------
    def on_implications(self):
        if not self.resultats:
            QMessageBox.warning(self, "Erreur", "Aucun résultat disponible.")
            return

        cat = self.resultats["categorie"]
        data = resume_categorie(cat)
        self.onglet_res.afficher_implications(cat, data)

    # ----------------------------------------------------------------------
    def on_export(self, nom_fichier):
        if not self.resultats:
            QMessageBox.warning(self, "Erreur", "Aucun résultat à exporter.")
            return

        try:
            fichier_xlsx, fichier_pdf = exporter_rapport(self.resultats, BASE_DIR, nom_fichier)
        except Exception as e:
            QMessageBox.critical(self, "Erreur export", str(e))
            return

        QMessageBox.information(
            self,
            "OK",
            f"Sauvegarde effectuée :\n- {fichier_xlsx}\n- {fichier_pdf}"
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)

    fen = FenetreDESP()
    fen.show()

    # --- Maximisation native Windows (fiable à 100 %) ---
    hwnd = fen.winId().__int__()
    ctypes.windll.user32.ShowWindow(hwnd, SW_MAXIMIZE)

    sys.exit(app.exec())



