# тест на самую длинную последовательность единиц в блоке
import scipy


sequence = "11110010110111000101111001000101101001101001000100100001001011101011011100111011110110000001000111100110000111111001010010001110"
n = len(sequence)
mas = [0] * 16
for i in range(16):
    mas[i] = [0] * 8
count = 0
for i in range(16):
    for j in range(8):
        mas[i][j] = sequence[count]
        j += 1
        count += 1
    i += 1
max_value = []
for i in range(16):
    maximum = 0
    count = 0
    for j in range(8):
        if mas[i][j] == '1' and j != 7:
            count += 1
        elif mas[i][j] == '1' and j == 7:
            count += 1
            if maximum < count:
                maximum = count
        elif mas[i][j] == '0':
            if maximum < count:
                maximum = count
            count = 0
    max_value.append(maximum)
list_v = [0, 0, 0, 0]
for elem in max_value:
    if elem <= 1:
        list_v[0] += 1
    if elem == 2:
        list_v[1] += 1
    if elem == 3:
        list_v[2] += 1
    if elem >= 4:
        list_v[3] += 1
hi = 0
pi = [0.2148, 0.3672, 0.2305, 0.1875]
i = 0
for elem in list_v:
    hi += (((elem - 16 * pi[i]) ** 2) / (16 * pi[i]))
    i += 1
p = scipy.special.gammaincc(3 / 2, hi / 2)
print(p)
# P = 0.19377917400603764
