import numpy as np
import scipy.linalg as la
import math
d = 2

def create_unitary(v):
    return np.hstack((v,la.null_space(v.T))).transpose()

a = np.matrix([[1/math.sqrt(d)] for i in range(0, d)])
U = create_unitary(a)


ej = np.matrix([[0] for i in range(1, d + 1)])
# Now, we will apply U to d + 1 vectors {f_j}
fj = ej - (np.inner(ej, a)) * a
# fj = (1/np.linalg.norm(fj1)) * fj1

Ufj = np.matmul(U, fj)

vj = Ufj
print(vj)
Px = np.matmul(vj, vj.H)
print(Px)

for j in range(1, d + 1):
    # ej = None
    ej = np.matrix([[0] if i != j else [1] for i in range(1, d + 1)])

    fj1 = ej - (np.inner(ej, a)) * a
    fj = (1/np.linalg.norm(fj1)) * fj1
    
    Ufj = np.matmul(U, fj)
    
    vj = Ufj
    print(vj)
    Px = np.matmul(vj, vj.H)
    print(Px)



# print(np.absolute(np.matmul(U, U.H).round()))
# print(np.absolute(np.matmul(U.H, U).round()))