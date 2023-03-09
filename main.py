import math
with open("GPSHC.txt", mode='r', encoding='UTF-8') as text:
    reader = text.read()
    new_dict2 = {}
    lisT = []
    lisT2 = []
    z = 1
    x = 0
    count = 0
    for i in reader:
        new_dict2[z] = reader[count:count + 8]
        lisT.append(i)
        lisT2.append(i)
        x += 1
        if x == 8:
            z += 1
            count += 8
            x = 0
    print(new_dict2)
    print(lisT)
    lisT = list(map(int, lisT))
    lisT2 = list(map(int, lisT))
    print(lisT2)