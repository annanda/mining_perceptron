import numpy as np
import random
import csv


class PerceptronGA:

    w = None
    w0 = None
    x = []
    y = []
    number_of_features = None

    def __init__(self,
                 csv_train_path,
                 population_size=5,
                 number_of_generations=10,
                 mutation_chance=0.1,
                 crossover_chance=0.8,
                 ):
        self.csv_train_path = csv_train_path
        self.population_size = population_size
        self.number_of_generations = number_of_generations
        self.crossover_chance = crossover_chance
        self.mutation_chance = mutation_chance

        self.read_csv()
        self.fit()

    def fit(self):
        population = self.create_initial_population()

        for generation in range(self.number_of_generations):
            population = self.select(population)
            population = self.crossover(population)
            population = self.mutate(population)

        sorted_population, fits = self.sort_by_best(population)
        best_individual = sorted_population[-1]
        self.w0 = best_individual[0]
        self.w = best_individual[1:]

    def sort_by_best(self, population):
        population_with_fit = []

        # cria uma lista de tuplas (individuo, valor_fit) para toda a populacao
        for individual in population:
            population_with_fit.append((individual, self.fitness_function(individual)))


        sorted_population = sorted(population_with_fit, key=lambda individual_fit: individual_fit[1])


        # separa as tuplas anteriores em duas duplas
        population_new, fits = zip(*sorted_population)
        # list de individuos e lista de suas fits
        population_new = list(population_new)
        fits = list(fits)
        return population_new, fits

    def select(self, population):
        sorted_population, fits = self.sort_by_best(population)
        total = 0
        for i in range(len(sorted_population)):
            total += fits[i]
            fits[i] = total

        selected = []
        for i in range(len(sorted_population)):
            aleatorio = random.uniform(1, total)
            for j in range(len(fits)):
                # import pdb; pdb.set_trace()
                if aleatorio <= fits[j]:
                    selected.append(sorted_population[j])
                    break

        return selected

    def crossover(self, population):
        for i in range(0, len(population), 2):
            if i+1 == len(population): #população impar
                # o ultimo continua
                continue
            random.seed()
            if random.random() > self.crossover_chance:
                continue

            ind1 = population[i]
            ind2 = population[i+1]

            point = random.choice(range(1, len(ind1)))

            population[i] = np.append(ind1[0:point], ind2[point:])
            population[i+1] = np.append(ind2[0:point], ind1[point:])

        for var in range(5):
            if len(population[var]) != 4:
                pass
        return population

    def mutate(self, population):
        for i in range(len(population)):
            individual = population[i]
            if random.random() > self.mutation_chance: # mutation chance
                return population
            mutation_position = random.choice(range(len(individual)))
            auxiliar_list = list(range(len(individual)))
            auxiliar_list.reverse()
            individual[mutation_position] = random.choice(range(auxiliar_list[mutation_position]+1))

            population[i] = individual
        return population

    def fitness_function(self, individual):
        erro_total = 0
        for i, example in enumerate(self.x):
            net = self.calcula_net(individual, example)
            y_estimado = self.aplica_funcao_ativacao(net)
            erro = self.calcula_erro(y_estimado, self.y[i])
            erro_total += erro

        max_error = len(self.x) # o erro maximo por exemplo é 1
        return max_error - erro_total

    def create_initial_population(self):
        population = []
        for i in range(self.population_size):
            random_individual = np.random.rand(1, self.number_of_features+1)[0]
            population.append(random_individual)

        return population

    def calcula_erro(self, y_estimado, y):
        return abs(float(y) - y_estimado)

    def calcula_net(self, individual, example):
        net = np.dot(individual[1:], example) + individual[0]
        return net

    def aplica_funcao_ativacao(self, net):
        return 1/(1 + np.e ** -net)

    def read_csv(self):
        """
        Transforma os dados de um arquivo CSV na lista de exemplos x (com 3 features cada exemplo)
        e na lista y que diz qual a classe o exemplo pertence
        So funciona com exemplos que tem 3 features
        """
        with open(self.csv_train_path, 'r') as csv_file:
            exemples = csv.reader(csv_file, delimiter=';')

            for row in exemples:
                xi = []
                xi.append(float(row[0]))
                xi.append(float(row[1]))
                xi.append(float(row[2]))
                self.y.append(row[3])
                self.x.append(xi)
        self.number_of_features = len(self.x[0])

p = PerceptronGA('/home/annanda/Documentos/mineracao/dataset.csv')
print(p.w)
print(p.w0)