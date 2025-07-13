from random import randint

numero = randint(1,10)
chute = int(input('Adivinhe o numero em que estou pensando (1 ate 10): '))

if chute == numero:
    print('PARABENS! Você acertou o numero')
else: 
    print('Você errou!')