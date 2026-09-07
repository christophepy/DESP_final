from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QFrame
from PyQt6.QtCore import Qt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT

from desp.desp_graphique import afficher_point_de_fonctionnement


class OngletGraphique(QWidget):
    """
    Onglet 2 : Graphique DESP
    """

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)   # ← IMPORTANT : plus AlignCenter

        self.frame_graph = QFrame()
        self.frame_graph.setLayout(QVBoxLayout())

        self.placeholder = QLabel("Graphique non généré.")
        self.placeholder.setStyleSheet("font-style: italic; color: gray;")
        self.frame_graph.layout().addWidget(self.placeholder)

        layout.addWidget(self.frame_graph)
        self.setLayout(layout)

    # ----------------------------------------------------------------------
    def afficher_graphique(self, tableau, x, ps, label_x):
        layout = self.frame_graph.layout()

        # Clear
        while layout.count():
            item = layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        # Génération du graphique
        fig, ax = afficher_point_de_fonctionnement(tableau, x, ps, label_x)
        canvas = FigureCanvasQTAgg(fig)

        # Toolbar Matplotlib : zoom, pan, reset, save
        toolbar = NavigationToolbar2QT(canvas, self)
        layout.addWidget(toolbar)      # ← La toolbar apparaît maintenant correctement

        # Ajout du canvas
        layout.addWidget(canvas)

        # Alignement propre
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
