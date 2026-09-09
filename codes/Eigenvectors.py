import matplotlib.pyplot as plt
import numpy as np

# Define vectors
v1 = np.array([1, 1])
v2 = np.array([1, -1])
origin = np.array([0, 0])

# Initialize figure and axes
fig, ax = plt.subplots(figsize=(6, 6))

# Plot vectors starting from the origin
ax.quiver(*origin, *v1, angles='xy', scale_units='xy', scale=1, color='black', label=r'$\mathbf{v}_1 = [1, 1]^T$')
ax.quiver(*origin, *v2, angles='xy', scale_units='xy', scale=1, color='black', label=r'$\mathbf{v}_2 = [1, -1]^T$')

# Axes, grid, and aspect ratio configuration
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.axhline(0, color='black', linewidth=0.8, linestyle='--')
ax.axvline(0, color='black', linewidth=0.8, linestyle='--')
ax.set_aspect('equal')
ax.grid(True, linestyle=':', alpha=0.6)

# Labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Vector Plot')
ax.legend(loc='upper left')

plt.show()
