numero = int(input('Informe um número: ').strip())
u = numero % 10
d = numero // 10 % 10
c = numero // 100 % 10
um = numero // 1000 % 10

print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Unidade de milhar: {}'.format(um))


