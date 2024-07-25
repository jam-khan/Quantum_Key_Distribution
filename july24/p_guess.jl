using Pkg; Pkg.add(url="https://github.com/ewoodhead/QuantumNPA.jl"); using QuantumNPA
using MosekTools
using Printf
using Plots

score = range(4, 5, length = 10);

PA = projector(1, 1:2, 1:3, full=true)
A4 = projector(1, 1:3, 4, full=true)
PB = projector(2, 1:2, 1:3, full=true)
PE = projector(5, 1:3, 1, full=true)

Obj = sum(A4[a, 1] * Id * PE[a, 1] for a in 1:3)
k = 1
# projectors
G = 2/3 * sum(4 * (PA[1,i] * PB[1,i]) - 2 * PA[1,i] - 
                2 * PB[1,i] + Id for i in 1:3) -1 * ((2 * PA[1,1] - Id) * (2 * PB[1,2] - Id) + 
                                                    (2 * PA[1,1] - Id) * (2 * PB[1,3] - Id) + 
                                                    (2 * PA[1,2] - Id) * (2 * PB[1,1] - Id) + 
                                                    (2 * PA[1,2] - Id) * (2 * PB[1,3] - Id) + 
                                                    (2 * PA[1,3] - Id) * (2 * PB[1,1] - Id) + 
                                                    (2 * PA[1,3] - Id) * (2 * PB[1,2] - Id)) - k * sum(A4[i, 1] * PB[1, i] for i in 1:3)

val = []
for score in range(4.01, 5.00, length=40)
    # score = 4.05
    global  val
    p_guess = npa_max(Obj, 2, ge=[Obj, G - score * Id]);

    randomness = -log2(p_guess)
    println((score, randomness))
end