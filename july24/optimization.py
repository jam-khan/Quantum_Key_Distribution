import cvxpy as cp

d = 2

def find_strats():
    
    n = d + 1
    strats = []
    for i in range(n + 1):
        val = [1 for j in range(i)]
        val += [0 for j in range(n - i)]
        
        strats.append(val)
    
    return strats
# def find_strats(x, n):
#     if n == 0:
#         return x
    
#     new = []
#     for partial_strat in x:
#         new.append(partial_strat + [0])
#         new.append(partial_strat + [1])
    
#     if not new:
#         new = [[0], [1]]
    
#     return find_strats(new, n - 1)

def classical_strats():
    
    # Alice = find_strats([], d + 1)
    # Bob   = find_strats([], d + 1)
    
    
    Alice = find_strats()
    Bob   = find_strats()
    
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
        
    return S_1111, S_2211, S_1112, S_1212, S_2212


def optimize():
    
    results = []
    
    strats = classical_strats()
    
    for A, B in strats:
        
        S_1, S_2, S_3, S_4, S_5 = generate_classical_expression(A, B)
        
        a1 = cp.Variable()
        a2 = cp.Variable()
        a3 = cp.Variable()
        a4 = cp.Variable()
        a5 = cp.Variable()
        
        v1 = (d + 1)/d 
        v2 = (d ** 2 - 1)/d
        v3 = (d + 1)/d**2
        v4 = (2 * (d + 1)**2 * (d - 1))/d**2
        v5 = ((d**2 - 1) * (d**2 - d - 1))/d**2
        
        constraints = [a1 >=0, a2 >= 0, a3 >= 0, a4 >= 0, a5 >= 0,
                        v1*a1 + v2*a2 + v3*a3 + v4*a4 + v5*a5 <= 1,
                        # S_1*a1 + S_2*a2 + S_3*a3 + S_4*a4 + S_5*a5 >= 2.70,
                        # S_1*a1 + S_2*a2 + S_3*a3 + S_4*a4 + S_5*a5 <= 2.77,
                        # (v1 * a1 + v2 * a2 + v3 * a3 + v4 * a4 + v5 * a5) - (S_1*a1 + S_2*a2 + S_3*a3 + S_4*a4 + S_5*a5) >= 0
                        ]
        
        for x in range(d + 1):
            for y in range(d * (d + 1)):
                # if x == d - 1 and y == d - 1:
                #     constraints.append(x/2 * a1 + x/2 * a2 + y/2 * a3 + (d*(d + 1) - y) * a4 + y/2 * a5 == 1)
                # else:
                    constraints.append(x/2 * a1 + x/2 * a2 + y/2 * a3 + (d*(d + 1) - y) * a4 + y/2 * a5 <= 1)
        print(v1, v2, v3, v4, v5)
        print(S_1, S_2, S_3, S_4, S_5)
        # obj  = cp.Maximize((v1 * a1 + v2 * a2 + v3 * a3 + v4 * a4 + v5 * a5) - (S_1*a1 + S_2*a2 + S_3*a3 + S_4*a4 + S_5*a5))
        
        obj  = cp.Minimize((S_1*a1 + S_2*a2 + S_3*a3 + S_4*a4 + S_5*a5))
        prob = cp.Problem(obj, constraints)
        
        
        
        prob.solve()
        
        print([A, B, prob.value, prob.status, (a1.value, a2.value, a3.value, a4.value, a5.value)])
        
    for result in results:
        print(result)
        
optimize()