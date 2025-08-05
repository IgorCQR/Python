from random import randint

numero = randint(0,10)
chute = -1
totalchutes = 0

print('Vou pensar em número de 0 ate 10. Tente adivinhar qual número eu pensei')

while numero != chute:
    chute = int(input('Faça seu chute: '))
    totalchutes += 1
print(f'PARABENS! Você acertou. Foram necessárias {totalchutes} tentativas')