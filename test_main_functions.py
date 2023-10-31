import unittest
from main_functions import *
from io import StringIO
import sys

class TestMainFunctions(unittest.TestCase):

    def test_lvl_info(self):
        self.assertEqual(lvl_info(500), "Ferro")
        self.assertEqual(lvl_info(1500), "Bronze")
        self.assertEqual(lvl_info(2500), "Prata")
        self.assertEqual(lvl_info(5500), "Ouro")
        self.assertEqual(lvl_info(6500), "Ouro")
        self.assertEqual(lvl_info(7500), "Platina")
        self.assertEqual(lvl_info(8500), "Ascendente")
        self.assertEqual(lvl_info(9500), "Imortal")
        self.assertEqual(lvl_info(10500), "Radiante")

    def test_rating_info(self):
        self.assertEqual(rating_info(5), "Ferro")
        self.assertEqual(rating_info(15), "Bronze")
        self.assertEqual(rating_info(25), "Prata")
        self.assertEqual(rating_info(55), "Ouro")
        self.assertEqual(rating_info(85), "Diamante")
        self.assertEqual(rating_info(95), "Lendário")
        self.assertEqual(rating_info(105), "Imortal")

    def test_random_hero_name(self):
        name = random_name()
        self.assertTrue(name.isalpha())  # Verifica se o nome contém apenas letras
        self.assertTrue(name[0].isupper())  # Verifica se a primeira letra é maiúscula

    def test_random_hero_xp(self):
        min_number = 1
        max_number = 11000
        xp = random_number(min_number, max_number)
        self.assertTrue(min_number <= xp <= max_number)  # Verifica se o xp está dentro do intervalo especificado

    def test_random_hero_league(self):
        hero_quantity = 10
        league = random_hero_league(hero_quantity)
        self.assertEqual(len(league), hero_quantity)  # Verifica se a quantidade de heróis é correta

    def test_hero_match(self):
        hero1 = Hero('Hero1', 25, 'mago', 2000)
        hero2 = Hero('Hero2', 30, 'soldado', 3000)
        winner = hero_match(hero1, hero2)
        self.assertIn(winner, [hero1.name, hero2.name])  # Verifica se o vencedor é um dos heróis

    def test_random_profession(self):
        profession = random_profession()
        self.assertIn(profession, ['mago', 'soldado', 'ladino'])  # Verifica se a profissão está dentro das opções especificadas

    def test_random_hero(self):
        hero = random_hero()
        self.assertIsInstance(hero, Hero)  # Verifica se o objeto retornado é uma instância da classe Hero

    def test_hero_attack(self):
        hero = Hero('HeroTest', 30, 'mago', 2000)
        sys.stdout = StringIO()  # Captura a saída do print
        hero.attack()
        output = sys.stdout.getvalue()
        sys.stdout = sys.__stdout__  # Restaura a saída padrão
        expected_output = 'o mago HeroTest atacou usando cajado\n'
        self.assertEqual(output, expected_output)

    def test_hero_defense(self):
        hero = Hero('HeroTest', 30, 'mago', 2000)
        sys.stdout = StringIO()  # Captura a saída do print
        hero.defense()
        output = sys.stdout.getvalue()
        sys.stdout = sys.__stdout__  # Restaura a saída padrão
        expected_output = 'mago HeroTest defendeu usando barreira\n'
        self.assertEqual(output, expected_output)

    def test_show_heroes(self):
        hero1 = Hero('Hero1', 25, 'mago', 2000)
        hero2 = Hero('Hero2', 30, 'soldado', 3000)
        hero_league = [hero1, hero2]
        sys.stdout = StringIO()  # Captura a saída do print
        show_heroes(hero_league)
        output = sys.stdout.getvalue()
        sys.stdout = sys.__stdout__  # Restaura a saída padrão
        expected_output = (
            "Hero\tIdade\tOfício\tXP\tVictory\tDefeat\tRatio\n"
            "Hero1\t25\tmago\t2000\t0\t0\t0\n"
            "Hero2\t30\tsoldado\t3000\t0\t0\t0\n"
        )
        self.assertEqual(output, expected_output)

    def test_hero_championship(self):
        hero1 = Hero('Hero1', 25, 'mago', 2000)
        hero2 = Hero('Hero2', 30, 'soldado', 3000)
        hero_league = [hero1, hero2]
        hero_championship(hero_league)
        total_matches = sum(hero.victories + hero.defeats for hero in hero_league)/2
        self.assertEqual(total_matches, 2 * (len(hero_league) - 1))  # Verifica se o número total de vitórias e derrotas é igual ao número de jogos jogados

if __name__ == "__main__":
    unittest.main()
