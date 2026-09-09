import cvxpy as cp

# Define the decision variable
x = cp.Variable()

# Define the convex objective function f(x) = |x| + |2x + 3|
objective = cp.Minimize(cp.abs(x) + cp.abs(2 * x + 3))

# Formulate and solve the problem
problem = cp.Problem(objective)
min_value = problem.solve()

print(f"Optimal x: {x.value:.4f}")
print(f"Minimum value of f(x): {min_value:.4f}")
