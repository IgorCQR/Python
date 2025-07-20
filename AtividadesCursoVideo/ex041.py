from random import choice
from time import sleep

# itens = ('Papel', 'Pedra', 'Tesoura') OUTRA MANEIRA DE FAZER 
# print(itens[1])

print('JOKENPÔ')
opcoes = [0, 1, 2]
computador = choice(opcoes)

print('Suas opções: \n [0] PEDRA \n [1] PAPEL \n [2] TESOURA ')

jogador = int(input('Qual é a sua jogada? '))


if jogador == 1 or jogador == 0 or jogador == 2:
    sleep(1)
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1.2)
    print('PÔ!')
else:
    print('OPÇÃO INEXISTENTE. Tente novamente')

if computador == jogador:
    print('EMPATE')
    if computador == 0:
        print('Ambos jogaram PEDRA')
    elif computador == 1:
        print('Ambos jogaram PAPEL')
    else:
        print('Ambos jogaram TESOURA')
elif computador == 1 and jogador == 0:
    print('VOCÊ PERDEU! O computador jogou PAPEL')
elif computador == 0 and jogador == 1:
    print('VOCÊ GANHOU! O computador jogou PEDRA')
elif computador == 0 and jogador == 2:
    print('VOCÊ PERDEU! O computador jogou PEDRA')
elif computador == 1 and jogador == 2:
    print('VOCÊ GANHOU! O computador jogou PAPEL')
elif computador == 2 and jogador == 1:
    print('VOCÊ PERDEU! O computador jogou TESOURA')
elif computador == 2 and jogador == 0:
    print('VOCÊ GANHOU! O computador jogou TESOURA')