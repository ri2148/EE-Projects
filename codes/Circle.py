import numpy as np
import matplotlib.pyplot as plt
#If using termux
import subprocess
import shlex
#end if

# Import custom matrix and vector modules
from CoordGeo.conics.funcs import circ_gen
from CoordGeo.line.funcs import line_gen
from CoordGeo.plotting.funcs import label_pts

# Initialize figure
fig, ax = plt.subplots(figsize=(9, 6), layout='constrained')

# Parameters
s = 4.0
r1 = 1.0
c1 = np.array([1.0, 1.0]).reshape(-1, 1)

R = 1.343
c2 = np.array([2.657, 2.657]).reshape(-1, 1)

# 1. Square Vertices & Side Generation
A_sq = np.array([0.0, 0.0]).reshape(-1, 1)
B_sq = np.array([s, 0.0]).reshape(-1, 1)
C_sq = np.array([s, s]).reshape(-1, 1)
D_sq = np.array([0.0, s]).reshape(-1, 1)

x_AB = line_gen(A_sq, B_sq)
x_BC = line_gen(B_sq, C_sq)
x_CD = line_gen(C_sq, D_sq)
x_DA = line_gen(D_sq, A_sq)

# Plot Square using line points
ax.plot(x_AB[0, :], x_AB[1, :], 'k-', linewidth=2, label='Square (s=4.0 cm)')
ax.plot(x_BC[0, :], x_BC[1, :], 'k-', linewidth=2)
ax.plot(x_CD[0, :], x_CD[1, :], 'k-', linewidth=2)
ax.plot(x_DA[0, :], x_DA[1, :], 'k-', linewidth=2)

# 2. Circle 1
x_circ1 = circ_gen(c1, r1)
ax.plot(x_circ1[0, :], x_circ1[1, :], 'b-', linewidth=1.5, label=r'Circle 1 ($r_1=1.0$ cm)')
ax.fill(x_circ1[0, :], x_circ1[1, :], color='#a6d5ff', alpha=0.8)

# 3. Circle 2
x_circ2 = circ_gen(c2, R)
ax.plot(x_circ2[0, :], x_circ2[1, :], 'r-', linewidth=1.5, label=r'Circle 2 (R=1.343 cm)')
ax.fill(x_circ2[0, :], x_circ2[1, :], color='#fcaeae', alpha=0.7)

# 4. Center Points & Labeling
centers = np.block([c1, c2])
ax.plot(c1[0, 0], c1[1, 0], 'bo', markersize=6, label='Center 1: (1.0, 1.0)')
ax.plot(c2[0, 0], c2[1, 0], 'ro', markersize=6, label='Center 2: (2.657, 2.657)')
label_pts(centers, ['C1', 'C2'])

# 5. Diagonal Line
x_diag = line_gen(A_sq, C_sq)
ax.plot(x_diag[0, :], x_diag[1, :], '--', color='gray', linewidth=1.5, label=r'Diagonal ($y = x$)')

# Formatting plot area
ax.set_xlim(-0.5, 4.5)
ax.set_ylim(-0.5, 4.5)
ax.set_aspect('equal')
ax.grid(True, linestyle='--', alpha=0.5)

# Remove the outer plot box (spines)
for spine in ax.spines.values():
    spine.set_visible(False)

# Axis labels
ax.set_xlabel('X (cm)')
ax.set_ylabel('Y (cm)')

# Legend
ax.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0., frameon=True)

#If using termux
plt.savefig('figs/Circle.png')
subprocess.run(shlex.split("termux-open figs/Circle.png"))

#else
#plt.show()
