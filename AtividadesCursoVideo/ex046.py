print('Somando numeros pares')

cont = 0
n = 0
total = 0
for i in range(1,7):
    n = int(input('Digite o {}° número: '.format(i)))
    if n % 2 == 0:
        total += n
        cont += 1
if total != 0:
    print(f'Números pares contados: {cont}. Soma dos pares: {total}')
else:
    print('Não existem números pares')