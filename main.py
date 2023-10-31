# Base da aplicação
import os
from main_functions import *
from main_classes import Hero

# Configurações iniciais

os.system('cls')
print("Bem-vindo ao campeonato dos heróis!\n")
input("Pressione 'enter' para começar a simulação do campeonato. ")

while True:

    herois = random_hero_league(20)
    hero_championship(herois, 3)

    # Listando heróis
    print("Esses é o ranking da liga: ")
    show_heroes(herois)

    # Input de herói escolhido
    heroi_escolhido = input("Por favor, escolha um herói da lista para saber suas informações: ")

    # Verifica se escolha está na lista

    heroi_na_lista = False

    for heroi in herois:
        if heroi.name == heroi_escolhido:
            heroi_na_lista = True
            vitorias_heroi = heroi.victories
            rating_heroi = rating_info(heroi.victories-heroi.defeats)
            nivel_heroi = lvl_info(heroi.xp)
            break

    if heroi_na_lista:
        # Mostrando categoria do herói
        print(f"O Herói de nome **{heroi_escolhido}** está no nível **{nivel_heroi}**")
        print(f"O Herói tem de saldo de **{vitorias_heroi}** vitórias e está na liga **{rating_heroi}**")

    else:
        print("Esse herói não está na lista.")
        novo_heroi = input("Deseja adicioná-lo? [s/n] ")

        if novo_heroi.lower() == 's':
            novo_xp = int(input(f"Digite o xp do herói {heroi_escolhido}: "))
            herois.append([heroi_escolhido, novo_xp, 0, 0])

            continue
        else:
            continue

    fim = input("Deseja parar [s]? ")

    if fim.lower() == 's':
        print("Até a próxima!")
        break

    else:
        print("Continuando...")
