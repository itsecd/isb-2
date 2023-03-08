from math import sqrt
from scipy.special import erfc


def main():
    bits = 1
    # вычисляем количество единиц и нулей в последовательности


    P = erfc(S / sqrt(2))
    # проверяем гипотезу на уровне значимости 0.01
    if P < 0.01:
        return "Failed  test"
    else:
        return "Passed  test"


if __name__ == "__main__":
    main()
