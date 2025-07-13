frase = input('Digite uma frase: ').strip().lower()

print(f'Número de letras A: {frase.count('a')}')
print(f'Primeira posição da letra A: {frase.find('a')}')
print(f'Ultima posição da letra A: {frase.rfind('a')}') # R: 'le' a cadeia da direita pra esquerda