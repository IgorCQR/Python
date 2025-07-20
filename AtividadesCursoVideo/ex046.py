print('Somando numeros pares')

n = 0
total = 0
for i in range(1,7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        total += n
if total != 0:
    print(f'Soma dos pares: {total}')
else:
    print('Não existem números pares')