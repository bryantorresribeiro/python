from model.villager import Villager

class Mage(Villager):

    def __init__(self, name: str):

        super().__init__(name)

        self.attack = 10
        self.mana = 100

    def fire_ball(self, target):

        attack = self.attack

        if self.mana - 20 != 0:
            self.mana -= 20
            attack += 20
        else:
            return (False, "Not enough mana!")

        if  attack > target.defense:
            battle = target.health - (attack - target.defense)
            target.health = battle if battle >= 0 else 0

            if target.health == 0:
                target.is_alive = False
                return (False, "Target is dead!")
            
        return target.health