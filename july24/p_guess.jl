# Calculating guessing probability Pg(A1, B1|E) in the CHSH 
# setting using full statistics
using Pkg; Pkg.add(url="https://github.com/ewoodhead/QuantumNPA.jl"); using QuantumNPA
using MosekTools
using Printf
using Plots

score = range(4, 5, length = 10);

PA = projector(1, 1:2, 1:3, full=true)
PB = projector(2, 1:2, 1:3, full=true)
# POVM
PE = projector(5, 1:2, 1:3, full=true)

Obj = sum(PA[a, 1] * Id * PE[a, 1] for a in 1:2)

# projectors
G = 2/3 * sum(4 * (PA[1,i] * PB[1,i]) - 2 * PA[1,i] - 
                2 * PB[1,i] + Id for i in 1:3) -1 * ((2 * PA[1,1] - Id) * (2 * PB[1,2] - Id) + 
                                                    (2 * PA[1,1] - Id) * (2 * PB[1,3] - Id) + 
                                                    (2 * PA[1,2] - Id) * (2 * PB[1,1] - Id) + 
                                                    (2 * PA[1,2] - Id) * (2 * PB[1,3] - Id) + 
                                                    (2 * PA[1,3] - Id) * (2 * PB[1,1] - Id) + 
                                                    (2 * PA[1,3] - Id) * (2 * PB[1,2] - Id));

val = []
for score in range(4.80, 5.00, length=20)
    global  val
    constraints = [
        G - score * Id,
    ]
    p_guess = npa_max(Obj, "2 + A B + A^2 B", eq=constraints, ge=[Obj]);

    randomness = -log2(p_guess)
    println(randomness)
end
# x = range(1, 10, length=10)
# plot(x,val[x])


# # Given values
# values = [0.369662134183343,
#         0.3820192232761561,
#         0.3968635796421249,
#         0.410858255722404,
#         0.4261756428899881,
#         0.44044931044116226,
#         0.45767112712491437,
#         0.4751556446325714,
#         0.49312412530003225,
#         0.5122050566952401,
#         0.5341739186521963,
#         0.5568049619253262,
#         0.581358828119113,
#         0.6081701156512627,
#         0.636474184405917,
#         0.6702727351759552,
#         0.7097234002652323,
#         0.758018590902405,
#         0.8231607631539477,
#         0.9965880928842265]

# # # Generate the range
# x = range(4.80, 5.00, length=20)

# # # Plot the values
# plot(x, values, label="Generated Values", xlabel="Range", ylabel="Values", title="Plot of Generated Values")

# # # Display the plot
# # # display(plot)