# onglet_classification.py
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit,
    QComboBox, QPushButton
)
from PyQt6.QtCore import Qt


class OngletClassification(QWidget):
    def __init__(self, df_desp, callback_valider):
        super().__init__()

        self.df_desp = df_desp
        self.callback_valider = callback_valider

        layout = QVBoxLayout()
        layout.setSpacing(10)

        # Type équipement
        self.combo_type = QComboBox()
        self.combo_type.addItems(["Sélectionnez...", "Récipients", "Tuyauteries", "Générateurs"])
        self.combo_type.currentIndexChanged.connect(self.mettre_a_jour_champs)
        layout.addWidget(self._ligne("Type d'équipement :", self.combo_type))

        # Fluide
        self.combo_fluides = QComboBox()
        fluides = df_desp["Fluides"].dropna().unique().tolist()
        self.combo_fluides.addItems(fluides)
        layout.addWidget(self._ligne("Fluide :", self.combo_fluides))

        # État
        self.combo_etat = QComboBox()
        self.combo_etat.addItems(["Sélectionnez...", "Gaz", "Liquide"])
        layout.addWidget(self._ligne("État du fluide :", self.combo_etat))

        # Paramètres
        self.widget_ps, self.edit_ps = self._champ("PS (bar) :")
        self.widget_v, self.edit_v = self._champ("V (litres) :")
        self.widget_dn, self.edit_dn = self._champ("DN :")

        layout.addWidget(self.widget_ps)
        layout.addWidget(self.widget_v)
        layout.addWidget(self.widget_dn)

        self.widget_ps.hide()
        self.widget_v.hide()
        self.widget_dn.hide()

        # Bouton valider centré en bas
        self.btn_valider = QPushButton("Valider les paramètres")
        self.btn_valider.clicked.connect(self._valider)
        self.btn_valider.setStyleSheet("""
            QPushButton {
                font-weight: bold;
                padding: 8px 22px;
                font-size: 14px;
            }
        """)

        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(self.btn_valider)
        button_layout.addStretch()

        # 🔑 Pousse tout vers le haut, bouton en bas
        layout.addStretch()
        layout.addLayout(button_layout)

        self.setLayout(layout)

    def _ligne(self, texte, widget):
        w = QWidget()
        h = QHBoxLayout()
        label = QLabel(texte)
        label.setStyleSheet("font-size: 16px; font-weight: bold;")
        label.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        label.setMinimumWidth(200)   # ← largeur fixe pour alignement parfait
        h.addWidget(label)
        h.addWidget(widget)
        h.addStretch()
        w.setLayout(h)
        return w

    def _champ(self, texte):
        w = QWidget()
        h = QHBoxLayout()
        label = QLabel(texte)
        label.setStyleSheet("font-size: 16px; font-weight: bold;")
        label.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        label.setMinimumWidth(200)   # ← même largeur pour alignement parfait
        edit = QLineEdit()
        edit.setFixedWidth(120)
        h.addWidget(label)
        h.addWidget(edit)
        h.addStretch()
        w.setLayout(h)
        return w, edit

    def mettre_a_jour_champs(self):
        choix = self.combo_type.currentText()
        self.widget_ps.hide()
        self.widget_v.hide()
        self.widget_dn.hide()

        if choix in ["Récipients", "Générateurs"]:
            self.widget_ps.show()
            self.widget_v.show()
        elif choix == "Tuyauteries":
            self.widget_ps.show()
            self.widget_dn.show()

    def _valider(self):
        type_eq = self.combo_type.currentText()
        fluide = self.combo_fluides.currentText()
        etat = self.combo_etat.currentText()

        def lire_float(widget):
            txt = widget.text().strip()
            if txt == "":
                return None
            try:
                return float(txt)
            except ValueError:
                return None

        ps = lire_float(self.edit_ps)
        v  = lire_float(self.edit_v)
        dn = lire_float(self.edit_dn)

        self.callback_valider(type_eq, fluide, etat, ps, v, dn)



