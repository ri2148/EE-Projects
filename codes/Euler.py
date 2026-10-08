import numpy as np
import matplotlib.pyplot as plt

#If using termux
import subprocess
import shlex
#end if
# Import custom modules
from CoordGeo.line.funcs import line_gen
from CoordGeo.plotting.funcs import label_pts
from CoordGeo.matrix.funcs import polyvalm
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

# Matrix form of the second-order recurrence relation using state-space representation
# State vector: [y_{n+1}, y_n]^T
# Companion matrix: A = [[2*(1-h), -(1-h)^2], [1, 0]]
A = np.array([
    [2 * (1 - h), -((1 - h)**2)],
    [1, 0]
])

# Compute recurrence using matrix power polynomial evaluation (polyvalm)
# Characteristic polynomial: lambda^2 - 2*(1-h)*lambda + (1-h)^2
char_poly = np.array([1, -2 * (1 - h), (1 - h)**2])

for n in range(N):
    state = np.array([y_num[n + 1], y_num[n]]).reshape(-1, 1)
    next_state = A @ state
    y_num[n + 2] = next_state[0, 0]

# Verify system polynomial zero evaluation at transition matrix A
poly_zero = polyvalm(char_poly, A)

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

# Define column vector target points for labeling
target_pt_y = np.array([x_target, y_target]).reshape(-1, 1)
target_pt_v = np.array([x_target, v_target]).reshape(-1, 1)

# Create stacked subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

# Top Subplot: y(x)
ax1.plot(x_fine, y_exact, 'b--', label=r'Theoretical $y(x) = x e^{-x}$', linewidth=2)
ax1.stem(x_num, y_num[:N + 1], linefmt='r-', markerfmt='ro', basefmt='k-', label=r'Euler Recurrence ($y_n$)')
ax1.plot(target_pt_y[0, 0], target_pt_y[1, 0], 'go', markersize=8, label=r'Target Point $x = \ln(2)$')
label_pts(target_pt_y, [r'$x=\ln(2)$'])

# Baseline axis generation using funcs_1 line_gen
x_base_top = line_gen(np.array([0, 0]).reshape(-1, 1), np.array([x_max, 0]).reshape(-1, 1))
ax1.plot(x_base_top[0, :], x_base_top[1, :], 'k-', linewidth=0.5)

ax1.set_ylabel('$y(x)$')
ax1.grid(True, linestyle='--', alpha=0.5)
ax1.legend(loc='upper right')

# Bottom Subplot: y'(x)
ax2.plot(x_fine, v_exact, 'b--', label=r'Theoretical $y^\prime(x) = (1-x) e^{-x}$', linewidth=2)
ax2.stem(x_num, v_num, linefmt='r-', markerfmt='ro', basefmt='k-', label=r'Numerical Derivative ($y_n^\prime$)')
ax2.plot(target_pt_v[0, 0], target_pt_v[1, 0], 'go', markersize=8, label=r'Target Point $x = \ln(2)$')
label_pts(target_pt_v, [r'$x=\ln(2)$'])

# Baseline axis generation using funcs_1 line_gen
x_base_bot = line_gen(np.array([0, 0]).reshape(-1, 1), np.array([x_max, 0]).reshape(-1, 1))
ax2.plot(x_base_bot[0, :], x_base_bot[1, :], 'k-', linewidth=0.5)

ax2.set_xlabel('$x$')
ax2.set_ylabel(r"$y^\prime(x)$")
ax2.grid(True, linestyle='--', alpha=0.5)
ax2.legend(loc='upper right')

plt.tight_layout()
#If using termux
plt.savefig("figs/Euler.png")
subprocess.run(shlex.split("termux-open Euler.png"))
#else
#plt.show()
