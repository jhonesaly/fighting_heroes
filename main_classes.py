
class Hero:
    def __init__(self, name, age, profession, xp):
        self.name = name
        self.age = age
        self.profession = profession
        self.xp = xp
        self.victories = 0
        self.defeats = 0

    def attack(self):
        attacks = {
            'mago': 'usou cajado',
            'guerreiro': 'usou espada',
            'ladino': 'usou adaga'
        }
        attack = attacks.get(self.profession, 'atacou')
        print(f'o {self.profession} atacou usando {attack}')