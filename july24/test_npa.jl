using Pkg; Pkg.add(url="https://github.com/ewoodhead/QuantumNPA.jl"); using QuantumNPA
using MosekTools
using Printf
using Plots


v = 1
    
# A1 = 2 * (v * PA[1, 1] + (1 - v) * 1/18 * Id) - Id
# A2 = 2 * (v * PA[1, 2] + (1 - v) * 1/18 * Id) - Id 
# A3 = 2 * (v * PA[1, 3] + (1 - v) * 1/18 * Id) - Id 
# B1 = 2 * (v * PB[1, 1] + (1 - v) * 1/18 * Id) - Id 
# B2 = 2 * (v * PB[1, 2] + (1 - v) * 1/18 * Id) - Id 
# B3 = 2 * (v * PB[1, 3] + (1 - v) * 1/18 * Id) - Id
A1 = 2 * PA[1, 1] - Id 
A2 = 2 * PA[1, 2] - Id
A3 = 2 * PA[1, 3] - Id
B1 = 2 * PB[1, 1] - Id
B2 = 2 * PB[1, 2] - Id 
B3 = 2 * PB[1, 3] - Id

npa_max(2/3 * (v * (A1 * B1 + A2 * B2 + A3 * B3) + (1 - v) * 1/3 * Id) + 
        - 1 * (v * (A1 * B2 + A1 * B3 + A2 * B1 + A2 * B3 + A3 * B1 + A3 * B2)
                    + (1 - v) * (2/3) * Id), 2)
    
#     return score 
# end
