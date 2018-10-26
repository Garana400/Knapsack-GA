from random import *
import matplotlib.pyplot as plt

##########################################################
# Solving Knapsack problem using a genetic algorithm.    #
#                                                        #
# Representing the Knapsack items with an array of ones  #
# and zeros. One for a selected item and zero otherwise. #
##########################################################
    
def intializePOP():
    """ Intialize random population to start with,
    if a generated number is less than 0.5 then
    gene equals 1 (item selected).
    """
    pop = []
    for i in range(popSize):
        pop.append([])
        for j in range(n):
            if random() < 0.5:
                pop[i].append(1)
            else:
                pop[i].append(0)
    return pop              


def calcFitness(chromo):
    """ Claculating fitness for each chromosome based of the value
    of each Knapsack item. If a chromosome exceeds the weight allowed
    for Knapsack items, then weight equals 0.
    """
    fit = 0
    weight = 0
    for i in range(len(chromo)):
        if chromo[i]==1:
            fit += ls[i][1]
            weight +=ls[i][0]
    if weight > w:
        return 0
    else:
        return fit

        
def calcCumFitness(pop):
    """ Claculating cummulative fitnesses of a population
    to set ranges for each chromosome and use it for roulette wheel
    selection algorithm afterwards.
    """
    total = 0
    for i in pop:
        cumFitness.append(total)
        x = calcFitness(i)
        fitness.append(x)
        total += x
        

def selection():
    """ Using roulette wheel algorithm, we generate a random number
    and see what range does this number fall to.
    """
    for i in range(int(len(pop)/2)):
        selected = []
        x = randint(0,cumFitness[-1])
        y = randint(0,cumFitness[-1])
        flagx, flagy = False, False
        couple = []
        if x not in cumFitness:
            cumFitness.append(x)
            cumFitness.sort()
            couple.append(cumFitness.index(x)-1)
            cumFitness.remove(x)
        else:
            couple.append(cumFitness.index(x))
        if y not in cumFitness:
            cumFitness.append(y)
            cumFitness.sort()
            couple.append(cumFitness.index(y)-1)
            cumFitness.remove(y)
        else:
            couple.append(cumFitness.index(y))
        selected.append(couple)
        return selected
            

def xoverNmutation(selected):
    """ Applying crossover on the selected couples with a probability of pc <=0.7
    for each couple, then applying mutation on the whole population with
    probability of pm <= 0.1 for each chromosome.
    """
    for i in range(len(selected)):
        if random() <= 0.7:
            x = randint(1,n-2)
            a = pop[selected[i][0]][:x] + pop[selected[i][1]][x:]
            b = pop[selected[i][1]][:x] + pop[selected[i][0]][x:]
            if (calcFitness(a) + calcFitness(b)) > (fitness[selected[i][0]] + fitness[selected[i][1]]):
                pop[selected[i][0]] = a
                pop[selected[i][1]] = b
                
    for i in range(len(pop)):
        temp = pop[i].copy()
        for j in range(len(pop[i])):
            if random() <= 0.1:
                if pop[i][j] == 1:
                    temp[j] = 0
                else:
                    temp[j] = 1
        if calcFitness(temp) > fitness[i]:
            pop[i] = temp

    
if __name__ == "__main__":
    popSize = 300
    gen = 700
    t = int(input())
    for j in range(t):
        n = int(input())
        w = int(input())
        ls = []
        for i in range(n):
            a,b = [int(x) for x in input().split()]
            ls.append((a,b))
        pop = intializePOP()
        champ = 0
        bestOfGen = []
        for i in range(gen):
            fitness = []
            cumFitness = []
            calcCumFitness(pop)
            bestOfGen.append(max(fitness))
            xoverNmutation(selection())
        plt.plot(bestOfGen)
        plt.ylabel("zobd al zebda mn kol geel, 7aga alaga <3")
        plt.xlabel("geel wara geel")
        plt.show()
