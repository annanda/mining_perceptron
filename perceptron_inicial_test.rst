====================
Testes de Perceptron
====================

Deve ser possível criar um Perceptron::
    >>> from perceptron_inicial import PerceptronInicial
    >>> perceptron = PerceptronInicial()

O w deve ser construido corretamente::
    >>> x = [[1,2], [6,7], [1,1], [1,2], [7, 7]]
    >>> y = [-1, 1, -1, -1, 1]
    >>> perceptron.create_random_w(len(x[0]))
    >>> print (len(perceptron.w))
    3

Funcao que verifica se dois numeros tem o mesmo sinal deve estar correta::
    >>> from perceptron import is_same_sign
    >>> is_same_sign(2, -7)
    False
    >>> is_same_sign(-2, -7)
    True
    >>> is_same_sign(2, 7)
    True
    >>> is_same_sign(-2, 7)
    False

Valor de w deve ser alterado corretamente::
    >>> import numpy
    >>> perceptron.w = numpy.array([1, 1, 1])
    >>> x[0].insert(0, 1)
    >>> x[0]
    [1, 1, 2]
    >>> x[0] = numpy.array(x[0])
    >>> perceptron.chance_w(x[0], y[0])
    >>> perceptron.w
    array([ 0,  0, -1])

Predict deve estar correto, de acordo com w::
    >>> perceptron.w = numpy.array([1, 1, 1])
    >>> novos_x = [[1,3], [1,4], [1, -7]]
    >>> perceptron.predict(novos_x)
    [1, 1, -1]

Deve adicionar o 1 no inicio de cada exemplo corretamente::
    >>> perceptron.insert_first_as_one([2, 3, 4])
    array([1, 2, 3, 4])
    >>> from perceptron_inicial import PerceptronInicial
    >>> perceptron = PerceptronInicial()

O w deve ser construido corretamente::
    >>> x = [[1,2], [6,7], [1,1], [1,2], [7, 7]]
    >>> y = [-1, 1, -1, -1, 1]
    >>> perceptron.create_random_w(len(x[0]))
    >>> print (len(perceptron.w))
    3

Funcao que verifica se dois numeros tem o mesmo sinal deve estar correta::
    >>> from perceptron import is_same_sign
    >>> is_same_sign(2, -7)
    False
    >>> is_same_sign(-2, -7)
    True
    >>> is_same_sign(2, 7)
    True
    >>> is_same_sign(-2, 7)
    False

Valor de w deve ser alterado corretamente::
    >>> import numpy
    >>> perceptron.w = numpy.array([1, 1, 1])
    >>> x[0].insert(0, 1)
    >>> x[0]
    [1, 1, 2]
    >>> x[0] = numpy.array(x[0])
    >>> perceptron.chance_w(x[0], y[0])
    >>> perceptron.w
    array([ 0,  0, -1])

Predict deve estar correto, de acordo com w::
    >>> perceptron.w = numpy.array([1, 1, 1])
    >>> novos_x = [[1,3], [1,4], [1, -7]]
    >>> perceptron.predict(novos_x)
    [1, 1, -1]

Deve adicionar o 1 no inicio de cada exemplo corretamente::
    >>> perceptron.insert_first_as_one([2, 3, 4])
    array([1, 2, 3, 4])
    >>> from perceptron import PerceptronInicial
    >>> perceptron = PerceptronInicial()

O w deve ser construido corretamente::
    >>> x = [[1,2], [6,7], [1,1], [1,2], [7, 7]]
    >>> y = [-1, 1, -1, -1, 1]
    >>> perceptron.create_random_w(len(x[0]))
    >>> print (len(perceptron.w))
    3

Funcao que verifica se dois numeros tem o mesmo sinal deve estar correta::
    >>> from perceptron_inicial import is_same_sign
    >>> is_same_sign(2, -7)
    False
    >>> is_same_sign(-2, -7)
    True
    >>> is_same_sign(2, 7)
    True
    >>> is_same_sign(-2, 7)
    False

Valor de w deve ser alterado corretamente::
    >>> import numpy
    >>> perceptron.w = numpy.array([1, 1, 1])
    >>> x[0].insert(0, 1)
    >>> x[0]
    [1, 1, 2]
    >>> x[0] = numpy.array(x[0])
    >>> perceptron.chance_w(x[0], y[0])
    >>> perceptron.w
    array([ 0,  0, -1])

Predict deve estar correto, de acordo com w::
    >>> perceptron.w = numpy.array([1, 1, 1])
    >>> novos_x = [[1,3], [1,4], [1, -7]]
    >>> perceptron.predict(novos_x)
    [1, 1, -1]

Deve adicionar o 1 no inicio de cada exemplo corretamente::
    >>> perceptron.insert_first_as_one([2, 3, 4])
    array([1, 2, 3, 4])
    >>> from perceptron import PerceptronInicial
    >>> perceptron = PerceptronInicial()

O w deve ser construido corretamente::
    >>> x = [[1,2], [6,7], [1,1], [1,2], [7, 7]]
    >>> y = [-1, 1, -1, -1, 1]
    >>> perceptron.create_random_w(len(x[0]))
    >>> print (len(perceptron.w))
    3

Funcao que verifica se dois numeros tem o mesmo sinal deve estar correta::
    >>> from perceptron_inicial import is_same_sign
    >>> is_same_sign(2, -7)
    False
    >>> is_same_sign(-2, -7)
    True
    >>> is_same_sign(2, 7)
    True
    >>> is_same_sign(-2, 7)
    False

Valor de w deve ser alterado corretamente::
    >>> import numpy
    >>> perceptron.w = numpy.array([1, 1, 1])
    >>> x[0].insert(0, 1)
    >>> x[0]
    [1, 1, 2]
    >>> x[0] = numpy.array(x[0])
    >>> perceptron.chance_w(x[0], y[0])
    >>> perceptron.w
    array([ 0,  0, -1])

Predict deve estar correto, de acordo com w::
    >>> perceptron.w = numpy.array([1, 1, 1])
    >>> novos_x = [[1,3], [1,4], [1, -7]]
    >>> perceptron.predict(novos_x)
    [1, 1, -1]

Deve adicionar o 1 no inicio de cada exemplo corretamente::
    >>> perceptron.insert_first_as_one([2, 3, 4])
    array([1, 2, 3, 4])
    >>> from perceptron import PerceptronInicial
    >>> perceptron = PerceptronInicial()

O w deve ser construido corretamente::
    >>> x = [[1,2], [6,7], [1,1], [1,2], [7, 7]]
    >>> y = [-1, 1, -1, -1, 1]
    >>> perceptron.create_random_w(len(x[0]))
    >>> print (len(perceptron.w))
    3

Funcao que verifica se dois numeros tem o mesmo sinal deve estar correta::
    >>> from perceptron import is_same_sign
    >>> is_same_sign(2, -7)
    False
    >>> is_same_sign(-2, -7)
    True
    >>> is_same_sign(2, 7)
    True
    >>> is_same_sign(-2, 7)
    False

Valor de w deve ser alterado corretamente::
    >>> import numpy
    >>> perceptron.w = numpy.array([1, 1, 1])
    >>> x[0].insert(0, 1)
    >>> x[0]
    [1, 1, 2]
    >>> x[0] = numpy.array(x[0])
    >>> perceptron.chance_w(x[0], y[0])
    >>> perceptron.w
    array([ 0,  0, -1])

Predict deve estar correto, de acordo com w::
    >>> perceptron.w = numpy.array([1, 1, 1])
    >>> novos_x = [[1,3], [1,4], [1, -7]]
    >>> perceptron.predict(novos_x)
    [1, 1, -1]

Deve adicionar o 1 no inicio de cada exemplo corretamente::
    >>> perceptron.insert_first_as_one([2, 3, 4])
    array([1, 2, 3, 4])