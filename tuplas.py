"""As tuplas, assim como as listas, são tipos básicos de sequência de dados do Python, porém detém algumas particularidades. 
São imutáveis, ou seja, não podem sofrer alterações em seus valores e são ideais para armazenar dados agrupados tendo a
 certeza de que eles não serão modificados em qualquer outro lugar do código."""

#tuplas sao declaradas com parenteses

tupla = ('Valor_1', 2, 3.1, 'Kenzie Academy', ['Elemento1', 'Elemento2'], 'Kenzie Academy',)
print(tupla)
print(tupla[-1])
print(len(tupla))
print(tupla.count("Kenzie Academy"))
print(tupla.index(3.1))
tupla[-1] = "Ultimo Elemento"
print(tupla)
