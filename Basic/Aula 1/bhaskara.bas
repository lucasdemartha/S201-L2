10 INPUT "VALOR A"; A
20 INPUT "VALOR B"; B
30 INPUT "VALOR C"; C
40 LET L = INT (A)
50 LET M = INT (B)
60 LET N = INT (C)
70 LET D = 0
80 LET X1 = 0
90 LET X2 = 0
100 D = (M*M)-(4*L*N)
110 X1 = ((-M)+SQR(D))/(2*L)
120 X2 = ((-M)-SQR (D))/(2*L)
130 PRINT X1
140 PRINT X2