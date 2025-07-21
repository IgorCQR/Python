print('PROGRESSAO ARITMETICA')

n1 = int(input('Qual o primeiro termo da PA? '))
razao = int(input('Qual a razão da PA? '))

an = n1 + (10 - 1) * razao
for i in range(n1,an,razao):
    print(i, end=' -> ')
print('FIM')