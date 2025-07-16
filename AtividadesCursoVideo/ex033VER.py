print('CONVERSOR NUMERICO')

n = int(input('Informe um número: '))

base = int(input(('\n 1-binário \n 2-octal \n 3-hexadecimal \n Qual a base de conversão? ')))

b = 0 
if base == 1:
    while n > 0 or n > 1:
        b += n % 2
        n = n // 2
        print(f'Quantidade de 1: {b}') # Funciona parcialmente, precisa ordenar o 1
elif base == 2:
    print()
elif base == 3:
    print()
else:
    print('Opção inválida!')