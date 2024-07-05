# Generate formula for the bell expression based on below:

'''
Beta(P_q) = (d + 1)/d * a1111 + (d^2 - 1)/d * a2211 + (d + 1)/d^2 * a1112
            + (2 * (d + 1)^2 (d - 1))/d**2 *a1212 + ((d**2 - 1)(d**2 - d - 1)/d**2)a2212
'''

d = 2

v1 = (d + 1) / d
v2 = (d**2 - 1) / d
v3 = ((d + 1)/d**2)
v4 = (2 * (d + 1)**2 * (d - 1)/d**2)
v5 = (d**2 - 1) * (d**2 - d - 1)/d**2
print(f'{v1}a1 + {v2}a2 + {v3}a3 + {v4}a4 + {(v5)}a5')
