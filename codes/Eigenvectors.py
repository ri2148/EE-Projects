import numpy as np
import matplotlib.pyplot as plt

# Define the eigenvectors
v1 = np.array([1, 1])
v2 = np.array([1, -1])

# Origin (0, 0)
origin = np.array([0, 0])

# Create figure
fig, ax = plt.subplots(figsize=(7, 7))

# Plot Eigenspaces (lines spanned by eigenvectors)
x_span = np.linspace(-2.5, 2.5, 100)
ax.plot(x_span, x_span, 'b--', alpha=0.4, label=r'Eigenspace $\lambda_1 = a+b$ ($y = x$)')
ax.plot(x_span, -x_span, 'r--', alpha=0.4, label=r'Eigenspace $\lambda_2 = d-b$ ($y = -x$)')

# Plot Eigenvectors as arrows
ax.quiver(*origin, *v1, angles='xy', scale_units='xy', scale=1, 
          color='blue', width=0.015, label=r'$v_1 = [1, 1]^T$')
ax.quiver(*origin, *v2, angles='xy', scale_units='xy', scale=1, 
          color='red', width=0.015, label=r'$v_2 = [1, -1]^T$')

# Annotate vectors directly on the plot
ax.text(1.1, 1.1, r'$v_1(1, 1)$', fontsize=12, color='blue', fontweight='bold')
ax.text(1.1, -1.1, r'$v_2(1, -1)$', fontsize=12, color='red', fontweight='bold')

# Configure grid and axes
ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-2.5, 2.5)
ax.axhline(0, color='black', linewidth=1)
ax.axvline(0, color='black', linewidth=1)
ax.grid(True, linestyle=':', alpha=0.7)
ax.set_aspect('equal', adjustable='box')

# Labels and Title
ax.set_title('Eigenvectors of Matrix $A$', fontsize=14, pad=15)
ax.set_xlabel('$x$', fontsize=12)
ax.set_ylabel('$y$', fontsize=12)
ax.legend(loc='upper left', framealpha=0.9)

# Display plot
plt.tight_layout()
plt.show()
