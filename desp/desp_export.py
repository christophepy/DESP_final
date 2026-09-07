# desp_export.py
# ---------------------------------------------------------
# Export du rapport DESP : Excel + PDF
# ---------------------------------------------------------

import os
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from xlsxwriter import Workbook

from desp.desp_graphs import tracer_tableau
from desp.desp_graphique import position_annotation


def exporter_rapport(resultats: dict, base_dir: str, nom_fichier: str) -> tuple[str, str]:
    """
    Exporte le rapport DESP en Excel + PDF.
    Retourne (chemin_excel, chemin_pdf).
    """

    # -----------------------------
    # Extraction des données
    # -----------------------------
    type_eq = resultats["type_eq"]
    ps = resultats["ps"]
    v = resultats["v"]
    dn = resultats["dn"]
    tableau = resultats["tableau"]
    categorie = resultats["categorie"]
    fluide = resultats["fluide"]
    etat = resultats["etat"]
    groupe = resultats["groupe"]

    # Détermination de x (V ou DN)
    x = v if type_eq in ["Récipients", "Générateurs"] else dn
    label_x = "V" if type_eq in ["Récipients", "Générateurs"] else "DN"

    # -----------------------------
    # Chemins des fichiers
    # -----------------------------
    fichier_xlsx = os.path.join(base_dir, f"{nom_fichier}.xlsx")
    fichier_pdf = os.path.join(base_dir, f"{nom_fichier}.pdf")
    fichier_png = os.path.join(base_dir, f"{nom_fichier}_graphique.png")

    # -----------------------------
    # 1) EXPORT EXCEL
    # -----------------------------
    wb = Workbook(fichier_xlsx)
    ws = wb.add_worksheet("Résultats")

    ws.set_paper(9)
    ws.set_landscape()
    ws.center_horizontally()
    ws.center_vertically()
    ws.set_margins(left=0.5, right=0.5, top=0.5, bottom=0.5)
    ws.fit_to_pages(1, 1)

    lignes = [
        ("Type", type_eq),
        ("Fluide", fluide),
        ("État", etat),
        ("Groupe fluide", groupe),
        ("Tableau DESP", tableau),
        ("Catégorie DESP", categorie),
        ("PS (bar)", ps),
        ("V (L)", v),
        ("DN (mm)", dn),
    ]

    for i, (k, v) in enumerate(lignes):
        ws.write(i, 0, k)
        ws.write(i, 1, "" if v is None else v)

    # -----------------------------
    # Graphique PNG
    # -----------------------------
    fig, ax = tracer_tableau(tableau, figsize=(10, 8))

    ax.plot(x, ps, marker="+", markersize=18, markeredgewidth=3,
            color="red", zorder=30)

    xmin, xmax = ax.get_xlim()
    ymin, ymax = ax.get_ylim()

    xt, yt = position_annotation(ax, x, ps)

    ax.annotate(
        f"Point de fonctionnement\n{label_x} = {x:.2f}\nPS = {ps:.2f}",
        xy=(x, ps),
        xytext=(xt, yt),
        arrowprops=dict(arrowstyle="->", color="red", lw=2),
        color="red", fontsize=10, fontweight="bold"
    )

    ax.plot([x, x], [ymin, ymax], "--", color="red", lw=1.5, zorder=15)
    ax.plot([xmin, xmax], [ps, ps], "--", color="red", lw=1.5, zorder=15)

    fig.savefig(fichier_png, dpi=120)
    plt.close(fig)

    ws.insert_image(0, 3, fichier_png)
    wb.close()

    # -----------------------------
    # 2) EXPORT PDF
    # -----------------------------
    with PdfPages(fichier_pdf) as pdf:
        fig, ax = tracer_tableau(tableau, figsize=(10, 8))

        ax.plot(x, ps, marker="+", markersize=18, markeredgewidth=3,
                color="red", zorder=30)

        xmin, xmax = ax.get_xlim()
        ymin, ymax = ax.get_ylim()

        xt, yt = position_annotation(ax, x, ps)

        ax.annotate(
            f"Point de fonctionnement\n{label_x} = {x:.2f}\nPS = {ps:.2f}",
            xy=(x, ps),
            xytext=(xt, yt),
            arrowprops=dict(arrowstyle="->", color="red", lw=2),
            color="red", fontsize=10, fontweight="bold"
        )

        ax.plot([x, x], [ymin, ymax], "--", color="red", lw=1.5, zorder=15)
        ax.plot([xmin, xmax], [ps, ps], "--", color="red", lw=1.5, zorder=15)

        txt = (
            f"Type : {type_eq}\n"
            f"Fluide : {fluide} ({etat})\n"
            f"Groupe fluide : {groupe}\n"
            f"Tableau DESP : {tableau}\n"
            f"Catégorie DESP : {categorie}\n"
            f"PS : {ps} bar\n"
            f"{label_x} : {x}\n"
        )
        fig.text(0.02, 0.02, txt, fontsize=9, va="bottom", ha="left")

        pdf.savefig(fig)
        plt.close(fig)

    # -----------------------------
    # Nettoyage PNG temporaire
    # -----------------------------
    try:
        os.remove(fichier_png)
    except Exception:
        pass

    return fichier_xlsx, fichier_pdf




