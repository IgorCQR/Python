from math import trunc
nume = float(input('Informe um número: '))
nume2 = float(input('Informe outro número: '))

print('O valor informado foi {} e sua porção inteira é {:.0f}'.format(nume, nume))
print(f'O segundo valor é {nume2} e sua porção inteira é {trunc(nume2)}')