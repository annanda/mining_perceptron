====================
Testes de Perceptron
====================

Deve ser possível criar um Perceptron::
    >>> from perceptron import Perceptron
    >>> perceptron = Perceptron()

O w deve ser construido corretamente::
    >>> x = [[1,2], [6,7], [1,1]]
    >>> y = [-1, 1, -1]
    >>> perceptron.create_random_w(len(x[0]))
    >>> print (len(perceptron.w))
    3