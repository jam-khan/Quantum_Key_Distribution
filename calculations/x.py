import numpy as np
from scipy.linalg import norm, qr, svd

# Local dimension
d = 2

# Find the unitary
allone = np.array(np.ones(d + 1)) / norm(np.ones(d + 1))
unitary = np.zeros((d + 1, d + 1))
unitary[0] = allone
unitary[1:] = np.array([np.eye(d + 1)[i] for i in range(1, d + 1)]).T
_, unitary, _ = qr(unitary)
print("Unitary matrix:")
print(unitary)

# d+1 vectors
def vect(x):
    return (np.dot(unitary, (np.eye(d + 1)[x] - np.dot(allone, np.eye(d + 1)[x])) / norm(np.eye(d + 1)[x] - np.dot(allone, np.eye(d + 1)[x]))))[1:]

# d+1 projections
def proj(x):
    v = vect(x)
    return np.outer(v, v)

print("Projection for x=0:")
print(proj(0))

# d+1 binary observables
def obs(x):
    return 2 * proj(x) - np.eye(d)

print("Observable for x=0:")
print(obs(0))

def jordanproduct(x, y):
    return (np.dot(x, y) + np.dot(y, x)) / 2

def sgn(x):
    u, s, v = svd(x)
    return np.dot(u, np.dot(np.diag(np.sign(s)), v))

def obs2(x, y):
    return sgn(obs(x) + obs(y))

print("obs2(0, 1):")
print(obs2(0, 1))

# Alternative O_{jk} operator
# def obs2(x, y):
#     return d / (d + 1) * np.outer(vect(x) - vect(y), vect(x) - vect(y))

