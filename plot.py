import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import numpy as np


def plot(w, w0):
    arquivo = open('dataset.csv', 'r')
    # arquivo = open('test.csv', 'r')
    X = []
    for line in arquivo:
        vec = line.split(';')
        for i in range(len(vec) - 1):
            vec[i] = float(vec[i])
        vec[-1] = int(vec[-1])
        X.append(vec)

    x1 = []
    y1 = []
    z1 = []
    x2 = []
    y2 = []
    z2 = []

    for line in X:
        if line[-1] == 1:
            x1.append(line[0])
            y1.append(line[1])
            z1.append(line[2])
        if line[-1] == 0:
            x2.append(line[0])
            y2.append(line[1])
            z2.append(line[2])

    plano = (w, w0)
    fig = plt.figure()
    ax = p3.Axes3D(fig)
    ax.scatter(x1, y1, z1, c='blue')
    ax.scatter(x2, y2, z2, c='red')
    xx, yy = np.meshgrid(range(-10,10), range(-10,10))
    z = (-plano[0][0] * xx - plano[0][1] * yy - plano[1]) * 1. / plano[0][2]
    ax.plot_surface(xx, yy, z, alpha=0.5, color='green')
    plt.savefig("imagem_ga_p_200_g_1000_dataset.png")
    plt.show()

plot([0., 0.3140456, 0.99699966],  0.622833369694)

