print('-=-'*10)
print(' '*3, 'FORMADOR DE TRIANGULO')
print('-=-'*10)

l1 = float(input('Informe o primeiro lado: '))
l2 = float(input('Informe o segundo lado: '))
l3 = float(input('Informe o terceiro lado: '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('As retas PODEM formar um triangulo!')
else:
    print('As retas NÃO podem formar um triangulo!')
    