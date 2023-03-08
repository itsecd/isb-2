from math import sqrt
from scipy.special import erfc


def main():
    bits = '00000000000000000000000000000000000000000000000000000000000000000000000111000010011010110000111110010111000100100110100011100011'
    # вычисляем количество единиц и нулей в последовательности
    f1 = bits.count('1') /128
    zeros = bits.count('0') 
    runs = [bits[0]]
    for i in range (1,128):
        if bits[i] != bits[i-1]:
            runs.append(bits[i])
    num = len(runs)
    # вычисляем Вероятность
    P = erfc( abs(num-2*128*f1*(1-f1))/(2*sqrt(2*128)*f1*(1-f1)) )
    # проверяем гипотезу на уровне значимости 0.01
    print(P)
    #4.64243718410548e-05 -> последовательность случайна 

if __name__ == "__main__":
    main()
