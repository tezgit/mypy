import random
list = []
n = 0
while (n < 7):
    for i in range(7):
        r = random.randint(1, 7)
        if r not in list:
            list.append(r)
            n += 1

print(list)
