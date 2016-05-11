import matplotlib.pyplot as plt

def read(path):
    with open(path, 'r') as txt_file:
        x = []
        for i, line in enumerate(txt_file):
            if i%4 == 0 and i != 0:
                x.append(float(line))

    return(x)
x = read('dados_population_500_generation_1000_tratado.txt')
y = read('dados_population_200_generation_1000.txt')
z = read('dados_population_200_generation_1500_tratado.txt')
w = read('dados_population_200_generation_500_mutation_30_tratado.txt')

plt.plot(range(0,1000), x, c='r')
plt.plot(range(0,1000), y, c='c')
plt.plot(range(0,1500), z, c='m')
plt.plot(range(0,1500), z, c='b')
plt.axis([0, 1500, 160, 230])
plt.grid()
p1 = plt.Rectangle((0, 0), 0.1, 0.1, fc='r')
p2 = plt.Rectangle((0, 0), 0.1, 0.1, fc='c')
p3 = plt.Rectangle((0, 0), 0.1, 0.1, fc='m')
p4 = plt.Rectangle((0, 0), 0.1, 0.1, fc='b')
plt.legend((p1, p2, p3, p4), ('p: 500 g: 1000 ', 'p: 200 g:1000', 'p: 200 g:1500', 'p: 200 g:500 m: 0.3'), loc='best')
plt.xlabel('Número de gerações')
plt.ylabel('Erro total do melhor indivíduo da geração')
plt.title("Erro total do melhor indivíduo da geração por geração")
plt.savefig("images/teste_5.png")
plt.show()
