import cvxpy as cp
import numpy as np
from scipy.linalg import cholesky

# Define the size of the matrix
n = 6

# Create a symmetric matrix variable
X = cp.Variable((n, n), symmetric=True)

# Define the objective function (minimize the Frobenius norm of X)
objective = cp.Minimize(cp.norm(X, 'fro'))

# Define the constraints (X must be positive semidefinite)
constraints = [
    X >> 0,
    X[0][3] == -1,
    X[0][4] == 3/2,
    X[0][5] == 3/2,
    X[1][3] == 3/2,
    X[1][4] == -1,
    X[1][5] == 3/2,
    X[2][3] == 3/2,
    X[2][4] == 3/2,
    X[2][5] == -1,   
    cp.trace(X) == 15]


# Form and solve the problem
problem = cp.Problem(objective, constraints)
problem.solve()

# Print the result
# print("Optimal value:", problem.value)
# for row in X.value:
#     print(row)
#

# Using SciPy (if available)
from scipy.linalg import cholesky
L = cholesky(X.value, lower=True, check_finite=False)
print(X[0] * L.T)

print("Matrix", L)

print((0.000187998487) ** 0.5)


print("Optimal matrix X:\n", X.value)