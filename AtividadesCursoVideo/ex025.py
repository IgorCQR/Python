velocidade = int(input('Em que velocidade você esta? '))

if velocidade <= 80:
    print('Você esta dentro do limite de velocidade!')
else:
    multa = (velocidade - 80) * 7
    print(f'Você ultrapassou o limite de 80km/h e foi multado em R$ {multa:.2f}')