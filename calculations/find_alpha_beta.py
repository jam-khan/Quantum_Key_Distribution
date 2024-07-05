
S12 = [(1,1,1,1), (2,2,1,1), (1,1,2,2), (2,2,2,2), (1,1,3,3), (2,2,3,3)]
S38 = [(1,2,1,2), (2,1,1,2), (1,2,1,3), (2,1,1,3), (1,2,2,1), (2,1,2,1), (1,2,2,3), (2,1,2,3), (1,2,3,1), (2,1,3,1), (1,2,3,2), (2,1,3,2)]


def find_strats(x, n):
    if n == 0:
        return x
    
    new = []
    for partial_strat in x:
        new.append(partial_strat + [1])
        new.append(partial_strat + [2])
    
    if not new:
        new = [[1], [2]]
    
    return find_strats(new, n - 1)

strats = find_strats([], 6)

unique = set()
alpha_beta_pairs = set()
for strat in strats:
    alice_strat = strat[:3]
    bob_strat   = strat[3:]
    
    alpha = 0
    beta  = 0
    for X in [1, 2, 3]:
        for Y in [1, 2, 3]:
            alice_ans   = alice_strat[X - 1]
            bob_ans     = bob_strat[Y - 1]
            if (alice_ans, bob_ans, X, Y) in S12:
                alpha += 1
            if (alice_ans, bob_ans, X, Y) in S38:
                beta += 1
    
    if (alpha, beta) == (3, 4):
        print(alice_strat, bob_strat)

    alpha_beta_pairs.add((alpha, beta))

print("Possible (alpha, beta) pairs: ", list(alpha_beta_pairs))

# Below calculates maximal classical values for each (alpha_i, beta_i)

maxgamma = 0
gamma = 0.01

while gamma < 0.3333333:
    
    quantum = 3/4 * gamma + 3/4
    
    maxi = 0
    best_strat = None
    for alpha, beta in alpha_beta_pairs:
        prob = alpha * gamma + ((1 - 3 * gamma)/6) * beta
        if prob > maxi and quantum - prob > 0:
            maxi = prob
            best_strat = (alpha, beta)
    
    print(f"best strat for gamma = {gamma}: {best_strat}")

    gamma += 0.001


        
    
    # print(f"Prob for ({alpha}, {beta}) is {maxi} with gamma = {maxgamma}, diff = {maxdiff}")
