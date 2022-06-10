#O init seria basicamente um construtor na hora de construir uma claase fora isso sao variaveis nativas da classe podendo ser chamada apenas
#se reverindo ao nome da classe a variavel

from datetime import datetime

class Ball():
    def __init__(self, ball_type="regular"):
        self.ball_type = ball_type

teste = Ball("mamaco")

print(teste.ball_type)

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




        
       
