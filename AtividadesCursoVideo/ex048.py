numero = int(input('Informe um número: '))

total = 0
for i in range(1,numero + 1):
    if numero % i == 0:
        total += 1
        print(f'{i}', end=' ')

print('\nO número {} foi dividido {} vezes'.format(numero, total))
if total == 2:
    print('\nÈ primo')
else:
    print('\nNão é primo')