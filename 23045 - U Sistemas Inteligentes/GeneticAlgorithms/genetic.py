

from random import *
from operator import add
from functools import reduce

def individual(length, min, max, id):
    # 'Create a member of the population.'
    individuo = [ randint(min,max) for x in range(length) ]
    print("Individuo "+str(id)+": "+str(individuo))
    return individuo
    # return [ randint(min,max) for x in range(length) ]

def population(count, length, min, max):
    """
    Create a number of individuals (i.e. a population).

    count: the number of individuals in the population
    length: the number of values per individual
    min: the minimum possible value in an individual's list of values
    max: the maximum possible value in an individual's list of values

    """
    print("Populacao criada com "+str(count)+" individuos.\n")
    return [ individual(length, min, max, x) for x in range(count) ]

def fitness(individual, target):
    """
    Determine the fitness of an individual. Higher is better.

    individual: the individual to evaluate
    target: the target number individuals are aiming for

    O fitness do individuo perfeito sera ZERO, ja que o somatorio dara o target
    reduce: reduz um vetor a um escalar, neste caso usando o operador add
    """
    sum = reduce(add, individual, 0) # O fitness nesse caso eh o target menos a soma de todas as posicoes do array
    return abs(target-sum)

def media_fitness(pop, target):
    # 'Find average fitness for a population.'
    summed = reduce(add, (fitness(x, target) for x in pop))
    return summed / (len(pop) * 1.0)

def roleta(population):
    # print("   ------- Girou! -------")
    fitnessSoma = sum([individual[0] for individual in population]) # Soma os fitness de todos
    agulha  = uniform(0, fitnessSoma) # Roda a roleta e atribui um valor para a agulha
    # print("  > Fitness Soma: "+ str(fitnessSoma))
    # print("  > Pos_agulha: " + str(agulha))
    pos_atual = 0
    for individual in population: # Percorre a roleta conferindo onde a agulha parou
        pos_atual += individual[0]
        if pos_atual >= agulha:
            # print("  > Selecionado: o individuo com fatia = ["+ str(pos_atual - individual[0])+"-"+str(pos_atual)+"]\n  " + str(individual))
            return individual[1]

def evolve(pop, target, retain=0.2, random_select=0.05, mutate=0.01):
    # 'Tabula cada individuo e o seu fitness'
    graded = [ (fitness(x, target), x) for x in pop]
    gradedCopia = graded
    # 'Ordena pelo fitness os individuos - menor->maior'
    graded = [ x[1] for x in sorted(graded)]
    # 'calcula qtos serao elite'
    retain_length = int(len(graded)*retain)
    # 'elites ja viram pais'
    parents = graded[:retain_length]
    # randomly add other POUCOS individuals to
    # promote genetic diversity

    # for individual in graded[retain_length:]:
    #     if random_select > random():
    #         parents.append(individual)

    giros = randint(0,int(len(pop)-len(parents)))
    while (giros+len(parents))%2 != 0: # Enquanto o numero total de pais nao for par
        giros = randint(0,int(len(pop)-len(parents)))
    
    # print("\n ******* Giros da roleta: "+str(giros) + " *******")
    for giro in range(giros):
        parents.append(roleta(gradedCopia[retain_length:]))
    
    # mutate some individuals
    for individual in parents:
        if mutate > random():
            pos_to_mutate = randint(0, len(individual)-1)
            # this mutation is not ideal, because it
            # restricts the range of possible values,
            # but the function is unaware of the min/max
            # values used to create the individuals,
            individual[pos_to_mutate] = randint(
                min(individual), max(individual))
    # crossover parents to create children
    parents_length = len(parents)
    # print("Parents_lenght: "+ str(parents_length))
    # 'descobre quantos filhos terao que ser gerados alem da elite e aleatorios'
    desired_length = len(pop) - parents_length
    children = []
    # 'comeca a gerar filhos que faltam'
    while len(children) < desired_length:
        # 'escolhe pai e mae no conjunto de pais'
        male = randint(0, parents_length-1)
        female = randint(0, parents_length-1)
        if male != female:
            male = parents[male]
            female = parents[female]
            half = len(male) // 2 # Floor division (retorna o valor inteiro piso)
            # 'gera filho metade de cada'
            child = male[:half] + female[half:]
            # 'adiciona novo filho a lista de filhos'
            children.append(child)
    # 'adiciona a lista de pais (elites) os filhos gerados'
    parents.extend(children)
    return parents
