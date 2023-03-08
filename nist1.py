from math import sqrt
from scipy.special import erfc


def main():
    bits = '00000000000000000000000000000000000000000000000000000000000000000000000111000010011010110000111110010111000100100110100011100011'
    # вычисляем количество единиц и нулей в последовательности
    ones = bits.count('1')
    zeros = bits.count('0')
    summ = ones+zeros*(-1)
    # вычисляем значение статистики теста
    S = summ/sqrt(128)
    # вычисляем Вероятность
    P = erfc(S / sqrt(2))
    # проверяем гипотезу на уровне значимости 0.01
    if P < 0.01:
        print("Failed  test")
    else:
        print( "Passed  test")

#passed test
if __name__ == "__main__":
    main()
