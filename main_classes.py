
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
            'mago': 'cajado',
            'soldado': 'espada',
            'ladino': 'adaga'
        }
        attack = attacks.get(self.profession, 'atacou')
        print(f'o {self.profession} {self.name} atacou usando {attack}')

    def defense(self):
        defenses = {
            'mago': 'barreira',
            'soldado': 'escudo',
            'ladino': 'esquiva'
        }
        defense = defenses.get(self.profession, 'defendeu')
        print(f'{self.profession} {self.name} defendeu usando {defense}')
