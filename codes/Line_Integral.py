import matplotlib.pyplot as plt
import numpy as np
#If using termux
import subprocess
import shlex
#end if
# Import custom modules
from CoordGeo.line.funcs import line_gen
from CoordGeo.plotting.funcs import label_pts

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
fig, ax = plt.subplots(figsize=(8, 6))

# Plot line integral accumulation
ax.plot(t_pts, work, color="crimson", lw=2.5)

# Generate baseline zero-axis using line_gen from funcs_1
A_base = np.array([0.0, 0.0]).reshape(-1, 1)
B_base = np.array([4.0, 0.0]).reshape(-1, 1)
x_base = line_gen(A_base, B_base)
ax.plot(x_base[0, :], x_base[1, :], color="black", linestyle="--", lw=1)

# Key vertices along path defined as a 2xN point matrix for label_pts
key_t = [0.0, 1.0, 2.0, 3.0, 4.0]
key_work = [0.0, 4.5, 8.0, 0.5, 0.0]
key_pts = np.block([[np.array(key_t)], [np.array(key_work)]])

key_labels = [
    "O (0.0)",
    "P (+4.5)",
    "Q (Peak) (+8.0)",
    "R (+0.5)",
    "O (Return) (0.0)",
]

# Plot vertex points and label them using funcs_2 label_pts
ax.plot(key_pts[0, :], key_pts[1, :], "o", color="darkred", markersize=6, zorder=5)
label_pts(key_pts, key_labels)

# Plot formatting
ax.set_xlabel("Path Segment Sequence")
ax.set_ylabel("Accumulated Line Integral (Work)")
ax.set_xticks(key_t, ["O (0,0)", "P (1,1)", "Q (0,2)", "R (-1,1)", "O (0,0)"])
ax.set_ylim(-1, 10)
ax.grid(True, linestyle="--", alpha=0.4)

plt.tight_layout()
#If using termux
plt.savefig("figs/Line_Integral.png")
subprocess.run(shlex.split("termux-open Line_Integral.png"))
#else
#plt.show()
