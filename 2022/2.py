data = open("data/2.txt").read().split("\n")

opponentPlay = {
    "A": "rock",
    "B": "paper",
    "C": "scissors"
}

strategy1Play = {
    "X": "rock",
    "Y": "paper",
    "Z": "scissors"
}

strategy2Play = {
    "X": "loss",
    "Y": "draw",
    "Z": "win"
}

game = {
    "rock": {
        "win": "scissors",
        "loss": "paper"
    },
    "paper": {
        "win": "rock",
        "loss": "scissors"
    },
    "scissors": {
        "win": "paper",
        "loss": "rock"
    }
}

shapeScore = {"rock": 1, "paper":2, "scissors":3}

def playGame(p1, p2):
    if p1 == p2:
        return "draw" 
    else:
        return [k for k, v in game[p1].items() if v == p2][0]

def score(shape, gameResult):
    factor = {"loss": 0, "draw": 1, "win": 2}
    return shapeScore[shape] + 3*factor[gameResult]

dataFormatted = [l.split(" ") for l in data]

score1 = 0
score2 = 0
for g in dataFormatted:
    playerShape1 = strategy1Play[g[1]]
    opponentShape = opponentPlay[g[0]]
    
    if strategy2Play[g[1]] == "draw":
        playerShape2 = opponentShape
    else:
        playerShape2 = [v for k, v in game[opponentShape].items() if k != strategy2Play[g[1]]][0]
    score1 += score(playerShape1, playGame(playerShape1, opponentShape))
    score2 += score(playerShape2, strategy2Play[g[1]])

print(score1)
print(score2)