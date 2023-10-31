# Base da aplicação
import os
from main_functions import *

# Configurações iniciais

print("Bem-vindo ao machmaking dos heróis!")
herois = random_hero_league(20)
hero_championship(herois, 4)

while True:

    os.system('cls')

    # Listando heróis
    print("Esses são os heróis da liga: ")
    show_heroes(herois)

    # Input de herói escolhido
    heroi_escolhido = input("Por favor, escolha um herói da lista para saber a sua categoria: ")

    # Verifica se escolha está na lista

    heroi_na_lista = False

    for heroi in herois:
        if heroi[0] == heroi_escolhido:
            heroi_na_lista = True
            vitorias_heroi = heroi[2]
            rating_heroi = rating_info(heroi[2]-heroi[3])
            break

    if heroi_na_lista:
        # Mostrando categoria do herói
        print(f"O Herói tem de saldo de **{vitorias_heroi}** está no nível de **{rating_heroi}**")

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

