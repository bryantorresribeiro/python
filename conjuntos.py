"""Algumas características importantes sobre Conjuntos em Python são:

Armazena somente dados únicos, ou seja, não existem dados repetidos em um conjunto;
Suporta operações matemáticas sobre conjuntos (união, intersecção, diferença);
Não é possível modificar os itens existentes, mas podemos adicionar ou remover novos elementos, ou seja, conjuntos são mutáveis;
São iteráveis, ou seja, podemos acessar seus elementos um a um;
Não são considerados sequências como listas e tuplas;
Não suportam indexação e fatiamento;
Podem conter apenas elementos imutáveis;"""

"""Conjuntso sao declarados com chaves"""

conjunto_1 = {1, 1, 'Kenzie', 'Academy', 'Kenzie', 10}
print(conjunto_1)
print(len(conjunto_1))
conjunto_1.add("Novo Elemento")
print(conjunto_1)
conjunto_1.discard("Novo Elemento")
print(conjunto_1)
conjunto_1.clear()
print(conjunto_1)