from math import sqrt
from scipy.special import erfc


def main():
    bits = '01111111111001001001101110110101010010110111001001000011100001100000001101111001110101100111110101111001100111110101100010110111'
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
    #0.8946367310768166 -> последовательность случайна 
    if (P < 0.01):
        print("Failed  test")
    else:
        print( "Passed  test")

if __name__ == "__main__":
    main()
