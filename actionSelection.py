import math
import random
"""numActions = number of actions ie 2 for fixed phasing and N for variable phasing
            fixed phasing:      0 = same phase, 1 = next phase
            variable phasing:   i = index of next phase (can be same as curr phase)
                                numActions = N-1 if indexing of phases starts from 0
        E = 0.05
        age = age of agent, increment at each time step
"""
def eGreedy(numActions, E, age, currBSON):
    epsilon = math.exp(-1*E*age)
    rand = random.uniform(0,1)

    """ split into 2 probability ranges separated by epsilon ie 0<=p<=epsilon and epsilon<p<=1
        if rand<=epsilon, random action
        else greedy action
    """
    if rand<=epsilon:
        return random.randint(0,numActions-1)
    else:
        nextMaxQ = currBSON[0]['qVal']
        greedyAction = 0
        for i in currBSON:
            if nextMaxQ < i['qVal']:
                nextMaxQ = i['qVal']
                greedyAction = i['action']
        return greedyAction

def softmax(numActions, numberCars, age, currBSON):
    # currBSON = DB entry corresponding to current (curr) state
    temperature = math.exp(-1*age/numberCars)
    options = numActions*[0]
    selProb = numActions*[0]
    selProbSum = 0
    for i in range(0, numActions):
        options[i] = i
        selProb[i] = math.exp(currBSON[i]['qVal']/temperature)
        selProbSum += selProb[i]

    for i in range(0, numActions):
        selProb[i] /= selProbSum

    return numpy.random.choice(options, p=selProb)

if __name__=="__main__":
    numActions = 5
    E = 0.05
    age = 10
    greedyAction = 2
    #print(softmax(numActions, E, age, currBSON))