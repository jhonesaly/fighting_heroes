
class Hero:
    def __init__(self, name, age, profession, xp, victories, defeats):
        self.name = name
        self.age = age
        self.profession = profession
        self.xp = xp
        self.victories = victories
        self.defeats = defeats

    def attack(self):
        attacks = {
            'mago': 'usou cajado',
            'guerreiro': 'usou espada',
            'ladino': 'usou adaga'
        }
        attack = attacks.get(self.profession, 'atacou')
        print(f'o {self.profession} atacou usando {attack}')