print('CONVERSOR NUMERICO')

n = int(input('Informe um número: '))

print('Escolha uma opção: \n 1-binário \n 2-octal \n 3-hexadecimal')
base = int(input(('Qual a base de conversão? ')))

contador = 0
b = 0 
if base == 1:
    while n > 0 or n > 1:
        b = n % 2
        n = n // 2
        print(f'{b}', end='') # Funciona parcialmente, precisa ordenar o binario
elif base == 2:
    print()
elif base == 3:
    print()
else:
    print('Opção inválida!')