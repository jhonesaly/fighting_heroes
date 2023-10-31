# Projeto: Matchmaking dos Heróis

Este projeto simula um campeonato entre heróis, os colocando em determinada categoria pelo seu desempenho. Cada herói possui um nome, experiência (XP), número de vitórias e número de derrotas. Eles são classificados em diferentes categorias com base em seu saldo de vitórias e derrotas.

Os nomes dos heróis são formados pela concatenação aleatória de letras. Cada nome pode ter aleatoriamente entre 2 e 3 sílabas formadas por uma consoante aleatória e uma vogal aleatória.

Já a experiência é um número aleatório entre 0 e 11000 (pois o maior ranking de experiência é 10000), então todas as categorias têm uma probabilidade próxima de ocorrerem. Se fosse um número maior que 11000, começa a aumentar a probabilidade de muitos estarem no maior ranking.

Na disputa, a vitória é determinada por um número aleatório que vai de 1 até a soma das experiências dos heróis na disputa. Quanto mais XP, maior a chance de ganhar. Por exemplo, digamos que vai haver uma disputa entre o herói 1, com 20 de xp, e o herói 2, com 60 de xp. Então será gerado um número aleatório entre 1 e 80 (20+60). Se der abaixo de 21, vitória do herói 1; se der acima de 20, vitória do herói 2.

E o campeonato se dá pela disputa entre todos os heróis duas vezes (ida e volta, i=j e j=i). As vitória e derrotas são registradas e então o "rating" pode ser calculado pela diferenã entre esses valores.

O projeto é baseado no desafio da plataforma Dio que pede o seguinte:

```

Crie uma função que recebe como parâmetro a quantidade de vitórias e derrotas de um jogador,
depois disso retorne o resultado para uma variável, o saldo de Rankeadas deve ser feito através do calculo (vitórias - derrotas)

Se vitórias for menor do que 10 = Ferro
Se vitórias for entre 11 e 20 = Bronze
Se vitórias for entre 21 e 50 = Prata
Se vitórias for entre 51 e 80 = Ouro
Se vitórias for entre 81 e 90 = Diamante
Se vitórias for entre 91 e 100= Lendário
Se vitórias for maior ou igual a 101 = Imortal

Ao final deve se exibir uma mensagem:
"O Herói tem de saldo de **{saldoVitorias}** está no nível de **{nivel}**"

```

## Estrutura de Arquivos

O projeto é composto por três arquivos principais:

- `main.py`: Este é o arquivo principal que executa o programa. Inicia o campeonato e interage com o usuário para obter informações sobre os heróis.
- `main_functions.py`: Este arquivo contém todas as funções principais que são necessárias para executar o programa. Isso inclui funções para criar heróis aleatórios, executar o campeonato, e calcular a categoria de um herói.
- `test_main_functions.py`: Este arquivo contém testes unitários para as funções no arquivo `main_functions.py`.

## Como Executar

1. Certifique-se de ter Python 3 instalado em seu sistema.
2. Execute o arquivo `main.py` usando o comando `python main.py`.
3. Siga as instruções na tela para interagir com o programa.

## Funcionalidades

- **Criação Aleatória de Heróis**: Heróis são criados aleatoriamente com nomes e experiência gerados aleatoriamente.
- **Campeonato de Heróis**: Os heróis competem entre si em um campeonato, onde o vencedor de cada partida é determinado com base na experiência.
- **Classificação de Heróis**: Os heróis são classificados em diferentes categorias com base em sua experiência ou saldo de vitórias e derrotas.
- **Interatividade com o Usuário**: O usuário pode visualizar a lista de heróis, obter informações sobre um herói específico e até adicionar um novo herói à liga.
- **Testes Unitários**: Há uma suíte de testes unitários para verificar as funções principais.

## Testes

Para executar os testes unitários, use o comando `python -m unittest test_main_functions.py`.
