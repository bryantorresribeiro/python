"""Entendendo empacotamento e desempacotamento"""

def sum_numbers(*args):
    sum = 0
    for values in args:
        sum += values
    return sum

print(sum_numbers(*[1, 2, 3, 4, 5, 6]))

def get_multiplied_amount(multiplier, *args):
    calc = 0
    for values in args:
        calc += values*multiplier
    return calc

print(get_multiplied_amount(2, *[1, 2, 3]))
    
def word_concatenator(*args):
    return " ".join(args)

print(word_concatenator(*["Tá", "pegando", "fogo", "bicho!!!"]))

def inverted_word_factory(*args):
    num = len(args)-1
    array = []
    while num >= 0 :
        index = len(args[num])-1
        while index >= 0:
           array.append(args[num][index])
           index -= 1
        array.append(" ")
        num -= 1
        
    return "".join(array)

print(inverted_word_factory(*["eae", "amigão", "belezinha?"]))

def dictionary_separator(**kwargs):
    tupla = ([], [])
    for key, value in kwargs.items():
       tupla[0].append(key)
       tupla[1].append(value)
    return tupla

print(dictionary_separator(**{"name": "Naruto", "age": 16, "favorite word": "Ichiraku Ramen"}))

def dictionary_creator(*args, **kwargs):
    index = 0
    obj = {}
    for values in kwargs.values():
        if index>=len(args):
            return None
        obj.update({args[index]: values})
        index+=1
    return obj

change_keys = ["username", "password", "address"]
user = {"name": "Williams", "key": "1234"}
print(dictionary_creator(*change_keys, **user))

def purchase_logger(**kwargs):
    return f'{kwargs["price"]} {kwargs["name"]} by {kwargs["quantity"]}'

print(purchase_logger(**{"name": "washing powder", "price": 6.7, "quantity": 4}))

def world_cup_logger(country, *args):
    return f'{country} - {sorted(args)}'

print(world_cup_logger('Alemanha', *[2014, 1990, 1974, 1954]))
