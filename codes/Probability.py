import matplotlib.pyplot as plt
import numpy as np

# Total students
N = 24

# Categories
categories = np.array([
    "Math Only\n(M ∩ E')",
    "English Only\n(M' ∩ E)",
    "Both\n(M ∩ E)",
    "Neither\n(M' ∩ E')"
])

# Counts and probabilities using NumPy
counts = np.array([6, 8, 4, 6])
probabilities = counts / N

# Colors for visual clarity
colors = ['#3498db', '#2ecc71', '#e74c3c', '#95a5a6']

# Create plot
plt.figure(figsize=(8, 5))
bars = plt.bar(categories, probabilities, color=colors, edgecolor='black', width=0.5)

# Label heights with exact probability and fraction
for bar, count, prob in zip(bars, counts, probabilities):
    yval = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2.0, 
        yval + 0.01, 
        f'{prob:.3f}\n({count}/{N})', 
        ha='center', 
        va='bottom', 
        fontsize=10, 
        fontweight='bold'
    )

plt.title("Probability Distribution ($N = 24$)", fontsize=13, fontweight='bold')
plt.xlabel("Student Group / Event", fontsize=11)
plt.ylabel("Probability $P(X)$", fontsize=11)
plt.ylim(0, 0.42)
plt.grid(axis='y', linestyle=':', alpha=0.7)

plt.tight_layout()
plt.show()
