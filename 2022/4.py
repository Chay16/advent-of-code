data = open("data/4.txt").read().split("\n")[:-1]

def getSections(input):
    s1, s2 = input.split(",")
    return [int(s1.split("-")[0]), int(s1.split("-")[1])], [int(s2.split("-")[0]), int(s2.split("-")[1])]

def contains(s1, s2):
    if s1[0] >= s2[0] and s1[1] <= s2[1]:
        return True
    elif s2[0] >= s1[0] and s2[1] <= s1[1]:
        return True
    else:
        return False

def overlaps(s1, s2):
    if s1[0] <= s2[1] and s1[0] >= s2[0]:
        return True
    elif s2[0] <= s1[1] and s2[0] >= s1[0]:
        return True
    else:
        return False

contained = 0
overlaped = 0
for d in data:
    s1, s2 = getSections(d)
    if contains(s1, s2): contained += 1
    if overlaps(s1, s2): overlaped += 1
print(contained)
print(overlaped)