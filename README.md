# Projeto: Fighting Heroes

Este projeto simula um campeonato entre heróis gerados aleatoriamente, onde cada herói possui características distintas como idade, profissão e experiência (XP). A simulação permite a visualização de embates entre os heróis, e ao final, é possível visualizar o ranking dos heróis baseado em suas vitórias e derrotas.

Diferente dos outros projetos, agora os heróis são objetos da classe Hero, com métodos próprios e atributos que são utilizados nas funções, que foram todas adaptadas.

O projeto é baseado no desafio da plataforma Dio que pede o seguinte:

```

## Objetivo:

Crie uma classe genérica que represente um herói de uma aventura e que possua as seguintes propriedades:

- nome
- idade
- tipo (ex: guerreiro, mago, monge, ninja )

além disso, deve ter um método chamado atacar que deve atender os seguientes requisitos:

- exibir a mensagem: "o {tipo} atacou usando {ataque}"
- aonde o {tipo} deve ser concatenando o tipo que está na propriedade da classe
- e no {ataque} deve seguir uma descrição diferente conforme o tipo, seguindo a tabela abaixo:

se mago -> no ataque exibir (usou magia)
se guerreiro -> no ataque exibir (usou espada)
se monge -> no ataque exibir (usou artes marciais)
se ninja -> no ataque exibir (usou shuriken)

## Saída

Ao final deve se exibir uma mensagem:

- "o {tipo} atacou usando {ataque}"
  ex: mago atacou usando magia
  guerreiro atacou usando espada

```

## Estrutura do Projeto

O projeto está estruturado em três arquivos principais:

- `main.py`: Este é o arquivo principal que executa a simulação do campeonato.
- `main_functions.py`: Contém as funções auxiliares necessárias para a simulação.
- `main_classes.py`: Define a classe `Hero`, que representa um herói no campeonato.
- `test_main_functions.py`: Contém testes unitários para validar a lógica implementada nas funções auxiliares.

## Como Executar

1. Certifique-se de ter o Python instalado em sua máquina.
2. Clone o repositório ou faça o download dos arquivos.
3. Abra o terminal e navegue até o diretório onde os arquivos estão localizados.
4. Execute o comando `python main.py` para iniciar a simulação.

## Funcionalidades

- **Criação de Heróis**: Heróis são gerados aleatoriamente com nome, idade, profissão e experiência (XP).
- **Campeonato**: Os heróis competem entre si em um campeonato, onde as vitórias e derrotas são registradas.
- **Classificação**: Ao final, é possível visualizar a classificação dos heróis baseada em suas vitórias e derrotas.
- **Interatividade**: O usuário pode escolher um herói da lista para ver suas informações, ou adicionar um novo herói ao campeonato.

## Testes

Para executar os testes unitários, use o comando `python -m unittest test_main_functions.py`.

## Contribuições

Este é um projeto aberto, e contribuições são bem-vindas. Se você encontrar um bug ou tem uma ideia para uma nova funcionalidade, sinta-se à vontade para abrir uma issue ou enviar um pull request.
