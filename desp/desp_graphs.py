# desp_graphs.py
# ---------------------------------------------------------
# Module de tracé des 9 graphes DESP (Annexe II 2014/68/UE)
# ---------------------------------------------------------
import matplotlib
matplotlib.use("QtAgg")
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter


# ---------------------------------------------------------
# Formatage des axes log
# ---------------------------------------------------------
def custom_format(xv, _):
    if abs(xv - round(xv)) < 1e-9:
        return f"{int(round(xv))}"
    return f"{xv:.2f}"


# ------------------------------------------------------------
# TABLEAU 1 – Récipients, gaz, groupe 1 – PS/V
# ------------------------------------------------------------
def trace_tableau_1(ax):
    segments = [
        ([0.1, 1, 2000], [1000, 1000, 0.5]),
        ([0.1, 1, 400],  [200, 200, 0.5]),
        ([1, 1, 100],    [200, 50, 0.5]),
        ([1, 1, 50],     [50, 25, 0.5]),
        ([0.1, 10000],   [0.5, 0.5]),
    ]
    for x, y in segments:
        ax.plot(x, y, color="black")

    # --- Axes log + limites ---
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlim(0.1, 10000)
    ax.set_ylim(0.1, 100000)

    ax.set_xticks([0.1, 1, 10, 50, 100, 400, 1000, 2000, 10000])
    ax.set_yticks([0.5, 1, 4, 25, 50, 100, 200, 1000, 10000])

    ax.xaxis.set_major_formatter(FuncFormatter(custom_format))
    ax.yaxis.set_major_formatter(FuncFormatter(custom_format))

    # Liste des valeurs à colorer X
    special_values = {1, 50, 100, 400, 2000}

    # Coloration des labels X
    for tick in ax.get_xticklabels():
        val = float(tick.get_text())
        if val in special_values:
            tick.set_color("red")
            tick.set_fontweight("bold")
        else:
            tick.set_color("black")

    # Liste des valeurs à colorer Y
    special_values = {25, 50, 200, 1000}

    # Coloration des labels Y
    for tick in ax.get_yticklabels():
        val = float(tick.get_text())
        if val in special_values:
            tick.set_color("red")
            tick.set_fontweight("bold")
        else:
            tick.set_color("black")

    ax.tick_params(axis="both", labelsize=8)

    ax.set_aspect("equal")

    # --- Titres ---
    ax.set_title("DESP Tableau 1", fontsize=16, pad=15, fontweight="bold", color="blue")
    ax.set_xlabel("V (L)", loc="right", fontweight="bold")
    ax.set_ylabel("PS (bar)", loc="top", fontweight="bold", rotation=0)

    # --- Zones ---
    ax.fill_between((0.1, 10000), (0.5), hatch="///", facecolor="None", edgecolor="black", linewidth=0.0)
    ax.fill_between([0.1, 1], [0.5, 0.5], [200, 200], color="yellow", alpha=0.5)
    ax.fill_between([1, 50], [0.5, 0.5], [25, 0.5], color="yellow", alpha=0.5)

    # --- Textes zones ---
    labels = [
        (25, 500, "IV"),
        (0.3, 500, "III"),
        (25, 3, "II"),
        (25, 1.1, "I"),
        (0.15, 1.5, "Règles de l'Art"),
    ]
    for x, y, txt in labels:
        ax.text(x, y, txt, fontsize=10, color="black", fontweight="bold")

    # --- Style ---
    ax.grid(True, linestyle="--", alpha=0.5)
    ax.tick_params(axis="x", length=5)
    ax.tick_params(axis="y", length=5)
    ax.tick_params(axis="both", which="minor", length=0)


# ------------------------------------------------------------
# TABLEAU 2 – Récipients, gaz, groupe 2 – PS/V
# ------------------------------------------------------------
def trace_tableau_2(ax):
    # --- Segments du tableau 1 (PS/V – gaz groupe 1) ---
    segments = [
        ([0.1, 1, 750, 10000], [3000, 3000, 4, 4]),
        ([0.1, 1, 2000], [1000, 1000, 0.5]),
        ([0.1, 1, 1], [1000, 1000, 50]),
        ([1, 400], [200, 0.5]),
        ([1, 100], [50, 0.5]),
        ([0.1, 10000], [0.5, 0.5]),
    ]
    for x, y in segments:
        ax.plot(x, y, color="black")

    # --- Axes log + limites ---
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlim(0.1, 10000)
    ax.set_ylim(0.1, 100000)

    ax.set_xticks([0.1, 1, 10, 100, 400, 750, 1000, 2000, 10000])
    ax.set_yticks([0.5, 1, 4, 50, 100, 200, 1000, 3000, 10000])

    ax.xaxis.set_major_formatter(FuncFormatter(custom_format))
    ax.yaxis.set_major_formatter(FuncFormatter(custom_format))

    # --- Rotation des ticks pour éviter chevauchement ---
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right")

    # Liste des valeurs à colorer X
    special_values = {1, 100, 400, 750, 2000}

    # Coloration des labels X
    for tick in ax.get_xticklabels():
        val = float(tick.get_text())
        if val in special_values:
            tick.set_color("red")
            tick.set_fontweight("bold")
        else:
            tick.set_color("black")

    # Liste des valeurs à colorer Y
    special_values = {4, 50, 200, 1000, 3000}

    # Coloration des labels Y
    for tick in ax.get_yticklabels():
        val = float(tick.get_text())
        if val in special_values:
            tick.set_color("red")
            tick.set_fontweight("bold")
        else:
            tick.set_color("black")

    ax.tick_params(axis="both", labelsize=8)

    ax.set_aspect("equal")

    # --- Titres ---
    ax.set_title("DESP Tableau 2", fontsize=16, pad=15, fontweight="bold", color="blue")
    ax.set_xlabel("V (L)", loc="right", fontweight="bold")
    ax.set_ylabel("PS (bar)", loc="top", fontweight="bold", rotation=0)

    # --- Zones ---
    ax.fill_between((0.1, 10000), (0.5), hatch="///", facecolor="None", edgecolor="black", linewidth=0.0)
    ax.fill_between([0.1, 1], [0.5, 0.5], [1000, 1000], color="yellow", alpha=0.5)
    ax.fill_between([1, 100], [0.5, 0.5], [50, 0.5], color="yellow", alpha=0.5)

    # --- Textes zones ---
    labels = [
        (25, 500, "IV"),
        (0.3, 1500, "III"),
        (25, 15, "II"),
        (25, 3.5, "I"),
        (0.15, 3, "Règles de l'Art"),
    ]
    for x, y, txt in labels:
        ax.text(x, y, txt, fontsize=10, color="black", fontweight="bold")

    # --- Style ---
    ax.grid(True, linestyle="--", alpha=0.5)
    ax.tick_params(axis="x", length=5)
    ax.tick_params(axis="y", length=5)
    ax.tick_params(axis="both", which="minor", length=0)


# ------------------------------------------------------------
# TABLEAU 3 – Récipients, liquides, groupe 1 – PS/V
# ------------------------------------------------------------
def trace_tableau_3(ax):
    segments = [
        ([0.1, 10000], [500, 500]),
        ([1, 1, 400], [10000, 200, 0.5]),
        ([20, 10000], [10, 10]),
        ([0.1, 10000], [0.5, 0.5]),
    ]
    for x, y in segments:
        ax.plot(x, y, color="black")

    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlim(0.1, 10000)
    ax.set_ylim(0.1, 100000)

    ax.set_xticks([0.1, 1, 10, 100, 400, 1000, 10000])
    ax.set_yticks([0.5, 1, 4, 10, 100, 200, 500, 1000, 10000])

    ax.xaxis.set_major_formatter(FuncFormatter(custom_format))
    ax.yaxis.set_major_formatter(FuncFormatter(custom_format))

    plt.setp(ax.get_xticklabels(), rotation=45, ha="right")

    special_values = {1, 400}
    for tick in ax.get_xticklabels():
        val = float(tick.get_text())
        if val in special_values:
            tick.set_color("red")
            tick.set_fontweight("bold")
        else:
            tick.set_color("black")

    special_values = {10, 200, 500}
    for tick in ax.get_yticklabels():
        val = float(tick.get_text())
        if val in special_values:
            tick.set_color("red")
            tick.set_fontweight("bold")
        else:
            tick.set_color("black")

    ax.tick_params(axis="both", labelsize=8)
    ax.set_aspect("equal")

    ax.set_title("DESP Tableau 3", fontsize=16, pad=15, fontweight="bold", color="blue")
    ax.set_xlabel("V (L)", loc="right", fontweight="bold")
    ax.set_ylabel("PS (bar)", loc="top", fontweight="bold", rotation=0)

    ax.fill_between((0.1, 10000), (0.5), hatch="///", facecolor="None", edgecolor="black", linewidth=0.0)
    ax.fill_between([0.1, 1], [0.5, 0.5], [500, 500], color="yellow", alpha=0.5)
    ax.fill_between([1, 400], [0.5, 0.5], [200, 0.5], color="yellow", alpha=0.5)

    labels = [
        (0.3, 2000, "II"),
        (300, 2000, "III"),
        (300, 100, "II"),
        (300, 3.5, "I"),
        (0.15, 3, "Règles de l'Art"),
    ]
    for x, y, txt in labels:
        ax.text(x, y, txt, fontsize=10, color="black", fontweight="bold")

    ax.grid(True, linestyle="--", alpha=0.5)
    ax.tick_params(axis="x", length=5)
    ax.tick_params(axis="y", length=5)
    ax.tick_params(axis="both", which="minor", length=0)


# ------------------------------------------------------------
# TABLEAU 4 – Récipients, liquides, groupe 2 – PS/V
# ------------------------------------------------------------
def trace_tableau_4(ax):
    segments = [
        ([0.1, 10, 1000, 10000], [1000, 1000, 10, 10]),
        ([10, 10], [1000, 10000]),
        ([20, 10000], [500, 500]),
        ([0.1, 10000], [0.5, 0.5]),
    ]
    for x, y in segments:
        ax.plot(x, y, color="black")

    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlim(0.1, 10000)
    ax.set_ylim(0.1, 100000)

    ax.set_xticks([0.1, 1, 10, 20, 100, 1000, 10000])
    ax.set_yticks([0.5, 1, 4, 10, 100, 500, 1000, 10000])

    ax.xaxis.set_major_formatter(FuncFormatter(custom_format))
    ax.yaxis.set_major_formatter(FuncFormatter(custom_format))

    plt.setp(ax.get_xticklabels(), rotation=45, ha="right")

    special_values = {10, 20, 1000}
    for tick in ax.get_xticklabels():
        val = float(tick.get_text())
        if val in special_values:
            tick.set_color("red")
            tick.set_fontweight("bold")
        else:
            tick.set_color("black")

    special_values = {10, 500, 1000}
    for tick in ax.get_yticklabels():
        val = float(tick.get_text())
        if val in special_values:
            tick.set_color("red")
            tick.set_fontweight("bold")
        else:
            tick.set_color("black")

    ax.tick_params(axis="both", labelsize=8)
    ax.set_aspect("equal")

    ax.set_title("DESP Tableau 4", fontsize=16, pad=15, fontweight="bold", color="blue")
    ax.set_xlabel("V (L)", loc="right", fontweight="bold")
    ax.set_ylabel("PS (bar)", loc="top", fontweight="bold", rotation=0)

    ax.fill_between((0.1, 10000), (0.5), hatch="///", facecolor="None", edgecolor="black", linewidth=0.0)
    ax.fill_between([0.1, 10], [0.5, 0.5], [1000, 1000], color="yellow", alpha=0.5)
    ax.fill_between([10, 1000], [0.5, 0.5], [1000, 10], color="yellow", alpha=0.5)
    ax.fill_between([1000, 10000], [0.5, 0.5], [10, 10], color="yellow", alpha=0.5)

    labels = [
        (0.3, 2000, "I"),
        (300, 2000, "II"),
        (300, 100, "I"),
        (0.15, 3, "Règles de l'Art"),
    ]
    for x, y, txt in labels:
        ax.text(x, y, txt, fontsize=10, color="black", fontweight="bold")

    ax.grid(True, linestyle="--", alpha=0.5)
    ax.tick_params(axis="x", length=5)
    ax.tick_params(axis="y", length=5)
    ax.tick_params(axis="both", which="minor", length=0)


# ------------------------------------------------------------
# TABLEAU 5 – Générateurs de vapeur ou d'eau surchauffée – PS/V
# ------------------------------------------------------------
def trace_tableau_5(ax):
    segments = [
        ([2, 2], [0.5, 10000]),
        ([2, 100, 1000, 1000], [32, 32, 3, 0.5]),
        ([2, 100], [25, 0.5]),
        ([6.25, 400], [32, 0.5]),
        ([0.1, 10000], [0.5, 0.5]),
    ]
    for x, y in segments:
        ax.plot(x, y, color="black")

    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlim(0.1, 10000)
    ax.set_ylim(0.1, 100000)

    ax.set_xticks([0.1, 1, 2, 6.25, 10, 94, 100, 400, 1000, 10000])
    ax.set_yticks([0.5, 1, 3, 25, 32, 100, 1000, 10000])

    ax.xaxis.set_major_formatter(FuncFormatter(custom_format))
    ax.yaxis.set_major_formatter(FuncFormatter(custom_format))

    plt.setp(ax.get_xticklabels(), rotation=45, ha="right")

    special_values = {2, 6.25, 94, 100, 400, 1000}
    for tick in ax.get_xticklabels():
        val = float(tick.get_text())
        if val in special_values:
            tick.set_color("red")
            tick.set_fontweight("bold")
        else:
            tick.set_color("black")

    special_values = {3, 25, 32}
    for tick in ax.get_yticklabels():
        val = float(tick.get_text())
        if val in special_values:
            tick.set_color("red")
            tick.set_fontweight("bold")
        else:
            tick.set_color("black")

    ax.tick_params(axis="both", labelsize=8)

    for tick in ax.get_xticklabels():
        if tick.get_text() == "100":
            tick.set_y(-0.03)

    ax.set_aspect("equal")

    ax.set_title("DESP Tableau 5", fontsize=16, pad=15, fontweight="bold", color="blue")
    ax.set_xlabel("V (L)", loc="right", fontweight="bold")
    ax.set_ylabel("PS (bar)", loc="top", fontweight="bold", rotation=0)

    ax.fill_between((0.1, 10000), (0.5), hatch="///", facecolor="None", edgecolor="black", linewidth=0.0)
    ax.fill_between([0.1, 2], [0.5, 0.5], [10000, 10000], color="yellow", alpha=0.5)

    labels = [
        (400, 200, "IV"),
        (400, 1.5, "III"),
        (50, 1.5, "II"),
        (10, 1.5, "I"),
        (0.15, 3, "Règles de l'Art"),
    ]
    for x, y, txt in labels:
        ax.text(x, y, txt, fontsize=10, color="black", fontweight="bold")

    ax.grid(True, linestyle="--", alpha=0.5)
    ax.tick_params(axis="x", length=5)
    ax.tick_params(axis="y", length=5)
    ax.tick_params(axis="both", which="minor", length=0)


# ------------------------------------------------------------
# TABLEAU 6 – Tuyauteries, gaz, groupe 1 – PS/DN
# ------------------------------------------------------------
def trace_tableau_6(ax):
    segments = [
        ([25, 25], [0.5, 10000]),
        ([25, 100, 100], [40, 10, 0.5]),
        ([100, 100, 350, 350], [10000, 35, 10, 0.5]),
        ([0.1, 10000], [0.5, 0.5]),
    ]
    for x, y in segments:
        ax.plot(x, y, color="black")

    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlim(0.1, 10000)
    ax.set_ylim(0.1, 100000)

    ax.set_xticks([0.1, 1, 10, 25, 100, 350, 1000, 10000])
    ax.set_yticks([0.5, 1, 4, 10, 35, 40, 100, 1000, 10000])

    ax.xaxis.set_major_formatter(FuncFormatter(custom_format))
    ax.yaxis.set_major_formatter(FuncFormatter(custom_format))

    plt.setp(ax.get_xticklabels(), rotation=45, ha="right")

    special_values = {25, 100, 350}
    for tick in ax.get_xticklabels():
        val = float(tick.get_text())
        if val in special_values:
            tick.set_color("red")
            tick.set_fontweight("bold")
        else:
            tick.set_color("black")

    special_values = {10, 35, 40}
    for tick in ax.get_yticklabels():
        val = float(tick.get_text())
        if val in special_values:
            tick.set_color("red")
            tick.set_fontweight("bold")
        else:
            tick.set_color("black")

    ax.tick_params(axis="both", labelsize=8)
    ax.set_aspect("equal")

    ax.set_title("DESP Tableau 6", fontsize=16, pad=15, fontweight="bold", color="blue")
    ax.set_xlabel("DN", loc="right", fontweight="bold")
    ax.set_ylabel("PS (bar)", loc="top", fontweight="bold", rotation=0)

    ax.fill_between((0.1, 10000), (0.5), hatch="///", facecolor="None", edgecolor="black", linewidth=0.0)
    ax.fill_between([0.1, 25], [0.5, 0.5], [10000, 10000], color="yellow", alpha=0.5)

    labels = [
        (400, 200, "III"),
        (50, 200, "II"),
        (50, 1.5, "I"),
        (0.15, 50, "Règles de l'Art"),
    ]
    for x, y, txt in labels:
        ax.text(x, y, txt, fontsize=10, color="black", fontweight="bold")

    ax.grid(True, linestyle="--", alpha=0.5)
    ax.tick_params(axis="x", length=5)
    ax.tick_params(axis="y", length=5)
    ax.tick_params(axis="both", which="minor", length=0)


# ------------------------------------------------------------
# TABLEAU 7 – Tuyauteries, gaz, groupe 2 – PS·DN
# ------------------------------------------------------------
def trace_tableau_7(ax):
    segments = [
        ([32, 32, 2000], [10000, 31.25, 0.5]),
        ([100, 100, 7000], [10000, 35, 0.5]),
        ([250, 250, 10000], [10000, 20, 0.5]),
        ([0.1, 10000], [0.5, 0.5]),
    ]
    for x, y in segments:
        ax.plot(x, y, color="black")

    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlim(0.1, 10000)
    ax.set_ylim(0.1, 100000)

    ax.set_xticks([0.1, 1, 10, 32, 100, 250, 1000, 2000, 7000, 10000])
    ax.set_yticks([0.5, 1, 4, 10, 20, 31.25, 35, 100, 1000, 10000])

    ax.xaxis.set_major_formatter(FuncFormatter(custom_format))
    ax.yaxis.set_major_formatter(FuncFormatter(custom_format))

    plt.setp(ax.get_xticklabels(), rotation=45, ha="right")

    special_values = {32, 100, 250, 2000, 7000, 10000}
    for tick in ax.get_xticklabels():
        val = float(tick.get_text())
        if val in special_values:
            tick.set_color("red")
            tick.set_fontweight("bold")
        else:
            tick.set_color("black")

    special_values = {10, 20, 31.25, 35}
    for tick in ax.get_yticklabels():
        val = float(tick.get_text())
        if val in special_values:
            tick.set_color("red")
            tick.set_fontweight("bold")
        else:
            tick.set_color("black")

    ax.tick_params(axis="both", labelsize=8)
    ax.set_aspect("equal")

    ax.set_title("DESP Tableau 7", fontsize=16, pad=15, fontweight="bold", color="blue")
    ax.set_xlabel("DN", loc="right", fontweight="bold")
    ax.set_ylabel("PS (bar)", loc="top", fontweight="bold", rotation=0)

    ax.fill_between((0.1, 10000), (0.5), hatch="///", facecolor="None", edgecolor="black", linewidth=0.0)
    ax.fill_between([0.1, 32], [0.5, 0.5], [10000, 10000], color="yellow", alpha=0.5)
    ax.fill_between([32, 2000], [0.5, 0.5], [31.25, 0.5], color="yellow", alpha=0.5)

    labels = [
        (400, 200, "III"),
        (150, 200, "II"),
        (50, 200, "I"),
        (0.15, 50, "Règles de l'Art"),
    ]
    for x, y, txt in labels:
        ax.text(x, y, txt, fontsize=10, color="black", fontweight="bold")

    ax.grid(True, linestyle="--", alpha=0.5)
    ax.tick_params(axis="x", length=5)
    ax.tick_params(axis="y", length=5)
    ax.tick_params(axis="both", which="minor", length=0)


# ------------------------------------------------------------
# TABLEAU 8 – Tuyauteries, liquides, groupe 1 – PS·DN
# ------------------------------------------------------------
def trace_tableau_8(ax):
    segments = [
        ([25, 25, 4000], [10000, 80, 0.5]),
        ([25, 10000], [500, 500]),
        ([200, 10000], [10, 10]),
        ([0.1, 10000], [0.5, 0.5]),
    ]
    for x, y in segments:
        ax.plot(x, y, color="black")

    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlim(0.1, 10000)
    ax.set_ylim(0.1, 100000)

    ax.set_xticks([0.1, 1, 10, 25, 100, 200, 350, 1000, 4000, 10000])
    ax.set_yticks([0.5, 1, 4, 10, 80, 100, 500, 1000, 10000])

    ax.xaxis.set_major_formatter(FuncFormatter(custom_format))
    ax.yaxis.set_major_formatter(FuncFormatter(custom_format))

    plt.setp(ax.get_xticklabels(), rotation=45, ha="right")

    special_values = {25, 200, 4000}
    for tick in ax.get_xticklabels():
        val = float(tick.get_text())
        if val in special_values:
            tick.set_color("red")
            tick.set_fontweight("bold")
        else:
            tick.set_color("black")

    special_values = {10, 80, 500}
    for tick in ax.get_yticklabels():
        val = float(tick.get_text())
        if val in special_values:
            tick.set_color("red")
            tick.set_fontweight("bold")
        else:
            tick.set_color("black")

    ax.tick_params(axis="both", labelsize=8)
    ax.set_aspect("equal")

    ax.set_title("DESP Tableau 8", fontsize=16, pad=15, fontweight="bold", color="blue")
    ax.set_xlabel("DN", loc="right", fontweight="bold")
    ax.set_ylabel("PS (bar)", loc="top", fontweight="bold", rotation=0)

    ax.fill_between((0.1, 10000), (0.5), hatch="///", facecolor="None", edgecolor="black", linewidth=0.0)
    ax.fill_between([0.1, 25], [0.5, 0.5], [10000, 10000], color="yellow", alpha=0.5)
    ax.fill_between([25, 4000], [0.5, 0.5], [80, 0.5], color="yellow", alpha=0.5)

    labels = [
        (1000, 2000, "III"),
        (1000, 80, "II"),
        (1000, 5, "I"),
        (0.15, 50, "Règles de l'Art"),
    ]
    for x, y, txt in labels:
        ax.text(x, y, txt, fontsize=10, color="black", fontweight="bold")

    ax.grid(True, linestyle="--", alpha=0.5)
    ax.tick_params(axis="x", length=5)
    ax.tick_params(axis="y", length=5)
    ax.tick_params(axis="both", which="minor", length=0)


# ------------------------------------------------------------
# TABLEAU 9 – Tuyauteries, liquides, groupe 2 – PS·DN
# ------------------------------------------------------------
def trace_tableau_9(ax):
    segments = [
        ([200, 200, 500, 10000], [10000, 25, 10, 10]),
        ([200, 10000], [500, 500]),
        ([0.1, 10000], [0.5, 0.5]),
    ]
    for x, y in segments:
        ax.plot(x, y, color="black")

    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlim(0.1, 10000)
    ax.set_ylim(0.1, 100000)

    ax.set_xticks([0.1, 1, 10, 100, 200, 500, 1000, 10000])
    ax.set_yticks([0.5, 1, 10, 25, 100, 500, 1000, 10000])

    ax.xaxis.set_major_formatter(FuncFormatter(custom_format))
    ax.yaxis.set_major_formatter(FuncFormatter(custom_format))

    plt.setp(ax.get_xticklabels(), rotation=45, ha="right")

    special_values = {200, 500}
    for tick in ax.get_xticklabels():
        val = float(tick.get_text())
        if val in special_values:
            tick.set_color("red")
            tick.set_fontweight("bold")
        else:
            tick.set_color("black")

    special_values = {10, 25, 500}
    for tick in ax.get_yticklabels():
        val = float(tick.get_text())
        if val in special_values:
            tick.set_color("red")
            tick.set_fontweight("bold")
        else:
            tick.set_color("black")

    ax.tick_params(axis="both", labelsize=8)
    ax.set_aspect("equal")

    ax.set_title("DESP Tableau 9", fontsize=16, pad=15, fontweight="bold", color="blue")
    ax.set_xlabel("DN", loc="right", fontweight="bold")
    ax.set_ylabel("PS (bar)", loc="top", fontweight="bold", rotation=0)

    ax.fill_between((0.1, 10000), (0.5), hatch="///", facecolor="None", edgecolor="black", linewidth=0.0)
    ax.fill_between([0.1, 200], [0.5, 0.5], [10000, 10000], color="yellow", alpha=0.5)
    ax.fill_between([200, 500], [0.5, 0.5], [25, 10], color="yellow", alpha=0.5)
    ax.fill_between([500, 10000], [0.5, 0.5], [10, 10], color="yellow", alpha=0.5)

    labels = [
        (1000, 2000, "II"),
        (1000, 80, "I"),
        (0.15, 50, "Règles de l'Art"),
    ]
    for x, y, txt in labels:
        ax.text(x, y, txt, fontsize=10, color="black", fontweight="bold")

    ax.grid(True, linestyle="--", alpha=0.5)
    ax.tick_params(axis="x", length=5)
    ax.tick_params(axis="y", length=5)
    ax.tick_params(axis="both", which="minor", length=0)


# ------------------------------------------------------------
# Dictionnaire de dispatch
# ------------------------------------------------------------
TRACEURS_TABLEAUX = {
    1: trace_tableau_1,
    2: trace_tableau_2,
    3: trace_tableau_3,
    4: trace_tableau_4,
    5: trace_tableau_5,
    6: trace_tableau_6,
    7: trace_tableau_7,
    8: trace_tableau_8,
    9: trace_tableau_9,
}


def tracer_tableau(tableau: int, ax=None, figsize=(12, 9), dpi=110):
    """
    Trace le tableau DESP demandé (1–9).
    - Si ax=None : crée une nouvelle figure avec la taille imposée.
    - Si ax est fourni : trace dans l'axe existant (PyQt6, subplots, etc.).
    """

    traceur = TRACEURS_TABLEAUX.get(tableau)
    if traceur is None:
        raise ValueError(f"Tableau DESP inconnu : {tableau}")

    # Création figure si nécessaire
    if ax is None:
        fig, ax = plt.subplots(figsize=figsize, dpi=dpi)
    else:
        fig = ax.figure

    # Tracé du tableau
    traceur(ax)

    return fig, ax


if __name__ == "__main__":
    plt.close("all")
    for i in range(1, 10):
        fig, ax = tracer_tableau(i)
        manager = plt.get_current_fig_manager()
        try:
            win = getattr(manager, "window", None)
            if win is not None:
                win.showMaximized()
            else:
                print("Backend non compatible avec showMaximized :", matplotlib.get_backend())
        except Exception:
            print("Backend non compatible avec showMaximized :", matplotlib.get_backend())
        plt.show()
