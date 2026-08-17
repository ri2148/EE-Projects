import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Initialize figure and axis with appropriate width to accommodate legend
fig, ax = plt.subplots(figsize=(8, 6))

# Parameters
s = 4.0
r1 = 1.0
c1 = (1.0, 1.0)

R = 1.343
c2 = (2.657, 2.657)

# 1. Square
square = patches.Rectangle(
    (0, 0), s, s, 
    linewidth=2, 
    edgecolor='black', 
    facecolor='none', 
    label='Square (s=4.0 cm)'
)
ax.add_patch(square)

# 2. Circle 1
circle1 = patches.Circle(
    c1, r1, 
    linewidth=1.5, 
    edgecolor='blue', 
    facecolor='#a6d5ff', 
    alpha=0.8, 
    label=r'Circle 1 ($r_1=1.0$ cm)'
)
ax.add_patch(circle1)

# 3. Circle 2
circle2 = patches.Circle(
    c2, R, 
    linewidth=1.5, 
    edgecolor='red', 
    facecolor='#fcaeae', 
    alpha=0.7, 
    label=r'Circle 2 (R=1.343 cm)'
)
ax.add_patch(circle2)

# 4. Center Points
ax.plot(c1[0], c1[1], 'bo', markersize=6, label='Center 1: (1.0, 1.0)')
ax.plot(c2[0], c2[1], 'ro', markersize=6, label='Center 2: (2.657, 2.657)')

# 5. Diagonal Line
ax.plot([0, s], [0, s], '--', color='gray', linewidth=1.5, label=r'Diagonal ($y = x$)')

# Formatting plot area
ax.set_xlim(-0.5, 4.5)
ax.set_ylim(-0.5, 4.5)
ax.set_aspect('equal')
ax.grid(True, linestyle='--', alpha=0.5)

# Axis labels
ax.set_xlabel('X (cm)')
ax.set_ylabel('Y (cm)')

# Title fix: adjusted pad & fontsize to keep inside margins
ax.set_title(r'Square (s=4.0 cm) with Tangent Circles ($r_1=1.0$ cm, R=1.343 cm)', pad=12, fontsize=11)

# Legend placed outside
ax.legend(bbox_to_anchor=(1.03, 1), loc='upper left', borderaxespad=0.)

# Adjust layout automatically to ensure title and legend fit properly
plt.tight_layout()

# Save figure with tight bounding box to guarantee no cropping
plt.savefig('circle_plot.png', dpi=300, bbox_inches='tight')

plt.show()
