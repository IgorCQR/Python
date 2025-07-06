import math

numero = int(input('Digite um numero: '))
raiz = math.sqrt(numero) #Utilizando a importacao

print(f'A raiz de {numero} é igual a {raiz:.2f}. \nArredondando para cima: {math.ceil(raiz)} \nArredondando para baixo: {math.floor(raiz)}')