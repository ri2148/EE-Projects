import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Constants and initial conditions
mu = 398600  # km^3/s^2
r0 = np.array([8000.0, 9000.0])  # km
v0 = np.array([-6.0, 6.0])       # km/s

# Equation of motion for 2-body problem: d^2 r / dt^2 = -mu * r / |r|^3
def orbit_ode(t, state):
    rx, ry, vx, vy = state
    r_mag = np.sqrt(rx**2 + ry**2)
    ax = -mu * rx / (r_mag**3)
    ay = -mu * ry / (r_mag**3)
    return [vx, vy, ax, ay]

# State vector [x, y, vx, vy]
state0 = [r0[0], r0[1], v0[0], v0[1]]

# Forward and backward integration times (seconds)
t_forward = np.linspace(0, 3000, 1000)
t_backward = np.linspace(0, -3000, 1000)

sol_fwd = solve_ivp(orbit_ode, [0, 3000], state0, t_eval=t_forward, rtol=1e-9, atol=1e-9)
sol_bwd = solve_ivp(orbit_ode, [0, -3000], state0, t_eval=t_backward, rtol=1e-9, atol=1e-9)

# Combine trajectory
x_traj = np.concatenate((sol_bwd.y[0][::-1], sol_fwd.y[0]))
y_traj = np.concatenate((sol_bwd.y[1][::-1], sol_fwd.y[1]))

fig, ax = plt.subplots(figsize=(8, 8))

# Draw Earth at origin
earth_radius = 6371  # km
earth = plt.Circle((0, 0), earth_radius, color='skyblue', alpha=0.6, label='Earth ($R_E = 6371$ km)')
ax.add_patch(earth)
ax.plot(0, 0, 'go', markersize=6, label='Earth Center (Focus)')

# Draw Trajectory
ax.plot(x_traj, y_traj, 'm-', linewidth=2, label='Hyperbolic Trajectory')

# Mark Initial Position & Velocity
ax.plot(r0[0], r0[1], 'ro', markersize=8, label=r'Initial Position $\vec{r}_0 = (8000, 9000)$ km')
ax.quiver(r0[0], r0[1], v0[0], v0[1], angles='xy', scale_units='xy', scale=0.001,
          color='darkred', width=0.008, label=r'Velocity $\vec{v}_0 = (-6, 6)$ km/s')

# Aesthetics
ax.set_title('Hyperbolic Trajectory of the Earth Satellite', fontsize=14, pad=15)
ax.set_xlabel('Perifocal $p$-axis (km)', fontsize=12)
ax.set_ylabel('Perifocal $q$-axis (km)', fontsize=12)
ax.grid(True, linestyle=':', alpha=0.7)
ax.axhline(0, color='black', linewidth=0.8)
ax.axvline(0, color='black', linewidth=0.8)
ax.set_aspect('equal', adjustable='box')
ax.set_xlim(-20000, 25000)
ax.set_ylim(-15000, 30000)
ax.legend(loc='upper left', fontsize=10, framealpha=0.9)

plt.tight_layout()
plt.show()
