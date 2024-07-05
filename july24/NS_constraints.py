# Generate the probability distribution
# Assign 1/2 diagonally and get the constraints.


# Goal is to generate all the constraints.

# Equation to generate NS constraints:

'''
B(NS) = (x/2) * a_1111 + (x/2) * a_2211 + (y/2)*a1112 + (d(d + 1) - y)*a_1212 + (y/2)*a2212

0 <= x <= (d + 1)
0 <= y <= d(d + 1)

'''

d = 5
print((d + 1) * (d * (d + 1)))

for x in range(d + 1):
    for y in range(d * (d + 1)):
        result = ""
        if x/2 != 0.0:
            result += f"{x/2} * a1 + {x/2} * a2"
        
        if y / 2 != 0.0:
            if result:
                result += f" + {y/2} * a3 + {y/2} * a4"
            else:
                result = f"{y/2} * a3 + {y/2} * a4"
        if (d*(d + 1) - y) != 0.0:
            if result:
                result += f" + {(d*(d + 1) - y)} * a5"
            else:
                result = f"{(d*(d + 1) - y)} * a5"
                
        result.strip()
        result.strip('+')
        result.strip()
        
        print(f"{result} <= 1,")