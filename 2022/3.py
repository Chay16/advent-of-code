data = open("data/3.txt").read().split("\n")[:-1]

import string

def getCompartiments(items):
    return items[:len(items)//2], items[len(items)//2:]

def intersection2Compartiments(c1, c2):
    return list(set(c1).intersection(c2))


PRIORITIES = {k:i+1 for i, k in enumerate(string.ascii_letters)}

answer1 = 0
for d in data:
    c1, c2 = getCompartiments(d)
    answer1 += PRIORITIES[intersection2Compartiments(c1, c2)[0]]
print(answer1)

answer2 = 0
for i in range(0, len(data)-2, 3):
    answer2 += PRIORITIES[intersection2Compartiments(data[i], intersection2Compartiments(data[i+1], data[i+2]))[0]]
print(answer2)
