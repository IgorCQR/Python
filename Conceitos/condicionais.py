nome = input('Escreva seu nome: ').title()
if nome == 'Gustavo':
    print('Belo nome')
else:
    print('Seu nome é tão normal')
print(f'Boa tarde, {nome}')


n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2

print(f'Sua média é {m:.1f}')
if m >= 6:
    print('Sua média foi boa, parabens!')
else:
    print('Sua média foi ruim!')

print('Parabens' if m >= 6 else 'Estude mais') # condicional simplificada (não recomendada)