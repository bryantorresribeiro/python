from soma import somar
from subtracao import subtrair

resultado_da_soma = somar(15,7)
print(resultado_da_soma)

    
resultado_da_subtracao = subtrair(15,7)
print(resultado_da_subtracao)


"""o soma e o subtrair sao modulos e o main.py e arquivo"""

""""Ao criar um sistema, ele sempre deverá conter um arquivo principal, ou seja, 
um arquivo que será executado e que servirá como porta de entrada para os outros módulos e pacotes do seu projeto."""

"""A importação absoluta acontece quando chamamos o arquivo a partir da raiz do projeto. 
Foi o que aconteceu no main.py, como soma.py e subtracao.py estão na raiz do projeto, é possível acessá-los diretamente."""