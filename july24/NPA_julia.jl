using Pkg; Pkg.add(url="https://github.com/ewoodhead/QuantumNPA.jl"); using QuantumNPA

@dichotomic A1 A2 B1 B2;

S = A1 * (B1 + B2) + A2*(B1 - B2);

# Maximizing CHSH at level 2 of the hierarchy
npa_max(S, 2)


# Maximizing the Svetlichny at level 1 + A B + A C + B C 
@dichotomic A[1: 2] B[1: 2] C[1: 2];

E(x, y, z) = A[x] * B[y] * C[z];

S = -E(1,1,1) + E(1,1,2) + E(1,2,1) + E(1,2,2) + E(2,1,1) + E(2,1,2) + E(2,2,1) - E(2,2,2);

npa_max(S, "1 + A B + A C + B C")

# Maximizing a modified CHSH at level 1 + A B + A^2 B
npa_max(0.3 * A1 + 0.6 * A1*(B1 + B2) + A2*(B1 - B2), "1 + A B + A^2 B")

# Specifying equality and inequality arguments using
# eq and ge keyword arguments
# <A1 * (B1 + B2)> = 1.4
# and
# <A2*(B1 - B2)> = 1.4

npa_max(A1, 2, eq=[A1*(B1 + B2) - 1.4*Id, A2*(B1 - B2) - 1.4*Id])

# Maximize <A1 + A2>
# subject to
#           <A1 + 2*A2> <= 1
#           <2*A1 + A2> <= 1

npa_max(A1 + A2, 1, ge=[Id - A1 - 2*A2, Id - 2*A1 - A2])

# Maximize <A1 + A2>
# subject to
#           <A1> = <A2>
#           <A1 + 2*A2> <= 1

npa_max(A1 + A2, 1, eq=[A1 - A2], ge=[Id - A1 - 2*A2])

# Using projectors

PA11, PA12 = projector(1,1,1:2);
PB11, PB12 = projector(2,1,1:2);

npa_max(-PA11 - PB11 + PA11 * (PB11 + PB12) + PA12 * (PB11 - PB12), 1)

# Maximize CGLMP with d=3 at level 1 + A B

npa_max(cglmp(3), "1 + A B")


