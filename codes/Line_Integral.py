import matplotlib.pyplot as plt
import numpy as np

# Fine resolution along path segments t in [0, 4]
t_pts = np.linspace(0, 4, 400)
work = np.zeros_like(t_pts)

# Calculate cumulative work piecewise along each segment
for i, t in enumerate(t_pts):
    if t <= 1:  # Segment O -> P
        work[i] = 4.5 * (t**2)
    elif t <= 2:  # Segment P -> Q
        tau = t - 1
        work[i] = 4.5 + (3 * tau + 0.5 * tau**2)
    elif t <= 3:  # Segment Q -> R
        tau = t - 2
        work[i] = 8.0 + (-12 * tau + 4.5 * tau**2)
    else:  # Segment R -> O
        tau = t - 3
        work[i] = 0.5 + (0.5 * tau**2 - tau)

# Initialize single figure plot
plt.figure(figsize=(8, 6))

# Plot line integral accumulation
plt.plot(t_pts, work, color="crimson", lw=2.5)
plt.axhline(0, color="black", linestyle="--", lw=1)

# Annotate key vertices along path
key_t = [0, 1, 2, 3, 4]
key_work = [0.0, 4.5, 8.0, 0.5, 0.0]
key_labels = [
    "O\n(0.0)",
    "P\n(+4.5)",
    "Q (Peak)\n(+8.0)",
    "R\n(+0.5)",
    "O (Return)\n(0.0)",
]

plt.scatter(key_t, key_work, color="darkred", s=50, zorder=5)

for kt, kw, lbl in zip(key_t, key_work, key_labels):
    plt.text(kt, kw + 0.4, lbl, ha="center", fontsize=9, fontweight="bold")

# Add text box indicating final net result
plt.annotate(
    "Net Loop Work = (+8.0) + (-8.0) = 0",
    xy=(2, 8.0),
    xytext=(1.2, 3.5),
    arrowprops=dict(facecolor="black", shrink=0.05, width=1, headwidth=5),
    fontsize=10,
    bbox=dict(boxstyle="round,pad=0.3", facecolor="yellow", alpha=0.3),
)

plt.title(
    r"Cumulative Line Integral $\int_0^t \vec{F} \cdot d\vec{l}$ Around Loop",
    fontsize=12,
)
plt.xlabel("Path Segment Sequence")
plt.ylabel("Accumulated Line Integral (Work)")
plt.xticks(key_t, ["O (0,0)", "P (1,1)", "Q (0,2)", "R (-1,1)", "O (0,0)"])
plt.ylim(-1, 10)
plt.grid(True, linestyle="--", alpha=0.4)

plt.tight_layout()
plt.show()
