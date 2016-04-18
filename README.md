# Perceptron que usa erro do tipo Delta

Para rodar:

## Instancie a classe Perceptron, passando como parâmetro o caminho do arquivo CSV que contém os exemplos de treinamento: 
```python
p = Perceptron('/home/annanda/exemplos.csv')
```

## Chame o método predict passando como parâmetro a lista de pontos cuja classe é desconhecida: 
```python
p.predict(x)
```

Esse método vai retornar uma lista preenchida com 0 ou 1, indicando qual a classe que aquele ponto pertence. 
