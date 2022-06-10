def soma(a, b):
    return a + b

def test_funcao_soma_dois_numeros():
    result = soma(1, 2)
    expect = 3
    assert result == expect, "Verifique se a função está somando corretamente"

# pytest teste.py
# caso o pytest nao rode coloque asdf reshim e reincie o terminal

def converte_celsius_to_fahrenheit(celsius: int):
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit

def test_converte_celsius_to_fahrenheit():
    result = converte_celsius_to_fahrenheit(12)
    expect = 53.6
    assert result == expect, "Verifique se a função está convertendo corretamente"

def imprimir_padrao(tamanho: int):
    if type(tamanho) is not int:
        return "Passe um inteiro como tamanho"
    return "*" * tamanho

def test_imprimir_padrao():
    result = imprimir_padrao(5)
    expect = "*****"
    assert result == expect, "Verifique se a função está com o tipagem correta"

def boas_vindas_estudante(nome: str):
    return f"Olá, {nome}! Boas-vindas à aula."

def test_boas_vindas_estudante():
    result = boas_vindas_estudante("bryan")
    expect = "Olá, bryan! Boas-vindas à aula."
    assert result == expect, "Verifique se a função está com o tipagem correta"
  
def fatorial(n: int):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

def test_fatorial():
    result = fatorial(5)
    expect = 120
    assert result == expect, "Verifique se a função está com um numero maior que 1"