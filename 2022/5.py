data = open("data/5.txt").read().split("\n")

from copy import deepcopy

stacks = {
    1: ["D","T","R","B","J","L","W","G"],
    2: ["S","W","C"],
    3: ["R","Z","T","M"],
    4: ["D","T","C","H","S","P","V"],
    5: ["G","P","T","L","D","Z"],
    6: ["F","B","R","Z","J","Q","C","D"],
    7: ["S","B","D","J","M","F","T","R"],
    8: ["L","H","R","B","T","V","M"],
    9: ["Q","P","D","S","V"]
}

def parseMovement(string):
    N = int(string.split(" ")[1])
    originStack = int(string.split(" ")[3])
    destStack = int(string.split(" ")[5])
    return N, originStack, destStack

def CrateMover_9000(stacks, N, originStack, destStack):
    for i in range(N):
        stacks[destStack].append(stacks[originStack][-1])
        stacks[originStack].pop()
    return stacks

def CrateMover_9001(stacks, N, originStack, destStack):
    kept, move = stacks[originStack][:len(stacks[originStack])-N], stacks[originStack][-1*N:]
    stacks[destStack] += move
    stacks[originStack] = kept
    return stacks

def answer(stacks):
    return "".join([v[-1] for v in stacks.values()])


stacks1 = deepcopy(stacks)
stacks2 = deepcopy(stacks)
for d in data[10:-1]:
    N, originStack, destStack = parseMovement(d)
    stacks1 = CrateMover_9000(stacks1, N, originStack, destStack)
    stacks2 = CrateMover_9001(stacks2, N, originStack, destStack)

print(answer(stacks1))
print(answer(stacks2))