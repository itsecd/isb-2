import math
import scipy
from scipy.special import gammaincc


def main():
    bits = '00000000000000000000000000000000000000000000000000000000000000000000000111000010011010110000111110010111000100100110100011100011'

    num_blocks = 128 // 8
    mas_count = []
    for i in range(16):
        block = bits[i * 8: (i + 1) * 8]
        one = 0
        max_one_in_block = 0
        max_run = 0
        for bit in block:
            if bit == '1':
                one += 1
                max_one_in_block = max(max_one_in_block, one)
            else:
                one = 0
        max_run = max(max_run, max_one_in_block)
        mas_count.append(max_run)
    print(mas_count)
    v1 = sum(x <= 1 for x in mas_count)
    v2 = sum(x == 2 for x in mas_count)
    v3 = sum(x == 3 for x in mas_count)
    v4 = sum(x > 4 for x in mas_count)
    k0 = 0.2148
    k1 = 0.3672
    k2 = 0.2305
    k3 = 0.1875
    X = ((v1-16*k0)**2)/(16*k0)+((v2-16*k1)**2)/(16*k1) + \
        ((v3-16*k2)**2)/(16*k2)+((v4-16*k3)**2)/(16*k3)
    P=gammaincc(3/2,X/2)
    print(P)
    #0.0005039782007990067
    
    
if __name__ == "__main__":
    main()
