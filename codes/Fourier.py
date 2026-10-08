import numpy as np
import matplotlib.pyplot as plt
#If using termux
import subprocess
import shlex
#end if

# Import custom modules matching project package hierarchy
from CoordGeo.line.funcs import line_gen
from CoordGeo.plotting.funcs import label_pts

# Parameters
T0 = 2.0
f0 = 1.0 / T0  # Fundamental frequency f0 = 0.5 Hz
N_harmonics = 50  # Number of Fourier series terms

# Time axis array
t = np.linspace(-3.0, 3.0, 1000)

# 1. Exact Periodic Square Wave x(t)
# rect(t) is 1 for |t| <= 0.5, periodic with T0 = 2
t_mod = (t + T0 / 2.0) % T0 - T0 / 2.0
x_exact = np.where(np.abs(t_mod) <= 0.5, 1.0, 0.0)

# 2. Fourier Series Reconstruction x(t) = sum(c_k * e^(j 2pi k f0 t))
x_reconstructed = np.zeros_like(t, dtype=np.complex128)

# k = 0 DC component: limit as k->0 of sin(pi k / 2) / (pi k) = 1/2
c0 = 0.5
x_reconstructed += c0

for k in range(-N_harmonics, N_harmonics + 1):
    if k == 0:
        continue
    # c_k = sin(pi * k / 2) / (pi * k)
    c_k = np.sin(np.pi * k / 2.0) / (np.pi * k)
    x_reconstructed += c_k * np.exp(1j * 2.0 * np.pi * k * f0 * t)

# The reconstructed signal is real
x_reconstructed = np.real(x_reconstructed)

# Figure Setup
fig, ax = plt.subplots(figsize=(10, 5))

# Plot exact square wave and Fourier approximation
ax.plot(t, x_exact, 'k--', linewidth=2, label=r'Exact Periodic $\text{rect}(t)$ ($T_0=2$)')
ax.plot(t, x_reconstructed, 'r-', linewidth=1.5, label=f'Fourier Series Reconstruction ($N={N_harmonics}$)')

# Coordinate Axes using line_gen
A_xaxis = np.array([-3.0, 0.0]).reshape(-1, 1)
B_xaxis = np.array([3.0, 0.0]).reshape(-1, 1)
x_axis = line_gen(A_xaxis, B_xaxis)
ax.plot(x_axis[0, :], x_axis[1, :], color='black', linewidth=0.8)

A_yaxis = np.array([0.0, -0.2]).reshape(-1, 1)
B_yaxis = np.array([0.0, 1.3]).reshape(-1, 1)
y_axis = line_gen(A_yaxis, B_yaxis)
ax.plot(y_axis[0, :], y_axis[1, :], color='black', linewidth=0.8)

# Key points for labeling
key_pts = np.block([
    np.array([0.0, 1.0]).reshape(-1, 1),
    np.array([0.5, 0.5]).reshape(-1, 1),
    np.array([-0.5, 0.5]).reshape(-1, 1)
])
ax.plot(key_pts[0, :], key_pts[1, :], 'bo', markersize=5)
label_pts(key_pts, ['Peak (0, 1)', 't = 0.5', 't = -0.5'])

# Formatting
ax.set_xlabel('$t$', fontsize=12)
ax.set_ylabel('$x(t)$', fontsize=12)
ax.set_title(r'Fourier Series Verification: $c_k = \frac{\sin(\pi k / 2)}{\pi k}$', fontsize=13)
ax.set_xlim(-3.0, 3.0)
ax.set_ylim(-0.3, 1.3)
ax.grid(True, linestyle=':', alpha=0.7)
ax.legend(loc='upper right')

plt.tight_layout()

#If using termux
plt.savefig("Fourier.png")
subprocess.run(shlex.split("termux-open Fourier.png"))
#else
#plt.show()
