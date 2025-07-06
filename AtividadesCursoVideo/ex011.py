dias = int(input('Por quantos dias você alugou o carro? '))
km = float(input('Quantos quilometros você rodou? '))

total = (dias * 60) + (km * 0.15)

print('Você alugou o carro por {} dias e percorreu {}KM. O valor total é de R$ {:.2f}'.format(dias, km, total))