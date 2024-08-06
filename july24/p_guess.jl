using Pkg; Pkg.add(url="https://github.com/ewoodhead/QuantumNPA.jl"); using QuantumNPA
using MosekTools
using Printf
using Plots


PA = projector(1, 1:2, 1:3, full=true)
A4 = projector(1, 1:3, 4, full=true)
PB = projector(2, 1:2, 1:3, full=true)
PE = projector(5, 1:3, 1, full=true)

Obj = sum(A4[a, 1] * Id * PE[a, 1] for a in 1:3)
k = 0.5
# Modified Bell Inequality
# Dichotomic variables
A1 = 2 * PA[1, 1] - Id 
A2 = 2 * PA[1, 2] - Id
A3 = 2 * PA[1, 3] - Id
B1 = 2 * PB[1, 1] - Id
B2 = 2 * PB[1, 2] - Id 
B3 = 2 * PB[1, 3] - Id

function score_from_noise(v)
    global A1, A2, A3, B1, B2, B3

    if v == 1
        return 5
    end

    # PC = projector(3, 1:2, 1:3, full=true)
    # PD = projector(4, 1:2, 1:3, full=true)

    # A1 = 2 * (v * PC[1, 1] + (1 - v) * 1/18 * Id) - Id
    # A2 = 2 * (v * PC[1, 2] + (1 - v) * 1/18 * Id) - Id 
    # A3 = 2 * (v * PC[1, 3] + (1 - v) * 1/18 * Id) - Id 
    # B1 = 2 * (v * PD[1, 1] + (1 - v) * 1/18 * Id) - Id 
    # B2 = 2 * (v * PD[1, 2] + (1 - v) * 1/18 * Id) - Id 
    # B3 = 2 * (v * PD[1, 3] + (1 - v) * 1/18 * Id) - Id
    # A1B1 = 
    score = npa_max(2/3 * (v * (A1 * B1 + A2 * B2 + A3 * B3) + (1 - v) * 1/3 * Id) + 
        - 1 * (v * (A1 * B2 + A1 * B3 + A2 * B1 + A2 * B3 + A3 * B1 + A3 * B2)
                    + (1 - v) * (2/3) * Id), 2)
    return score
end


G = 2/3 * (A1 * B1 + A2 * B2 + A3 * B3)  -1 * (A1 * B2 + A1 * B3 + A2 * B1 + A2 * B3 + A3 * B1 + A3 * B2) - k * sum(A4[i, 1] * PB[1, i] for i in 1:3);

# G = 2/3 * sum(4 * (PA[1,i] * PB[1,i]) - 2 * PA[1,i] - 
#                 2 * PB[1,i] + Id for i in 1:3) -1 * ((2 * PA[1,1] - Id) * (2 * PB[1,2] - Id) + 
#                                                     (2 * PA[1,1] - Id) * (2 * PB[1,3] - Id) + 
#                                                     (2 * PA[1,2] - Id) * (2 * PB[1,1] - Id) + 
#                                                     (2 * PA[1,2] - Id) * (2 * PB[1,3] - Id) + 
#                                                     (2 * PA[1,3] - Id) * (2 * PB[1,1] - Id) + 
#                                                     (2 * PA[1,3] - Id) * (2 * PB[1,2] - Id)) - k * sum(A4[i, 1] * PB[1, i] for i in 1:3)


# We need to calculate score as a function of noise.


for v in range(0.80, 1, length=40)
    p_guess = npa_max(Obj, 2, ge=[Obj, G - score_from_noise(v) * Id]);

    randomness = -log2(p_guess)
    println((v, randomness))
end


# In order to calculate Guessing Probability as a function of noise
# We introduce quantum behaviours Pq which results in ideal Bell violation
# and mix it with noise
# which is simply that all combinations are equally possible and therefore,
# random correlation Pr 

# score = (1 - noise) * Pq + noise * Pr

# Pq in CG format