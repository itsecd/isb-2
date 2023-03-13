import math

from info import sequence, N


z = (1/N)*sum(sequence)
print(z)
# 0.6015625
e1 = z - 0.5
print(e1)
# 0.1015625
e2 = 2/math.sqrt(N)
print(e2)
# 0.17677669529663687
if e1 < e2:
    count = 0
    for i in range(len(sequence)-1):
        if(sequence[i]!=sequence[i+1]):
            count += 1
    count += 1
    print(count) 
    #62
    num = count-(2*N*z*(1-z))
    if num < 0:
        num *= -1
    denum = 2*math.sqrt(2*N)*z*(1-z)
    P = math.erfc(num/denum)
else: 
    P = 0
print(P)
# 0.9059716064924803
# последвоательность случайна
