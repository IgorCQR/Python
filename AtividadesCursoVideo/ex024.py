from random import randint
from time import sleep

print('-'*37)
print('Vou pensar em um número entre 1 e 10!')
print('-'*37)

numero = randint(1,10)
chute = int(input('Em que número estou pensando? '))
print('PROCESSANDO...')
sleep(2) # faz o computador "esperar"

if chute == numero:
    print('PARABENS! Você acertou o numero')
else: 
    print(f'Você errou! Eu pensei no número {numero}')