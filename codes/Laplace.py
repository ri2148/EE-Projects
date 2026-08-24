import numpy as np
import matplotlib.pyplot as plt

# Domain setup for stem plot
x0, x_end = 0, 5
h = 0.2  # Step size for discrete visualization
N = int((x_end - x0) / h) + 1

x = np.linspace(x0, x_end, N)

# 1. Euler Recurrence Relation: y_{n+1} = 2(1 - h) y_n - (1 - h)^2 y_{n-1}
y_rec = np.zeros(N)
y_rec[0] = 0.0          # y(0) = 0
y_rec[1] = 0.0 + h * 1.0  # y_1 = y_0 + h * y'(0) = h

for n in range(1, N - 1):
    y_rec[n + 1] = 2.0 * (1.0 - h) * y_rec[n] - ((1.0 - h)**2) * y_rec[n - 1]

# 2. Exact Theoretical Solution: y(x) = x * e^(-x)
y_exact = x * np.exp(-x)

# 3. Stem Plot
plt.figure(figsize=(9, 5))

markerline, stemlines, baseline = plt.stem(
    x,
    y_rec,
    linefmt='r-',
    markerfmt='ro',
    basefmt='k-',
    label='Euler Recurrence ($y_n$)',
)
plt.setp(stemlines, linewidth=1.5)
plt.setp(markerline, markersize=6)

plt.plot(
    x,
    y_exact,
    'b--',
    linewidth=2,
    label=r'Theoretical $y(x) = x e^{-x}$',
)

# Mark target point x = ln(2)
x_target = np.log(2)
slope_target = (1.0 - np.log(2)) * 0.5
plt.plot(x_target, x_target * np.exp(-x_target), 'go', markersize=8, label=f'Target Point $x = \\ln(2)$')

plt.xlabel('x')
plt.ylabel('y(x)')
plt.title(r'Stem Plot of Euler Recurrence Relation ($y_{n+1} = 2(1-h)y_n - (1-h)^2 y_{n-1}$)')
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.tight_layout()
plt.show()
