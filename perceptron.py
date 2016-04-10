import numpy as np


class Perceptron:
    """
    Implementa o Perceptron Learning Algorithm
    """

    w = None

    def fit(self, x, y):
        #quantidade de exemplos
        tamanho_x = len(x)

        #dimensao de cada exemplo
        tamanho_w = len(x[0]) + 1

        #contruindo o w aleatoriamente
        self.w = np.random.rand(1, tamanho_w)
        self.w = self.w[0]

        i = 0
        while i < tamanho_x:
            x[i].insert(0, 1)
            x[i] = np.array(x[i])

            if np.dot(self.w, x[i]) != y[i]:
                self.w = self.w + y[i] * x[i]
                #volta ao inicio da lista de exemplos
                i = 0
                break
            i += 1

    def predict(self, x):
        pass
