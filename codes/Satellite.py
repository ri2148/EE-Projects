import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# --- Constants & Initial Conditions ---
mu = 398600.0  # km^3/s^2
r0 = np.array([8000.0, 9000.0])  # km
v0 = np.array([-6.0, 6.0])       # km/s
earth_radius = 6371  # km

# --- Equation of Motion (Two-Body Problem) ---
def orbit_ode(t, state):
    rx, ry, vx, vy = state
    r_mag = np.sqrt(rx**2 + ry**2)
    ax = -mu * rx / (r_mag**3)
    ay = -mu * ry / (r_mag**3)
    return [vx, vy, ax, ay]

state0 = [r0[0], r0[1], v0[0], v0[1]]

# Integrate trajectories (-8000s to +8000s)
t_forward = np.linspace(0, 8000, 1500)
t_backward = np.linspace(0, -8000, 1500)

sol_fwd = solve_ivp(orbit_ode, [0, 8000], state0, t_eval=t_forward, rtol=1e-9, atol=1e-9)
sol_bwd = solve_ivp(orbit_ode, [0, -8000], state0, t_eval=t_backward, rtol=1e-9, atol=1e-9)

# Primary Physical Branch
x_traj1 = np.concatenate((sol_bwd.y[0][::-1], sol_fwd.y[0]))
y_traj1 = np.concatenate((sol_bwd.y[1][::-1], sol_fwd.y[1]))

# --- Hyperbola Geometric Parameters ---
r0_mag = np.linalg.norm(r0)
v0_mag = np.linalg.norm(v0)

energy = 0.5 * v0_mag**2 - mu / r0_mag
a = mu / (2.0 * energy)

h = r0[0] * v0[1] - r0[1] * v0[0]
v_cross_h = np.array([v0[1] * h, -v0[0] * h])
e_vec = v_cross_h / mu - r0 / r0_mag

r_center = -a * e_vec
vacant_focus = 2 * r_center

# Secondary Branch
x_traj2 = 2 * r_center[0] - x_traj1
y_traj2 = 2 * r_center[1] - y_traj1

# --- Plotting Subplots ---
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7.5))

# SUBPLOT 1: Near-Earth Trajectory (Zoomed)
earth1 = plt.Circle((0, 0), earth_radius, color='skyblue', alpha=0.6, label='Earth ($R_E = 6371$ km)')
ax1.add_patch(earth1)
ax1.plot(0, 0, 'go', markersize=6, label='Earth Center (Focus)')
ax1.plot(x_traj1, y_traj1, 'm-', linewidth=2, label='Hyperbolic Trajectory')
ax1.plot(r0[0], r0[1], 'ro', markersize=8, label=r'Initial Position $\vec{r}_0$')

# Fixed vector arrow scale (scale=0.001 keeps length at 6,000 km)
ax1.quiver(r0[0], r0[1], v0[0], v0[1], angles='xy', scale_units='xy', scale=0.001,
           color='darkred', width=0.008, label=r'Velocity $\vec{v}_0$')

ax1.set_title('Near-Earth Trajectory (Primary Branch)', fontsize=13, pad=12)
ax1.set_xlabel('Perifocal $p$-axis (km)', fontsize=11)
ax1.set_ylabel('Perifocal $q$-axis (km)', fontsize=11)
ax1.grid(True, linestyle=':', alpha=0.7)
ax1.axhline(0, color='black', linewidth=0.8)
ax1.axvline(0, color='black', linewidth=0.8)
ax1.set_aspect('equal', adjustable='box')
ax1.set_xlim(-20000, 25000)
ax1.set_ylim(-15000, 30000)
ax1.legend(loc='upper left', fontsize=9, framealpha=0.9)

# SUBPLOT 2: Global Orbit View
earth2 = plt.Circle((0, 0), earth_radius, color='skyblue', alpha=0.6, label='Earth ($R_E = 6371$ km)')
ax2.add_patch(earth2)
ax2.plot(0, 0, 'go', markersize=6, label='Earth Center (Primary Focus)')
ax2.plot(r_center[0], r_center[1], 'kx', markersize=8, markeredgewidth=2, label='Hyperbola Center')
ax2.plot(vacant_focus[0], vacant_focus[1], 'c*', markersize=9, label='Vacant Focus')

ax2.plot(x_traj1, y_traj1, 'm-', linewidth=2, label='Primary Branch (Physical)')
ax2.plot(x_traj2, y_traj2, 'b--', linewidth=2, label='Secondary Branch (Mathematical)')

ax2.plot(r0[0], r0[1], 'ro', markersize=8, label=r'Initial Position $\vec{r}_0$')

# Fixed vector arrow scale for macro view (scale=0.0003 keeps length proportional at ~28,000 km)
ax2.quiver(r0[0], r0[1], v0[0], v0[1], angles='xy', scale_units='xy', scale=0.0003,
           color='darkred', width=0.006, label=r'Velocity $\vec{v}_0$')

ax2.set_title('Global Orbit View (Both Hyperbolic Branches)', fontsize=13, pad=12)
ax2.set_xlabel('Perifocal $p$-axis (km)', fontsize=11)
ax2.set_ylabel('Perifocal $q$-axis (km)', fontsize=11)
ax2.grid(True, linestyle=':', alpha=0.7)
ax2.axhline(0, color='black', linewidth=0.8)
ax2.axvline(0, color='black', linewidth=0.8)
ax2.set_aspect('equal', adjustable='box')
ax2.set_xlim(-150000, 30000)
ax2.set_ylim(-140000, 40000)
ax2.legend(loc='upper left', fontsize=9, framealpha=0.9)

plt.tight_layout()
plt.show()
