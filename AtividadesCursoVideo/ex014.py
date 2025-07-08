from math import cos,sin,tan,radians

angulo = float(input('Valor do angulo: '))
anguloR = radians(angulo)

print('Para um angulo de {} o seno é de {:.2f} em radianos'.format(angulo,sin(anguloR)))
print('Para um angulo de {} o coseno é de {:.2f} em radianos'.format(angulo, cos(anguloR)))
print('Para um angulo de {} a tangente é {:.2f} em radianos'.format(angulo,tan(anguloR)))