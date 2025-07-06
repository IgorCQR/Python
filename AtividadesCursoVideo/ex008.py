altura = float(input('Informe a altura da parede: '))
largura = float(input('Informe a largura da parede: '))

areap = largura * altura

tinta = areap / 2 

print('A parede tem {}m² e serão necessarios {} litros de tinta'.format(areap,tinta))