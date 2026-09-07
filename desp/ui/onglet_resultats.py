# onglet_resultats.py
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton, QInputDialog,
    QGridLayout, QHBoxLayout
)
from PyQt6.QtCore import Qt
from desp.desp_rapport import resume_categorie


class OngletResultats(QWidget):
    def __init__(self, callback_export):
        super().__init__()
        self.callback_export = callback_export

        # --- Layout principal vertical ---
        final = QVBoxLayout()
        final.setContentsMargins(20, 20, 20, 20)
        final.setSpacing(10)

        # --- Ligne des titres ---
        titre_layout = QHBoxLayout()

        titre_left = QLabel("Résumé DESP")
        titre_left.setStyleSheet("font-size: 20px; font-weight: bold;")
        titre_left.setAlignment(Qt.AlignmentFlag.AlignLeft)

        titre_right = QLabel("Implications réglementaires (DESP)")
        titre_right.setStyleSheet("font-size: 20px; font-weight: bold;")
        titre_right.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        titre_layout.addWidget(titre_left)
        titre_layout.addStretch(1)
        titre_layout.addWidget(titre_right)
        titre_layout.addStretch(1)

        final.addLayout(titre_layout)

        # --- Layout horizontal des deux colonnes ---
        layout = QHBoxLayout()
        layout.setSpacing(40)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        # ------------------------------------------------------------------
        # COLONNE GAUCHE (centrée dans sa demi-fenêtre)
        # ------------------------------------------------------------------
        col_left = QVBoxLayout()
        col_left.setSpacing(4)

        self.grid_left = QGridLayout()
        self.grid_left.setSpacing(2)
        col_left.addLayout(self.grid_left)

        left_wrapper = QHBoxLayout()
        left_wrapper.addStretch(1)
        left_wrapper.addLayout(col_left)
        left_wrapper.addStretch(1)

        layout.addLayout(left_wrapper)

        # ------------------------------------------------------------------
        # COLONNE DROITE (centrée dans sa demi-fenêtre)
        # ------------------------------------------------------------------
        col_right = QVBoxLayout()
        col_right.setSpacing(4)

        self.grid_right = QGridLayout()
        self.grid_right.setSpacing(2)
        col_right.addLayout(self.grid_right)

        right_wrapper = QHBoxLayout()
        right_wrapper.addStretch(1)
        right_wrapper.addLayout(col_right)
        right_wrapper.addStretch(1)

        layout.addLayout(right_wrapper)

        final.addLayout(layout)

        # ------------------------------------------------------------------
        # Bouton Sauvegarder — même style que premier onglet
        # ------------------------------------------------------------------
        btn_save = QPushButton("Sauvegarder (Excel + PDF)")
        btn_save.clicked.connect(self._exporter)

        btn_save.setStyleSheet("""
            QPushButton {
                font-weight: bold;
                padding: 8px 22px;
                font-size: 14px;
            }
        """)

        btn_layout = QHBoxLayout()
        btn_layout.addStretch()
        btn_layout.addWidget(btn_save)
        btn_layout.addStretch()

        # 🔥 Correction : bouton collé en bas comme onglet 1
        final.addStretch()
        final.addLayout(btn_layout)

        self.setLayout(final)

    # ----------------------------------------------------------------------
    def afficher_resultats(self, r):
        # Nettoyage gauche
        while self.grid_left.count():
            item = self.grid_left.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        lignes = [
            ("Type d’équipement :", r["type_eq"]),
            ("Fluide :", f"{r['fluide']} ({r['etat']})"),
            ("Groupe fluide :", str(r["groupe"])),
            ("Catégorie DESP :", r["categorie"]),
            ("PS :", f"{r['ps']} bar"),
        ]

        if r["type_eq"] in ["Récipients", "Générateurs"]:
            lignes.append(("V :", f"{r['v']} L"))
        else:
            lignes.append(("DN :", f"{r['dn']} mm"))

        for i, (label_txt, valeur_txt) in enumerate(lignes):
            lbl = QLabel(label_txt)
            lbl.setAlignment(Qt.AlignmentFlag.AlignRight)
            lbl.setStyleSheet("font-weight: bold; font-size: 14px;")

            val = QLabel(str(valeur_txt))
            val.setAlignment(Qt.AlignmentFlag.AlignLeft)
            val.setStyleSheet("font-size: 14px;")

            self.grid_left.addWidget(lbl, i, 0)
            self.grid_left.addWidget(val, i, 1)

        # ------------------------------------------------------------------
        # Implications réglementaires
        # ------------------------------------------------------------------
        data = resume_categorie(r["categorie"])

        while self.grid_right.count():
            item = self.grid_right.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        lignes_imp = [
            ("Niveau de risque :", data["risque"]),
            ("Organisme notifié :", data["organisme_notifie"]),
            ("Modules :", ", ".join(data["modules"])),
            ("Implications :", "<br>".join(f"- {i}" for i in data["implications"])),
            ("Exemples :", "<br>".join(f"- {e}" for e in data["exemples"])),
        ]

        for i, (label_txt, valeur_txt) in enumerate(lignes_imp):
            lbl = QLabel(label_txt)
            lbl.setAlignment(Qt.AlignmentFlag.AlignRight)
            lbl.setStyleSheet("font-weight: bold; font-size: 14px;")

            val = QLabel(valeur_txt)
            val.setAlignment(Qt.AlignmentFlag.AlignLeft)
            val.setWordWrap(True)
            val.setStyleSheet("font-size: 14px;")

            self.grid_right.addWidget(lbl, i, 0)
            self.grid_right.addWidget(val, i, 1)

    # ----------------------------------------------------------------------
    def _exporter(self):
        nom, ok = QInputDialog.getText(self, "Nom du fichier", "Nom (sans extension) :")
        if ok and nom.strip():
            self.callback_export(nom.strip())

