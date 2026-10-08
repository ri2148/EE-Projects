import numpy as np
import matplotlib.pyplot as plt

#If using termux
import subprocess
import shlex
#end if
# Import custom modules
from CoordGeo.line.funcs import line_gen
from CoordGeo.plotting.funcs import label_pts

# System Parameters
E = 200e9        # Pa (200 GPa)
A = 100e-6       # m^2 (100 mm^2)
L = 100e-3       # m (100 mm)
k_spring = 200e6 # N/m (200 kN/mm)
M = 100          # kg

# Equivalent Stiffness & Natural Frequency Calculation
k_bar = (A * E) / L
k_eq = (k_bar * k_spring) / (k_bar + k_spring)
omega_n = np.sqrt(k_eq / M) # rad/s (1000 rad/s)

# Time period T = 2*pi / omega_n
T = 2 * np.pi / omega_n # seconds (~0.00628 s = 6.28 ms)

# Define time array for 3 complete cycles
t = np.linspace(0, 3 * T, 1000) # seconds
t_ms = t * 1000                 # milliseconds

# Initial conditions: Displacement X_0 = 1.0 mm
X0 = 1.0 # mm
x_t = X0 * np.cos(omega_n * t)                          # Displacement (mm)
v_t = -X0 * (omega_n / 1000) * np.sin(omega_n * t)         # Velocity (m/s)
a_t = -X0 * ((omega_n / 1000)**2) * np.cos(omega_n * t)    # Acceleration (km/s^2)

# Plotting SHM Response
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(9, 8), sharex=True)

# Generate zero reference baseline axis using line_gen from funcs_1
A_base = np.array([0.0, 0.0]).reshape(-1, 1)
B_base = np.array([3 * T * 1000, 0.0]).reshape(-1, 1)
x_base = line_gen(A_base, B_base)

# 1. Displacement Plot
ax1.plot(t_ms, x_t, 'b-', linewidth=2, label=r'Displacement $x(t) = X_0 \cos(\omega_n t)$')
ax1.plot(x_base[0, :], x_base[1, :], color='black', linewidth=0.8)
ax1.set_ylabel('Displacement (mm)', fontsize=11, color='blue')
ax1.grid(True, linestyle=':', alpha=0.7)

# Mark 1st Time Period T using line_gen vertical boundary
P1 = np.array([T * 1000, -1.2]).reshape(-1, 1)
P2 = np.array([T * 1000, 1.2]).reshape(-1, 1)
x_period = line_gen(P1, P2)
ax1.plot(x_period[0, :], x_period[1, :], 'r--', alpha=0.7)

# Point annotation using label_pts from funcs_2
period_pt = np.array([T * 1000, 0.5]).reshape(-1, 1)
ax1.plot(period_pt[0, 0], period_pt[1, 0], 'ro', markersize=5)
label_pts(period_pt, [f'T = {T*1000:.2f} ms'])

ax1.legend(loc='upper right', framealpha=0.9)

# 2. Velocity Plot
ax2.plot(t_ms, v_t, 'g-', linewidth=2, label=r'Velocity $v(t) = -\omega_n X_0 \sin(\omega_n t)$')
ax2.plot(x_base[0, :], x_base[1, :], color='black', linewidth=0.8)
ax2.set_ylabel('Velocity (m/s)', fontsize=11, color='green')
ax2.grid(True, linestyle=':', alpha=0.7)
ax2.legend(loc='upper right', framealpha=0.9)

# 3. Acceleration Plot
ax3.plot(t_ms, a_t, 'r-', linewidth=2, label=r'Acceleration $a(t) = -\omega_n^2 X_0 \cos(\omega_n t)$')
ax3.plot(x_base[0, :], x_base[1, :], color='black', linewidth=0.8)
ax3.set_xlabel('Time $t$ (ms)', fontsize=11)
ax3.set_ylabel('Acc. (km/s$^2$)', fontsize=11, color='red')
ax3.grid(True, linestyle=':', alpha=0.7)
ax3.legend(loc='upper right', framealpha=0.9)

plt.tight_layout()
#If using termx
plt.savefig("figs/Spring.png")
subprocess.run(shlex.split("termux-open Spring.png"))
#else
#plt.show()
