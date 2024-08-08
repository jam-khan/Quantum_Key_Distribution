import cvxpy as cp
import numpy as np
from scipy.linalg import cholesky
import sympy as sp
from sympy import Rational, nsimplify

def recover_exact_form(decimal_number):
    # Try to find an exact rational form
    rational_approx = nsimplify(decimal_number, rational=True)
    return rational_approx

# Example usage
# decimal_number = 0.471301344131
# exact_form = recover_exact_form(decimal_number)
# print(f"The exact form of {decimal_number} is {exact_form}")

def eigen_decomposition(matrix):
    # Compute eigenvalues and eigenvectors
    eigenvalues, eigenvectors = np.linalg.eigh(matrix)
    # Zero out negative eigenvalues
    eigenvalues[eigenvalues < 0] = 0
    # Reconstruct the matrix
    L = eigenvectors @ np.diag(np.sqrt(eigenvalues))
    return L



# Define the size of the matrix
n = 6

# Create a symmetric matrix variable
X = cp.Variable((n, n), symmetric=True)

# Define the objective function (minimize the Frobenius norm of X)
objective = cp.Minimize(cp.norm(X, 'fro'))

# Define the constraints (X must be positive semidefinite)
alpha = 0.05

# Below constraints will provide SOS decomposition for
# B' s.t I' = B' + alpha * (A0 - B0)^2
# constraints = [
#     X >> 0,
#     X[0][1] == 0.0,
#     X[0][2] == 0.0,
#     X[1][0] == 0.0,
#     X[1][2] == 0.0,
#     X[0][3] == -1 * (1 - alpha),
#     X[0][4] == 3/2,
#     X[0][5] == 3/2,
#     X[1][3] == 3/2,
#     X[1][4] == -1,
#     X[1][5] == 3/2,
#     X[2][3] == 3/2,
#     X[2][4] == 3/2,
#     X[2][5] == -1,
#     cp.trace(X) == 15 - 2 * alpha]

# Below constraints will provide SOS decomposition for
# B' s.t I' = B' + alpha * (A1 - B1)^2
constraints = [
    X >> 0,
    
    X[0][1] == 0.0,
    X[0][2] == 0.0,
    X[0][3] == -1.0 * (1 - alpha),
    X[0][4] == 1.50,
    X[0][5] == 1.50,
    
    X[1][0] == 0.0,
    X[1][2] == 0.0,
    X[1][3] == 1.50,
    X[1][4] == -1.0,
    X[1][5] == 1.50,
    
    X[2][0] == 0.0,
    X[2][1] == 0.0,
    X[2][3] == 1.50,
    X[2][4] == 1.50,
    X[2][5] == -1.0,
    
    X[3][0] == -1.0 * (1 - alpha),
    X[3][1] == 1.50,
    X[3][2] == 1.50,
    X[3][4] == 0,
    X[3][5] == 0,
    
    X[4][0] == 1.50,
    X[4][1] == -1.00,
    X[4][2] == 1.50,
    X[4][3] == 0,
    X[4][5] == 0,
    
    X[5][0] == 1.50,
    X[5][1] == 1.50,
    X[5][2] == -1.00,
    X[5][3] == 0,
    X[5][4] == 0,
    
    X[0][0] == 2.5 - alpha,
    X[3][3] == 2.5 - alpha,
    cp.trace(X) == 15 - 2 * alpha]

# Form and solve the problem
problem = cp.Problem(objective, constraints)
problem.solve()

# Print the result
# print("Optimal value:", problem.value)
# for row in X.value:
#     print(row)
#

# # Using SciPy (if available)
# from scipy.linalg import cholesky
# L = cholesky(X.value, lower=True, check_finite=False)

# print("L:")
# print(L)

# print(L.dot(L.T))
# print(X.value)
A0, A1, A2, B0, B1, B2 = sp.symbols('A0 A1 A2 B0 B1 B2')
x = sp.Matrix([A0, A1, A2, B0, B1, B2])

result = x.T * X.value * x 
simplified_result = sp.simplify(result)
formatted_result  = sp.simplify(str(simplified_result))
print("----------------------------------------------------")
print(formatted_result)
print("----------------------------------------------------\n\n")

L = eigen_decomposition(X.value)
result = x.T * L * L.T * x + sp.Matrix([alpha * (A0*A0 - 2 * A0 * B0 + B0 * B0)])
simplified_result = sp.simplify(result)
formatted_result  = sp.simplify(str(simplified_result))

print("----------------------------------------------------\n\n")
print(formatted_result)
print("----------------------------------------------------\n\n")

L = eigen_decomposition(X.value)
result = x.T * L
simplified_result = sp.simplify(result)
formatted_result  = sp.simplify(str(simplified_result))

print("----------------------------------------------------\n\n")
res = 0
for n in formatted_result:
    res += n ** 2
    print(n)
    
print("----------------------------------------------------\n\n")

print(sp.simplify(str(sp.simplify(res + alpha * (A0*A0 - 2 * A0 * B0 + B0 * B0)))))
# print()
# print(formatted_result)
print("----------------------------------------------------")

# GPA = 4.3 * 12 + 3.44 * 26
# print(GPA/42)


print(recover_exact_form(176/625))
print(176/625)
print(9*(2 ** 0.5) / (25))