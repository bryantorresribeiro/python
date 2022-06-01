"""Os dicionários em Python são outra estrutura para armazenar e agrupar dados em formato chave e valor. 
As chaves servem para indexar (posicionar) determinado elemento no dicionário, e só podem ser de tipos imutáveis. 
Geralmente em desenvolvimento web utilizaremos o tipo string para nossas chaves. 
Ele é muito parecido com o JSON (JavaScript Object Notation) na linguagem Javascript."""

"""funcao zip ela ajuda a mescla chave e valores de dois arrays distintos"""
"""para procurar uma posicao em um dicionario e necessario passar o valor da chave entre colchetes"""
"""caso nao queira que estoure uma mensagem de erro caso o valor nn for encontrado passe o metodo get"""
""" Tambem e possivel passar o metodo que retorna so chaves keys() ou entao so valores value() e os dois items()"""
"""" adicionar um nova chave com valor e so declarar passando o nome da chave e o valor que ela vai conter ou o metodo update"""
""" para deletar elementos utilizamos ou pop ou del"""

d1 = {'nome':'kenzinho', 'cidade': 'Curitiba', 'modulo': 'M5'}
print(d1)
print(type(d1))
print(d1['nome'])
print(d1['cidade'])
print(d1['modulo'])
print(d1.get('telefone', 'a chave telefone não existe'))
print(d1.keys())
print(d1.values())

lista_1 = ["telefone", "casado", "idade"]
lista_2 = ["999-999-999", False, 28]

d2 = dict(zip(lista_1, lista_2))
print(d2)
d1.update(d2)
print(d1)
del d1['casado']
print(d1)
d1.clear()
print(d1)
