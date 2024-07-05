# This involves optimization of Maximal Violation of Bell Expression for a specific d.

# Goal:
#   Find classical strategies that maximize violation
#   for a specific pair of (a_1, a_2, a_3, a_4, a_5)
#   Find general pattern and then, find potential strategies.

# First find the probability distributions for classical

d = 2
# For d = 3, we have d + 1 questions with 2 answers each

def find_strats(x, n):
    if n == 0:
        return x
    
    new = []
    for partial_strat in x:
        new.append(partial_strat + [0])
        new.append(partial_strat + [1])
    
    if not new:
        new = [[0], [1]]
    
    return find_strats(new, n - 1)

def classical_strats():
    
    Alice = find_strats([], d + 1)
    Bob   = find_strats([], d + 1)
    # This will generate all possible classical strats
    
    strats = []
    for A in Alice:
        for B in Bob:
            strats.append([A, B])
    
    return strats

def generate_classical_expression(A, B):
    n = d + 1
    Alice = A
    Bob   = B
    
    if d == 0: return []
    
    S_1111 = S_2211 = S_1112 = S_2212 = S_1212 = 0
    
    for i in range(2 * n):
        for j in range(2 * n):
            x = i // d
            y = j // d
            a = i % 2
            b = j % 2
            
            if Alice[x] == a and Bob[y] == b:
                S_1111 += 1 if x == y and a == b == 0 else 0
                S_2211 += 1 if x == y and a == b == 1 else 0
                S_1112 += 1 if x != y and a == b == 0 else 0
                S_2212 += 1 if x != y and a == b == 1 else 0
                S_1212 += 1 if x != y and a != b else 0
        #         print(1, end=' ')
        #     else:
        #         print(0, end=' ')
        # print()
        
    return S_1111, S_2211, S_1112, S_1212, S_2212

def quantum_expression():
    
    S_1111 = (d + 1) / d
    S_2211 = (d**2 - 1) / (d**2)
    S_1112 = (d + 1) / (d**2)
    S_1212 = (2 * (d + 1)**2 * (d - 1)) / d**2 
    S_2212 = ((d**2 - 1) * (d**2 - d - 1)) / d**2
    
    return S_1111, S_2211, S_1112, S_1212, S_2212

    
    

def B_q(a_1, a_2, a_3, a_4, a_5):
    
    S_1111, S_2211, S_1112, S_1212, S_2212 = quantum_expression()
    
    return a_1 * S_1111 + a_2 * S_2211 + a_3 * S_1112 + a_4 * S_1212 + a_5 * S_2212

def B_c(A, B, a_1, a_2, a_3, a_4, a_5):
    
    S_1111, S_2211, S_1112, S_1212, S_2212 = generate_classical_expression(A, B)
    
    return a_1 * S_1111 + a_2 * S_2211 + a_3 * S_1112 + a_4 * S_1212 + a_5 * S_2212


def unique_local():
    
    strats = classical_strats()
    
    possible = set()
    for A, B in strats:
        S_1111, S_2211, S_1112, S_1212, S_2212 = generate_classical_expression(A, B)
        if (S_1111, S_2211, S_1112, S_1212, S_2212) == (0, 3, 0, 0, 6):
            print(A, B)
            
        possible.add((S_1111, S_2211, S_1112, S_1212, S_2212))
    
    return list(possible)
        
def find_maximal_classical_violation():
    
    unique_vals = unique_non_local()
    
    max_Bpc = 0
    best_coefficients = None
    best_strats = None
    
    for S_1111, S_2211, S_1112, S_1212, S_2212 in unique_vals:
        
        a1 = a2 = a3 = a4 = a5 = 0.01
        
        while a1 < 1.0:
            while a2 < 1.0:
                while a3 < 1.0:
                    while a4 < 1.0:
                        while a5 < 1.0:
                            # if int(a1 * (d + 1) + a2 * (d + 1) + a3 * d * (d + 1) + a4 * 2 * d * (d + 1) + S_2212 * d * (d + 1) + 0.03) == 1:
                            val = a1 * S_1111 + a2 * S_2211 + a3 * S_1112 + a4 * S_1212 + a5 * S_2212
                            
                            if val > max_Bpc:
                                max_Bpc = val
                                best_coefficients = (a1, a2, a3, a4, a5)
                                best_strats = (S_1111, S_2211, S_1112, S_1212, S_2212)
                            a5 += 0.01
                        a4 += 0.01
                    a3 += 0.01
                a2 += 0.01
            a1 += 0.01
    print(max_Bpc)
    print(best_coefficients)
    print(best_strats)
    
find_maximal_classical_violation()                   

# def bell_violation():
    
#     a1 = a2 = a3 = a4 = a5 = 0.01
    
#     strats = classical_strats() 
#     best_pairs = None
#     max_val = float('-inf')
    
#     a1 = 0
#     while a1 < 1.0:
#         a2 = 0
#         while a2 < 1.0:
#             a3 = 0
#             while a3 < 1.0:
#                 a4 = 0
#                 while a4 < 1.0:
#                     a5 = 0
#                     while a5 < 1.0:
#                         if 0.98 < abs((d + 1) * a1 + \
#                             (d + 1) * a2 + \
#                                 d * (d + 1) * a3 + \
#                                     2 * d * (d + 1) * a4 + \
#                                         d * (d + 1) * a5) < 1.02:
#                             mini = float('inf')
#                             best_strat = None
#                             for A, B in strats:
#                                 val = B_q(a1, a2, a3, a4, a5) - B_c(A, B, a1, a2, a3, a4, a5) 
#                                 if val < mini and val > 0:
#                                     best_strat = [A, B]
#                                     mini = val
#                             print(best_strat, mini)
#                             if max_val < mini:
#                                 max_val = mini 
#                                 best_pairs = (a1, a2, a3, a4, a5)                
#                         a5 += 0.02
#                     a4 += 0.02
#                 a3 += 0.02
#             a2 += 0.02
#         a1 += 0.02

#     print(max_val, best_pairs)
# bell_violation()
                            
    
    



