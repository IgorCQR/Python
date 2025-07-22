maior = 0
menor = 0

for i in range(1,6):
    peso = float(input('Peso da {}ª pessoa: '.format(i)))
    if menor == 0:
        menor = peso
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print(f'O maior peso foi de {maior}Kg')
print(f'O menor peso foi de {menor}Kg')