#тест на самую длинную последовательность единиц в блоке
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
    for elem in mas[i]:
        if elem == '1':
            count += 1
        if elem == '0':
            if maximum < count:
                maximum = count
            count = 0
    max_value.append(maximum)
print(max_value)
    

