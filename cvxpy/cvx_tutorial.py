import cvxpy as cp




# Formula to Solve:
# 1. Iterate through all unique classical strategies
#   Classical strategy i
#   1. maximize B(p_q) - B(p_c) over alpha constraints.
#   2. Get alpha values and gap value
# 2. Repeat for all classical strategies
# 3. Take the classical strategy with min {max gap value}


# Create two scalar optimization variables

# x = cp.Variable()
# y = cp.Variable()

# # Create two constraints.
# constraints = [ x + y == 1,
#                 x - y >= 1]


# # # Form objective.
# obj = cp.Minimize((x - y)**2)

# # Form and solve problem.
# prob = cp.Problem(obj, constraints)
# prob.solve() # Returns the optimal value.
# # print("status:", prob.status)
# # print("optimal value", prob.value)
# # print("optimal var", x.value, y.value)

# # Replace the objective
# prob2 = cp.Problem(cp.Maximize(x + y), prob.constraints)
# print("optimal value", prob2.solve())

# # Replace the constraint (x + y == 1).
# constraints = [x + y <= 3] + prob2.constraints[1:]
# prob3       = cp.Problem(prob2.objective, constraints)
# print("optimal value", prob3.solve()) 

'''

Equation to maximize:
3/2 a1 + 3/2 a2 + 3/4 a3 + 9/2 a4 + 3/4 a5
constraints:

6a5 <= 1
0.5a3 + 0.5a4 + 5a5 <= 1
1.0a3 + 1.0a4 + 4a5 <= 1
1.5a3 + 1.5a4 + 3a5 <= 1
2.0a3 + 2.0a4 + 2a5 <= 1
2.5a3 + 2.5a4 + 1a5 <= 1
0.5a1 + 0.5a2 + 6a5 <= 1
0.5a1 + 0.5a2 + 0.5a3 + 0.5a4 + 5a5 <= 1
0.5a1 + 0.5a2 + 1.0a3 + 1.0a4 + 4a5 <= 1
0.5a1 + 0.5a2 + 1.5a3 + 1.5a4 + 3a5 <= 1
0.5a1 + 0.5a2 + 2.0a3 + 2.0a4 + 2a5 <= 1
0.5a1 + 0.5a2 + 2.5a3 + 2.5a4 + 1a5 <= 1
1.0a1 + 1.0a2 + 6a5 <= 1
1.0a1 + 1.0a2 + 0.5a3 + 0.5a4 + 5a5 <= 1
1.0a1 + 1.0a2 + 1.0a3 + 1.0a4 + 4a5 <= 1
1.0a1 + 1.0a2 + 1.5a3 + 1.5a4 + 3a5 <= 1
1.0a1 + 1.0a2 + 2.0a3 + 2.0a4 + 2a5 <= 1
1.0a1 + 1.0a2 + 2.5a3 + 2.5a4 + 1a5 <= 1

Equation to maximize:

'''

a1 = cp.Variable()
a2 = cp.Variable()
a3 = cp.Variable()
a4 = cp.Variable()
a5 = cp.Variable()

constraints = [a1 >=0, a2 >= 0, a3 >= 0, a4 >= 0, a5 >= 0,
                6*a5 <= 1,
                1.5*a1 + 1.5*a2 + 0.75*a3 + 4.5*a4 + 0.75*a5 <= 1,
                0.5*a3 + 0.5*a4 + 5*a5 <= 1,
                1.0*a3 + 1.0*a4 + 4*a5 <= 1,
                1.5*a3 + 1.5*a4 + 3*a5 <= 1,
                2.0*a3 + 2.0*a4 + 2*a5 <= 1,
                2.5*a3 + 2.5*a4 + 1*a5 <= 1,
                0.5*a1 + 0.5*a2 + 6*a5 <= 1,
                0.5*a1 + 0.5*a2 + 0.5*a3 + 0.5*a4 + 5*a5 == 1,
                0.5*a1 + 0.5*a2 + 1.0*a3 + 1.0*a4 + 4*a5 <= 1,
                0.5*a1 + 0.5*a2 + 1.5*a3 + 1.5*a4 + 3*a5 <= 1,
                0.5*a1 + 0.5*a2 + 2.0*a3 + 2.0*a4 + 2*a5 <= 1,
                0.5*a1 + 0.5*a2 + 2.5*a3 + 2.5*a4 + 1*a5 <= 1,
                1.0*a1 + 1.0*a2 + 6*a5 <= 1,
                1.0*a1 + 1.0*a2 + 0.5*a3 + 0.5*a4 + 5*a5 <= 1,
                1.0*a1 + 1.0*a2 + 1.0*a3 + 1.0*a4 + 4*a5 <= 1,
                1.0*a1 + 1.0*a2 + 1.5*a3 + 1.5*a4 + 3*a5 <= 1,
                1.0*a1 + 1.0*a2 + 2.0*a3 + 2.0*a4 + 2*a5 <= 1,
                1.0*a1 + 1.0*a2 + 2.5*a3 + 2.5*a4 + 1*a5 <= 1]

obj = cp.Maximize(1.5*a1 + 1.5*a2 + 0.75*a3 + 4.5*a4 + 0.75*a5)
prob = cp.Problem(obj, constraints)

prob.solve()
print("status:", prob.status)
print("optimal value", prob.value)
print("optimal var", a1.value, a2.value, a3.value, a4.value, a5.value)


