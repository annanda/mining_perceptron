import numpy as np
import csv


class Perceptron:
    """
    Implementa o Perceptron utilizando o Delta como forma de calcular o erro
    """

    w = None
    tolerancia = None
    w0 = None
    learning_rate = None
    csv_train_path = None
    x = []
    y = []

    def __init__(self, csv_train_path):
        """
        csv_train_path indica o caminho onde o arquivo CSV está
        """
        self.csv_train_path = csv_train_path
        self.read_csv()
        self.fit()

    def fit(self):
        # quantidade de exemplos
        tamanho_x = len(self.x)

        self.create_random_w(len(self.x[0]))

        variacao_erro = 100000
        erro_anterior = 100000
        self.learning_rate = 0.9
        self.tolerancia = 0.01

        iteracoes = 0
        while variacao_erro > self.tolerancia:
            i = 0
            erro_total = 0
            while i < tamanho_x:
                self.x[i] = np.array(self.x[i])
                net = self.calcula_net(self.x[i])
                y_estimado = self.aplica_funcao_ativacao(net)
                erro = self.calcula_erro(y_estimado, self.y[i])
                erro_total+= abs(erro)
                self.ajusta_w(self.x[i], erro)
                print("Iteração nos exemplos")
                print(i)
                print(self.w)
                i += 1

            print("Variação de erro antes ", variacao_erro)
            variacao_erro = abs(erro_anterior - erro_total)
            print("Variação de erro depois ", variacao_erro)
            print("Erro anterior", erro_anterior)
            print("Erro total", erro_total)
            erro_anterior = erro_total
            iteracoes += 1
            print("Iterações:", iteracoes)

    def create_random_w(self, tamanho_xi):
        # dimensao de cada exemplo
        tamanho_w = tamanho_xi

        # contruindo o w aleatoriamente
        self.w = np.random.rand(1, tamanho_w)
        self.w = self.w[0]
        self.w0 = np.random.rand(1, 1)
        self.w0 = self.w0[0]

    def ajusta_w(self, xi, erro,):
        self.w += self.learning_rate * erro * xi
        self.w0 += self.learning_rate * erro

    def calcula_erro(self, y_estimado, y):
        return float(y) - y_estimado

    def calcula_net(self, xi):
        return np.dot(self.w, xi) + self.w0

    def aplica_funcao_ativacao(self, net):
        return 1/(1 + np.e ** -net)

    def predict(self, x):
        resposta = []

        for xi in x:
            if np.dot(self.w, xi) >= 0.5:
                resposta.append(1)
            else:
                resposta.append(0)

        return resposta

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


p = Perceptron('/home/annanda/Documentos/mineracao/dataset.csv')
print(p.w)
print(p.w0)