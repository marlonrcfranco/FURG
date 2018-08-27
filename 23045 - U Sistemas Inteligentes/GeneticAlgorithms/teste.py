
# Objetivo: achar um vetor de inteiros (entre i_min e i_max) com i_length posicoes cuja a soma de todos os termos seja o mais proximo possivel de target

#O algoritmo rodara epochs vezes -> numero de populacoes geradas. Sera impresso a media de fitness de cada uma das epochs populacoes

#RODAR COM PYTHON 2!!! (senao colocar () em print e tirar x de xrange
  
from genetic import *
target = 782 # O objetivo que os individuos estao buscando
i_length = 10 # Numero de caracteristicas distintas em um individuo (# of features)
i_min = 0 # Valor minimo que uma caracteristica pode assumir em uma lista de caracteristicas de um individuo (min value in a feature)
i_max = 1000 # Valor maximo que uma caracteristica pode assumir em uma lista de caracteristicas de um individuo (max value in a feature)
p_count = 6 # Numero de individuos na populacao
epochs = 4000 # Numero de epocas (evolucoes)
p = population(p_count, i_length, i_min, i_max) # Cria uma populacao de tamanho p_count
fitness_history = [media_fitness(p, target),]
for i in range(epochs):
    p = evolve(p, target)
    fitness_history.append(media_fitness(p, target))
count = 0
for datum in fitness_history:
    count += 1
    print ("Evolucao #" + str(count) + ": \t" + str(datum))
