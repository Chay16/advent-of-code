data = open("data/6.txt").read().split("\n")[0]

def isMarker(sequence):
    return True if len(set(sequence)) == len(sequence) else False

for i in range(0, len(data)-4):
    if isMarker(data[i:i+4]): 
        print(i+4)
        break

for i in range(0, len(data)-14):
    if isMarker(data[i:i+14]): 
        print(i+14)
        break