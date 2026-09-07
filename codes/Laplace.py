import numpy as np
import matplotlib.pyplot as plt

# Simulation parameters
h = 0.1
x_max = 5.0
N = int(round(x_max / h))  # 50 steps -> 51 grid points

# Initialize arrays for numerical solution
x_num = np.linspace(0, x_max, N + 1)
y_num = np.zeros(N + 2)

# Initial conditions: y(0) = 0, y'(0) = 1 -> y_1 = y_0 + h*1 = h
y_num[0] = 0.0
y_num[1] = h

# Second-order Euler Recurrence: y_{n+2} = 2(1-h)y_{n+1} - (1-h)^2 y_n
for n in range(N):
    y_num[n + 2] = 2 * (1 - h) * y_num[n + 1] - ((1 - h)**2) * y_num[n]

# Numerical first derivative: y'_n = (y_{n+1} - y_n) / h
v_num = (y_num[1:N + 2] - y_num[0:N + 1]) / h

# Theoretical continuous curves
x_fine = np.linspace(0, x_max, 500)
y_exact = x_fine * np.exp(-x_fine)
v_exact = (1 - x_fine) * np.exp(-x_fine)

# Target evaluation point x = ln(2)
x_target = np.log(2)
y_target = x_target * np.exp(-x_target)
v_target = (1 - x_target) * np.exp(-x_target)

# Create stacked subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

# Top Subplot: y(x)
ax1.plot(x_fine, y_exact, 'b--', label=r'Theoretical $y(x) = x e^{-x}$', linewidth=2)
ax1.stem(x_num, y_num[:N + 1], linefmt='r-', markerfmt='ro', basefmt='k-', label=r'Euler Recurrence ($y_n$)')
ax1.plot(x_target, y_target, 'go', markersize=8, label=r'Target Point $x = \ln(2)$')
ax1.set_ylabel('$y(x)$')
ax1.set_title(r'Euler Method Solution: $y(x)$ and $y^\prime(x)$ ($h = 0.1$)')
ax1.grid(True, linestyle='--', alpha=0.5)
ax1.legend(loc='upper right')

# Bottom Subplot: y'(x)
ax2.plot(x_fine, v_exact, 'b--', label=r'Theoretical $y^\prime(x) = (1-x) e^{-x}$', linewidth=2)
ax2.stem(x_num, v_num, linefmt='r-', markerfmt='ro', basefmt='k-', label=r'Numerical Derivative ($y_n^\prime$)')
ax2.plot(x_target, v_target, 'go', markersize=8, label=r'Target Point $x = \ln(2)$')
ax2.set_xlabel('$x$')
ax2.set_ylabel(r"$y^\prime(x)$")
ax2.grid(True, linestyle='--', alpha=0.5)
ax2.legend(loc='upper right')

plt.tight_layout()
plt.show()
