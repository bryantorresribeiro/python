from datetime import datetime

class Ball():
    def __init__(self, ball_type="regular"):
        self.ball_type = ball_type

teste = Ball("mamaco")

#print(teste.ball_type)

#O init seria basicamente um construtor na hora de construir uma claase fora isso sao variaveis nativas da classe podendo ser chamada apenas
#se reverindo ao nome da classe a variavel

def declare_winner(fighter1, fighter2, first_attacker):
    
    playerOne = fighter2.health
    playerTwo = fighter1.health
    rounds = first_attacker
    
    while True:

        if fighter1.name == rounds:
            playerOne -= fighter1.damage_per_attack
            if playerOne >= 0:
                break
            rounds = fighter2.name

        elif fighter2.name == rounds:
            playerTwo -= fighter2.damage_per_attack
            if playerTwo >= 0:
                break
            rounds = fighter1.name       

    return rounds

class Funcionario():

    funcao = "Funcionário"

    def __init__(self, nome_completo:str, cpf, salario=3000):
        name = nome_completo.title().split()
        self.nome = " ".join(name)
        self.cpf = cpf
        self.salario = salario
        self.admissao = datetime.now().strftime("%d/%m/%Y")

    def __str__(self):
       return f' {Funcionario.funcao}: {self.nome}' 

funcionario_1 = Funcionario(" jordan  cardoso poole ", "32112343215")

#print(funcionario_1.__dict__)
#print(funcionario_1)

class Dictionary():
    def __init__(self):
        self.array = []
        
    def newentry(self, word, definition):
        self.array.append({word:definition})
        
    def look(self, key):
        definition = f"Can't find entry for {key}"
        for item in self.array:
            if item.get(key) != None: 
                definition = item.get(key)
        return definition     
