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
    # Частотный побитовый тест.
    for i in range(len(lisT)):
        if lisT[i] == 0:
            lisT[i] = -1
    print(lisT)
    print(sum(lisT))
    S1 = (-1/math.sqrt(128))*sum(lisT)
    print(S1)
    P1 = math.erfc(S1/math.sqrt(2))
    print(P1) #P1 = 0.1572992070502852
    # Тест на одинаковые подряд идущие биты.
    S2 = (1 / 128) * sum(lisT2)
    print(S2)
    if abs(S2 - 0.5) < 2 / math.sqrt(128):
        print("Go next!")
    else:
        print("Oh no")
    ri = []
    for i in range(len(lisT2) - 1):
        if lisT2[i] == lisT2[i + 1]:
            ri.append(0)
        else:
            ri.append(1)
    print(ri)
    Vn = sum(ri)
    print(Vn)
    P2 = math.erfc((abs(Vn - 2 * 128 * S2 * (1 - S2))) / (2 * math.sqrt(2 * 128) * S2 * (1 - S2)))
    print(P2)  # P2 = 0.4375

