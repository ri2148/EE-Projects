import matplotlib.pyplot as plt
import numpy as np

# Categories and probabilities
categories = [
    "Math Only\n(M ∩ E')",
    "English Only\n(M' ∩ E)",
    "Both\n(M ∩ E)",
    "Neither\n(M' ∩ E')"
]
counts = [6, 8, 4, 6]
total = 24
probabilities = [c / total for c in counts]
x = np.arange(len(categories))

# Single uniform color for all stems
color = "#3498db"

fig, ax = plt.subplots(figsize=(8.5, 5))

# Single stem plot call with unified color
markerline, stemlines, baseline = ax.stem(x, probabilities, basefmt=" ")
plt.setp(markerline, color=color, markersize=9, zorder=3)
plt.setp(stemlines, color=color, linewidth=2.5, zorder=2)

# Value annotations above stems
for i, (p, c) in enumerate(zip(probabilities, counts)):
    ax.annotate(
        f"{p:.3f}\n({c}/{total})",
        (x[i], p + 0.015),
        ha='center',
        va='bottom',
        fontsize=10,
        fontweight='bold'
    )

# Formatting axes and labels
ax.set_xticks(x)
ax.set_xticklabels(categories, fontsize=10)
ax.set_xlabel("Student Group / Event", fontsize=11, labelpad=8)
ax.set_ylabel("Probability $P(X)$", fontsize=11)
ax.set_title("Probability Distribution ($N = 24$)", fontsize=13, fontweight='bold', pad=12)

ax.set_ylim(0, 0.42)
ax.set_xlim(-0.5, 3.5)
ax.grid(axis="y", linestyle=":", alpha=0.7)

# Enclose plot in a full border frame
for spine in ax.spines.values():
    spine.set_visible(True)
    spine.set_color('black')

plt.tight_layout()
plt.show()
