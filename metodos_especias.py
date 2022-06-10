class Filme():
    def __init__(self, title:str, duration:int):
        self.title = title
        self.duration = duration
        self.numero_de_exibicoes = 0

    def __str__(self):
        return f"<{Filme.__name__}: {self.title} >"

    def __len__(self):
        return self.duration

    def __call__(self):
        self.numero_de_exibicoes += 1
        return self.numero_de_exibicoes
     
john_wick = Filme('John Wick', 113)

print(john_wick)
print(len(john_wick))
print(john_wick.numero_de_exibicoes)
print(vars(john_wick))
print(john_wick.numero_de_exibicoes)
print(vars(john_wick))

