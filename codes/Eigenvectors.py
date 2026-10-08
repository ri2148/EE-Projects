import numpy as np
import matplotlib.pyplot as plt

#If using termux
import subprocess
import shlex
#end if
# Import custom matrix and vector modules
from CoordGeo.line.funcs import line_gen
from CoordGeo.plotting.funcs import label_pts

# Initialize figure and axes
fig, ax = plt.subplots(figsize=(6, 6))

# Define origin and vectors as 2x1 column matrices
origin = np.array([0, 0]).reshape(-1, 1)
v1 = np.array([1, 1]).reshape(-1, 1)
v2 = np.array([1, -1]).reshape(-1, 1)

# Generate line points from origin to vector endpoints
x_v1 = line_gen(origin, v1)
x_v2 = line_gen(origin, v2)

# Plot vector lines
ax.plot(x_v1[0, :], x_v1[1, :], color='black', linewidth=2, label=r'$\mathbf{v}_1 = [1, 1]^T$')
ax.plot(x_v2[0, :], x_v2[1, :], color='black', linewidth=2, label=r'$\mathbf{v}_2 = [1, -1]^T$')

# Plot vector endpoints
points = np.block([v1, v2])
ax.plot(v1[0, 0], v1[1, 0], 'ko', markersize=5)
ax.plot(v2[0, 0], v2[1, 0], 'ko', markersize=5)

# Label point endpoints using funcs_2
label_pts(points, [r'$\mathbf{v}_1$', r'$\mathbf{v}_2$'])

# Axes, grid, and aspect ratio configuration
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.axhline(0, color='black', linewidth=0.8, linestyle='--')
ax.axvline(0, color='black', linewidth=0.8, linestyle='--')
ax.set_aspect('equal')
ax.grid(True, linestyle=':', alpha=0.6)

# Labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.legend(loc='upper left')
#If using termux
plt.savefig("figs/Eigenvectors.png")
subprocess.run(shlex.split("termux-open figs/Eigenvecotrs.png"))
#else
#plt.show()
