# desp_graphique.py
# ---------------------------------------------------------
# Graphique DESP : point de fonctionnement + annotation
# ---------------------------------------------------------

import matplotlib.pyplot as plt
from desp.desp_graphs import tracer_tableau


def position_annotation(ax, x, ps):
    """
    Position fixe hors du graphique, en haut à droite.
    Coordonnées Axes (0–1).
    """
    return 1.05, 0.95


def afficher_point_de_fonctionnement(tableau: int, x: float, ps: float,
                                     label_x: str, figsize=(12, 9)):
    """
    Affiche le point de fonctionnement sur le tableau DESP :
    - point rouge
    - annotation hors graphique
    - lignes PS et X
    """

    fig, ax = tracer_tableau(tableau, figsize=figsize)

    # Point rouge
    ax.plot(x, ps, marker="+", markersize=18, markeredgewidth=3,
            color="red", zorder=30)

    # Position hors du graphique (fixe)
    xt, yt = position_annotation(ax, x, ps)

    # Choix de l’affichage de x + unité
    if label_x.lower().startswith("diam"):
        short_label = "DN"
        x_display = f"{int(x)}"          # DN sans unité
    else:
        short_label = "V"
        x_display = f"{x:.2f} L"         # V avec unité L

    # Annotation hors du graphique + encadré léger
    ax.annotate(
        f"Point de fonctionnement\n{short_label} = {x_display}\nPS = {ps:.2f} bar",
        xy=(x, ps),
        xytext=(xt, yt),
        textcoords=ax.transAxes,     # repère Axes (0–1)
        arrowprops=dict(arrowstyle="->", color="red", lw=2),
        color="red",
        fontsize=10,
        fontweight="bold",
        bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="red", alpha=0.6)
    )

    # Lignes rouges
    xmin, xmax = ax.get_xlim()
    ymin, ymax = ax.get_ylim()

    ax.plot([x, x], [ymin, ymax], "--", color="red", lw=1.5, zorder=15)
    ax.plot([xmin, xmax], [ps, ps], "--", color="red", lw=1.5, zorder=15)

    plt.grid(True, linestyle="--", alpha=0.5)

    return fig, ax








