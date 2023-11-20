data = open("data/1.txt").read().split("\n")

sumCalories = []
currentSum = 0
for calories in data:
    if calories == "":
        sumCalories.append(currentSum)
        currentSum = 0
    else:
        currentSum += int(calories)

print(max(sumCalories))
print(sum(sorted(sumCalories)[-3:]))