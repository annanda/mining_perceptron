import numpy as np
import random


class Perceptron:
    """
    Implementa o Perceptron utilizando o Delta como forma de calcular o erro
    """

    w = None
    tolerancia = None
    bias = None

    def __init__(self):
        pass

    def fit(self, x, y):
        # quantidade de exemplos
        tamanho_x = len(x)

        self.create_random_w(len(x[0]))

        variacao_erro = 100000
        erro_anterior = 100000
        learning_rate = 0.01

        while variacao_erro > self.tolerancia:
            i = 0
            erro_total = 0
            while i < tamanho_x:
                x[i] = np.array(x[i])
                i+= 1
                net = self.calcula_net(x[i])
                y_estimado = self.aplica_funcao_ativacao(net)
                erro = self.calcula_erro(y_estimado, y[i])
                erro_total+= abs(erro)
                self.ajusta_w(x[i], learning_rate, erro)
                variacao_erro = abs(erro_anterior - erro_total)

    def create_random_w(self, tamanho_xi):
        # dimensao de cada exemplo
        tamanho_w = tamanho_xi

        # contruindo o w aleatoriamente
        self.w = np.random.rand(1, tamanho_w)
        self.w = self.w[0]
        self.bias = random.uniform(0, 1)

    def ajusta_w(self, xi, learning_rate, erro,):
        self.w += learning_rate * erro * xi

    def calcula_erro(self, y_estimado, y):
        return y - y_estimado

    def calcula_net(self, xi):
        return np.dot(self.w, xi) + self.bias

    def aplica_funcao_ativacao(self, net):
        return 1/(1 + np.e** -net)

    def predict(self, x):
        resposta = []

        for xi in x:
            if np.dot(self.w, xi) >= 0.5:
                resposta.append(1)
            else:
                resposta.append(0)

        return resposta
