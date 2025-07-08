from math import hypot,sqrt

cateOpo = float(input('Informe o valor do cateto oposto: '))
cateAdj = float(input('Informe o valor do cateto adjacente: '))

print('O valor da hipotenusa é {:.2f}'.format(hypot(cateOpo, cateAdj)))

hipotenusa = sqrt(cateOpo**2 + cateAdj**2)
print(f'{hipotenusa:.2f}')