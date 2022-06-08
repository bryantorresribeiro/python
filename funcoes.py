"""Uma função é um conjunto de comandos que executa uma determinada tarefa e tem um nome. 
Além disso, pode receber parâmetros ou argumentos que especificam o que a tarefa irá processar.
A sua principal finalidade é nos ajudar a organizar programas em pedaços que correspondam a como imaginamos uma solução do problema."""

import math

def delta(a, b, c):

    calc = (b*b) - 4*a*c
    
    return calc

def bhaskara(a, b, c):

    resultado_delta = delta(a, b, c)

    if resultado_delta < 0:
        return 'Delta Negativo'

    x1 = (-b) + math.sqrt(resultado_delta) / (2*a)
    x2 = (-b) - math.sqrt(resultado_delta) / (2*a)
    
    return f'x1={x1}, x2={x2}'

print(bhaskara(4, 2, -6))