'''
Current problem:
let x1, x2, x3, x4, x5 in (0, 1) and c is classical strategy.

let x = (x1, x2, x3, x4, x5)

f(x) = x1 * S_1 * P(11|11) + x2 * S_2 * P(22|11)
        + x3 * S_3 * P(11|12) + x4 * S_4 * P(12|12)
         + x5 * S_5 * P(22|12)


let f(x) be the quantum bell value.
let g(x, c) be the classical bell value
'''

'''
Objective: maximize f(x) - g(x, c)
            over 0 < x < 1
            
            NS constraint:
            x1 * S_1 * 1/2 + x2 * S_1 * 1/2 
'''