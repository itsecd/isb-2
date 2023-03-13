# тест на одинаковые подряд идущие биты
import sys
import math


sequence = "11110010110111000101111001000101101001101001000100100001001011101011011100111011110110000001000111100110000111111001010010001110"
n = len(sequence)
ratio = 1 / n
sum_elem = 0
for elem in sequence:
    if elem == '1':
        sum_elem += 1
    if elem == '0':
        sum_elem += 0
one = ratio * sum_elem
if (abs(one - 0.5)) < (2 / math.sqrt(n)) == False:
    sys.exit("P = 0")
v = 0
massiv = list(sequence)
for i in range(0, 127):
    if massiv[i] == massiv[i + 1]:
        v += 0
    else:
        v += 1
p = math.erfc(abs(v - 2 * n * one * (1 - one)) /
              (2 * math.sqrt(2 * n) * one * (1 - one)))
print("P =", p)
# P = 0.8618206240105855
