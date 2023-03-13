# частотный побитовый тест
import math


sequence = "11110010110111000101111001000101101001101001000100100001001011101011011100111011110110000001000111100110000111111001010010001110"
n = len(sequence)
ratio = (1 / math.sqrt(n))
sum_elem = 0
for elem in sequence:
    if elem == '1':
        sum_elem += 1
    if elem == '0':
        sum_elem += -1
s_n = ratio * sum_elem
p = math.erfc(s_n / math.sqrt(2))
print("P =", p)
# P = 0.8596837951986662
