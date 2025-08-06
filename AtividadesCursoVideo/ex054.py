from random import randint

numero = randint(0,10)
chute = -1
totalchutes = 0

print('Pensei em número de 0 a 10. Tente adivinhar qual número eu pensei')

while numero != chute:
    chute = int(input('Dê seu chute: '))
    # if chute > numero:
    #     print('Um pouco mais baixo')
    # else:
    #     print('Um pouco mais alto')
    totalchutes += 1
print(f'PARABENS! Você acertou. Foram necessárias {totalchutes} tentativas')