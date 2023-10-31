import unittest
from main_functions import *
from io import StringIO
import sys

class TestMainFunctions(unittest.TestCase):

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

        
    def test_show_heroes(self):
        hero_league = [['Hero1', 5000, 10, 5], ['Hero2', 3000, 8, 8]]
        sys.stdout = StringIO()  # Captura a saída do print
        show_heroes(hero_league)
        output = sys.stdout.getvalue()
        sys.stdout = sys.__stdout__  # Restaura a saída padrão
        expected_output = (
            "Hero\tXP\tVictory\tDefeat\tRatio\n"
            "Hero1\t5000\t10\t5\t5\n"
            "Hero2\t3000\t8\t8\t0\n"
        )
        self.assertEqual(output, expected_output)

    def test_hero_match(self):
        hero_1 = ['Hero1', 5000, 10, 5]
        hero_2 = ['Hero2', 3000, 8, 8]
        winner = hero_match(hero_1, hero_2)
        self.assertIn(winner, ['Hero1', 'Hero2'])  # Verifica se o vencedor é um dos heróis
        
    def test_hero_championship(self):
        hero_league = [['Hero1', 5000, 0, 0], ['Hero2', 3000, 0, 0]]
        hero_championship(hero_league)
        # Verifica se o número total de vitórias e derrotas é igual ao número de jogos jogados
        total_matches = sum(hero[2] + hero[3] for hero in hero_league)/2
        self.assertEqual(total_matches, 2 * (len(hero_league) - 1))

    def test_rating_info(self):
        self.assertEqual(rating_info(5), "Ferro")
        self.assertEqual(rating_info(15), "Bronze")
        self.assertEqual(rating_info(25), "Prata")
        self.assertEqual(rating_info(55), "Ouro")
        self.assertEqual(rating_info(85), "Diamante")
        self.assertEqual(rating_info(95), "Lendário")
        self.assertEqual(rating_info(105), "Imortal")
     

if __name__ == "__main__":
    unittest.main()