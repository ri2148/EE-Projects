import numpy as np
import matplotlib.pyplot as plt

# Define x range around critical points (-1.5 and 0)
x = np.linspace(-3.5, 2.0, 500)
y = np.abs(x) + np.abs(2*x + 3)

fig, ax = plt.subplots(figsize=(8, 6))

# Plot the function
ax.plot(x, y, 'b-', linewidth=2.5, label=r'$f(x) = |x| + |2x + 3|$')

# Highlight critical points
crit_x = [-1.5, 0]
crit_y = [1.5, 3.0]
ax.plot(crit_x, crit_y, 'ro', markersize=8, zorder=5)

# Add reference line for minimum y-value
ax.axhline(1.5, color='r', linestyle='--', alpha=0.7, label='Min Value = 1.5')

# Labels and Grid
ax.set_title(r'Graph of $f(x) = |x| + |2x + 3|$', fontsize=14, pad=15)
ax.set_xlabel('$x$', fontsize=12)
ax.set_ylabel('$f(x)$', fontsize=12)
ax.grid(True, linestyle=':', alpha=0.7)
ax.axhline(0, color='black', linewidth=1)
ax.axvline(0, color='black', linewidth=1)

# Limits
ax.set_xlim(-3.5, 2.0)
ax.set_ylim(0, 9)
plt.tight_layout()
plt.show()
