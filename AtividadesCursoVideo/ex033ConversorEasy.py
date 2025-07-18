print('=-='*20)
print('CONVERSOR DE BASES NUMERICAS')
print('=-='*20)

n = int(input('Digite um número: '))
print('Escolha uma das opções: \n 1-Binário \n 2-Octal \n 3-Hexadecimal')
op = int(input('Opção: '))

if op == 1:
    print(f'O número {n} em binário é igual a {bin(n)[2:]}')
elif op == 2:
    print(f'O número {n} em octal é igual a {oct(n)[2:]}')
elif op == 3:
    print(f'O número {n} em hexadecimal é igual a {hex(n)[2:]}')
else:
    print('OPÇÃO INVALIDA')