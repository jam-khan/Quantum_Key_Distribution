import numpy as np
import math

c = 0
I = np.identity(2)
# e4 = np.matrix([[-1/3], [-math.sqrt(2)/3], [-math.sqrt(2/3)]])

basis = []


def generate_projections(basis):
    
    projections = []
    # projections.append(np.matrix([[3/2, 0], [0, 0]]))
    # projections.append(np.matrix([[-3/4, -3/4], [-3/4, 3/4]]))
    # projections.append(np.matrix([[3/4, 3/4], [3/4, 3/4]]))
    for e in basis:
        projections.append(np.matmul(e, e.H))
    
    return projections

def probability(state, E1, E2):
    
    rho = np.kron(E1, E2)
    return np.matmul(np.matmul(state.H, rho), state)

def generate_box(state, P1, P2):
    Q1 = I - P1
    Q2 = I - P2
    
    results = []
    for Alice in [P1, Q1]:
        for Bob in [P2, Q2]:
            results.append(probability(state, Alice, Bob))
    
    return results

def normalize_vector(vector):
    # Calculate the magnitude of the vector
    magnitude = np.linalg.norm(vector)
    # Divide each component by the magnitude
    return vector / magnitude


def add_perturbation(basis, epsilon):
    
    theta = epsilon * (np.random.rand() - 0.5)
    rotation_matrix = np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta), np.cos(theta)]
    ])
    
    return np.dot(rotation_matrix, basis)

def get_box(perturbation):
    
    # theta = perturbation
    # rotation_matrix = np.array([
    #     [np.cos(theta), -np.sin(theta)],
    #     [np.sin(theta), np.cos(theta)]
    # ])
    
    e1 = normalize_vector(add_perturbation(np.matrix([[1],[0]]), perturbation))
    e2 = normalize_vector(add_perturbation(np.matrix([[1/2], [-(math.sqrt(3))/2]]), perturbation))
    e3 = normalize_vector(add_perturbation(np.matrix([[-1/2], [-math.sqrt(3)/2]]), perturbation))
    

    print(e1)
    print(e2)
    print(e3)
    
    projections = generate_projections([e1, e2, e3])

    ket0 = np.matrix([[1], [0]])
    ket1 = np.matrix([[0], [1]])
    # ket2 = np.matrix([[0], [0], [1]])

    ket00 = np.kron(ket0, ket0)
    ket11 = np.kron(ket1, ket1)
    # ket22 = np.kron(ket2, ket2)

    state = np.dot(ket00 + ket11, 1/math.sqrt(2))

    box = [[0 for i in range(6)] for j in range(6)]
    # print(state)

    for i in range(1, len(projections) + 1):
        for j in range(1, len(projections) + 1):
            A = projections[i - 1]
            B = projections[j - 1]
            results = generate_box(state, A, B)
            
            x = i - 1
            y = j - 1
            
            box[2 * x][2 * y]           = results[0]
            box[2 * x][2 * y + 1]       = results[1]
            box[2 * x + 1][2 * y]       = results[2]
            box[2 * x + 1][2 * y + 1]   = results[3]
    
    return box

box = get_box(0.06)
for row in box:
    for col in row:
        print(f"{col[(0, 0)]:>9.3f}", end=" ")  # Use a single space
    print()

