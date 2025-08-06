# from math import factorial

numero = n = int(input('Informe um número para calcular seu fatorial: '))
fatorial = 1

print(f'Calculando {numero}!: ', end='')
while n != 0:
    print(f'{n}', end='')
    print(' x ' if n > 1 else ' = ', end='')
    fatorial *= n
    n -= 1
print(f'{fatorial}')
       