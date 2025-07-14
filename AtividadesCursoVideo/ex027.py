distancia = float(input('Quantos quilometros você irá viajar? '))

if distancia > 200:
    preco = distancia * 0.50
    print(f'Para uma viagem de {distancia} quilometros, você vai pagar R$ {preco:.2f}')
else:
    preco = distancia * 0.45
    print(f'Para uma viagem de {distancia} quilometros, você vai pagar R$ {preco:.2f}')