# cont = 0 
# for i in range(1,101):
    # cont += i
    # print(cont, end=' ')

# total = 0
# for i in range(2, 1001, 2):
    # total += i
# print(f'Soma dos números pares entre 2 e 1000: {total}')

# quanti = 0
# for i in range(1,7):
#     numero = int(input('Informe um numero: '))
#     if numero == 0:
#         quanti += 1
# print(f'Quantidade de zeros digitados: {quanti}')

# soma = 0
# for i in range(3,100,3):
#     print(i, end=' ')
#     soma += i
# print(f'\nValor total da soma: {soma}')

# somaPar = 0
# somaImpar = 0
# for i in range(1,201):
#     if i % 2 == 0:
#         somaPar += i
#     else:
#         somaImpar += i
# print(f'Soma dos números pares compreendidos entre 1 e 200: {somaPar} \nDos números impares {somaImpar}')

zero = 0
maior = 0
for i in range(1,6):
    numero = int(input('Escreva um numero: '))
    if numero > maior:
        maior = numero
    elif numero < 0:
        zero += 1
print(f'O maior número foi {maior}')
if zero != 0:
    print(f'Foram digitados {zero} numero(s) negativos')