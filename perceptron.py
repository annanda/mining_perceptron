import numpy as np


class Perceptron:
    """
    Implementa o Perceptron Learning Algorithm
    """

    w = None

    def fit(self, x, y):
        #quantidade de exemplos
        tamanho_x = len(x)

        tamanho_w = len(x[0]) + 1

        self.create_random_w(len(x[0]))

        i = 0
        while i < tamanho_x:
            x[i] = self.insert_first_as_one(x[i])

            if not is_same_sign(np.dot(self.w, x[i]), y[i]):
                self.chance_w(x[i], y[i])
                #volta ao inicio da lista de exemplos
                i = 0
                break
            i += 1

    def create_random_w(self, tamanho_xi):
        #dimensao de cada exemplo depois que adiciono o 1 na frente
        tamanho_w = tamanho_xi + 1

        #contruindo o w aleatoriamente
        self.w = np.random.rand(1, tamanho_w)
        self.w = self.w[0]

    def chance_w(self, xi, yi):
        self.w = self.w + (yi * xi)


    def predict(self, x):
        resposta = []

        for xi in x:
            xi = self.insert_first_as_one(xi)
            if np.dot(self.w, xi) >= 0:
                resposta.append(1)
            else:
                resposta.append(-1)

        return resposta

    def insert_first_as_one(self, xi):
        xi.insert(0, 1)
        xi = np.array(xi)
        return xi

def is_same_sign(value_1, value_2):
    #verifica se as duas entradas tem o mesmo sinal
    return (value_1 < 0) == (value_2 < 0)