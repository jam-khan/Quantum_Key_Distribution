M = [0, 0, 0, 0;
    0, 2/3, -1, -1;
    0, -1, 2/3, -1;
    0, -1, -1, 2/3];

desc = [2 2 3 3];
cla = BellInequalityMax(M, desc, 'fc', 'classical')
Q   = BellInequalityMax(M, desc, 'fc', 'quantum', '1 + AP')
NS  = BellInequalityMax(M, desc, 'fc', 'nosignal')
