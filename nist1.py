from math import sqrt
from scipy.special import erfc


def main():
    bits = '01111111111001001001101110110101010010110111001001000011100001100000001101111001110101100111110101111001100111110101100010110111'
    # вычисляем количество единиц и нулей в последовательности
    ones = bits.count('1')
    zeros = bits.count('0')
    summ = ones+zeros*(-1)
    # вычисляем значение статистики теста
    S = summ/sqrt(128)
    # вычисляем Вероятность
    P = erfc(S / sqrt(2))
    # проверяем гипотезу на уровне значимости 0.01
    print(P)
    if (P < 0.01):
        print("Failed  test")
    else:
        print( "Passed  test")
#0.11161176829829224
#passed test
if __name__ == "__main__":
    main()
