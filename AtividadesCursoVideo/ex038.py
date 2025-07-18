l1 = float(input('Lado 1 do triangulo: '))
l2 = float(input('Lado 2 do triangulo: '))
l3 = float(input('Lado 3 do triangulo: '))

if l1 < l3 + l2 and l2 < l1 + l3 and l3 < l2 + l1:
    print('É possivel formar um triangulo!')
    if l1 == l2 == l3:
        print('Esse triangulo é EQUILATERO')
    elif l1 != l2 != l3 != l1:
        print('O triangulo é ESCALENO')
    else:
        print('O triangulo é ISÓSCELES')
else: 
    print('Não é possivel formar um triangulo!')

