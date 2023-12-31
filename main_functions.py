# Funções da aplicação

import random
from main_classes import Hero

def lvl_info(hero_xp):
    if hero_xp < 1000:
        return "Ferro"
    elif 1001 <= hero_xp <= 2000:
        return "Bronze"
    elif 2001 <= hero_xp <= 5000:
        return "Prata"
    elif 5001 <= hero_xp <= 7000:
        return "Ouro"
    elif 7001 <= hero_xp <= 8000:
        return "Platina"
    elif 8001 <= hero_xp <= 9000:
        return "Ascendente"
    elif 9001 <= hero_xp <= 10000:
        return "Imortal"
    else:
        return "Radiante"


def rating_info(hero_rating):
    if hero_rating < 10:
        return "Ferro"
    elif 11 <= hero_rating <= 20:
        return "Bronze"
    elif 21 <= hero_rating <= 50:
        return "Prata"
    elif 51 <= hero_rating <= 80:
        return "Ouro"
    elif 81 <= hero_rating <= 90:
        return "Diamante"
    elif 91 <= hero_rating <= 100:
        return "Lendário"
    else:
        return "Imortal"


def random_name():
    consoantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
    vogais = ['a', 'e', 'i', 'o', 'u']

    num_silabas = random.choice([2, 3])

    nome = ''
    
    for _ in range(num_silabas):
        consoante_aleatoria = random.choice(consoantes)
        vogal_aleatoria = random.choice(vogais)
        silaba = consoante_aleatoria + vogal_aleatoria
        nome += silaba
    
    return nome.capitalize()


def random_number(min_number, max_number):
    return random.randint(min_number, max_number)


def random_profession():
    professions = ['mago', 'soldado', 'ladino']
    profession = random.choice(professions)
    return profession


def random_hero():
    hero_name = random_name()
    hero_xp = random_number(1, 11000)
    hero_profession = random_profession()
    hero_age = random_number(20, 70)
    hero = Hero(hero_name, hero_age, hero_profession, hero_xp)
    return hero


def random_hero_league(hero_quantity):
    hero_league = []
    for i in range(hero_quantity):
        hero = random_hero()
        hero_league.append(hero)

    return hero_league


def show_heroes(hero_league):
    print("Hero\tIdade\tOfício\tXP\tVictory\tDefeat\tRatio")
    for hero in hero_league:
        print(f"{hero.name}\t{hero.age}\t{hero.profession}\t{hero.xp}\t{hero.victories}\t{hero.defeats}\t{hero.victories-hero.defeats}")


def hero_match(hero_1, hero_2):
    prevalence = {
        'soldado': 'ladino',
        'ladino': 'mago',
        'mago': 'soldado'
    }

    hero_1_xp = hero_1.xp
    hero_2_xp = hero_2.xp

    if prevalence[hero_1.profession] == hero_2.profession:
        hero_1_xp *= 2
        hero_2_xp /= 2
    elif prevalence[hero_2.profession] == hero_1.profession:
        hero_2_xp *= 2
        hero_1_xp /= 2

    hero_total_xp = hero_1_xp + hero_2_xp
    match_number = random_number(1,int(hero_total_xp))

    print(f'Disputa: {hero_1.name} X {hero_2.name}')

    hero_1.attack()
    hero_2.defense()
    hero_2.attack()
    hero_1.defense()

    if match_number < hero_1_xp:
        hero_1.victories += 1
        hero_2.defeats += 1
        print(f'Vencedor:{hero_1.name}\n')
        return hero_1.name
    else:
        hero_2.victories += 1
        hero_1.defeats += 1
        print(f'Vencedor:{hero_2.name}\n')
        return hero_2.name


def hero_championship(hero_league, seasons=1):
    for k in range(seasons):
        for i in range(len(hero_league)):
            for j in range(len(hero_league)):
                if i == j :
                    continue
                else:
                    hero_match(hero_league[i], hero_league[j])


if __name__ == '__main__':

    import os
    os.system('cls')

    hero_league = random_hero_league(20)
    hero_championship(hero_league, 4)
    show_heroes(hero_league)
