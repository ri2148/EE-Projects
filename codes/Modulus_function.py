import numpy as np
import matplotlib.pyplot as plt
import cvxpy as cp
#If using termux
import subprocess
import shlex
#end if

# Import custom modules
from CoordGeo.line.funcs import line_gen
from CoordGeo.plotting.funcs import label_pts

# Define the decision variable
x_opt = cp.Variable()

# Define the convex objective function f(x) = |x| + |2x + 3|
objective = cp.Minimize(cp.abs(x_opt) + cp.abs(2 * x_opt + 3))

# Formulate and solve the problem
problem = cp.Problem(objective)
min_value = problem.solve()

print(f"Optimal x: {x_opt.value:.4f}")
print(f"Minimum value of f(x): {min_value:.4f}")

# Define x range around critical points (-1.5 and 0)
x_vals = np.linspace(-3.5, 2.0, 500)
y_vals = np.abs(x_vals) + np.abs(2 * x_vals + 3)

fig, ax = plt.subplots(figsize=(8, 6))

# Plot the function
ax.plot(x_vals, y_vals, 'b-', linewidth=2.5, label=r'$f(x) = |x| + |2x + 3|$')

# Define critical points as a 2xN matrix
crit_pts = np.block([
    np.array([-1.5, 1.5]).reshape(-1, 1),
    np.array([0.0, 3.0]).reshape(-1, 1)
])

# Highlight critical points and annotate using label_pts
ax.plot(crit_pts[0, :], crit_pts[1, :], 'ro', markersize=8, zorder=5)
label_pts(crit_pts, ['Min (-1.5, 1.5)', '(0, 3)'])

# Generate minimum value reference line using line_gen from funcs_1
A_min = np.array([-3.5, 1.5]).reshape(-1, 1)
B_min = np.array([2.0, 1.5]).reshape(-1, 1)
x_min_line = line_gen(A_min, B_min)
ax.plot(x_min_line[0, :], x_min_line[1, :], 'r--', alpha=0.7, label='Min Value = 1.5')

# Generate coordinate axes using line_gen from funcs_1
A_xaxis = np.array([-3.5, 0.0]).reshape(-1, 1)
B_xaxis = np.array([2.0, 0.0]).reshape(-1, 1)
x_axis = line_gen(A_xaxis, B_xaxis)
ax.plot(x_axis[0, :], x_axis[1, :], color='black', linewidth=1)

A_yaxis = np.array([0.0, 0.0]).reshape(-1, 1)
B_yaxis = np.array([0.0, 9.0]).reshape(-1, 1)
y_axis = line_gen(A_yaxis, B_yaxis)
ax.plot(y_axis[0, :], y_axis[1, :], color='black', linewidth=1)

# Labels, Grid, and Limits
ax.set_xlabel('$x$', fontsize=12)
ax.set_ylabel('$f(x)$', fontsize=12)
ax.grid(True, linestyle=':', alpha=0.7)
ax.set_xlim(-3.5, 2.0)
ax.set_ylim(0, 9)
ax.legend(loc='upper right')

plt.tight_layout()
#if using termux
plt.savefig("Modulus_function.png")
subprocess.run(shlex.split("termux-open Modulus_function.png"))
#else
#plt.show()
