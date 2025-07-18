from random import choice

print('JO KEN PO')
opcoes = [0, 1, 2]
computador = choice(opcoes)

print('Suas opções: \n [0] PEDRA \n [1] PAPEL \n [2] TESOURA ')

jogador = int(input('Qual é a sua jogada? '))

if computador == jogador:
    print('empate')
