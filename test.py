w = ['cubes-2.0', 'love', 'кубики', 'boxgame']
w1 = ['bub', 'Кубики Правые', 'boxgame-2.0']
for i in w:
    i = i.lower()
    for j in w1:
        j = j.lower()
        if i in j:
            print(1, i, j)
        else:
            print(2, i, j)
