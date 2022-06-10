class Villager:
    
    def __init__(self, name:str):
        self.name = name
        self.health = 50
        self.defense = 0
        self.attack = 0
        self.is_alive = True
       
    def check_health(self, incoming_attack_value:int):

        if incoming_attack_value > self.defense:
            battle = self.health - (incoming_attack_value -self.defense)
            self.health = battle

            if battle <= 0:
                self.is_alive = False
                return (False, "Target is dead!")

            return self.health

    def normal_attack(self, target):

        if self.attack > target.defense:
            battle = target.health - (self.attack - target.defense)
            target.health = battle if battle >= 0 else 0

            if target.health == 0:
                target.is_alive = False
                return (False, "Target is dead!")
            
        return target.health
