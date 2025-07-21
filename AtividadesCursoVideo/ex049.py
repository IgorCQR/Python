frase = input('Digite uma frase: ').upper().split()
junto = ''.join(frase)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('Temos um palindromo')
else:
    print('A frase digitada não é um palindromo')
#  inverso = junto[::-1] (outra maneira de inverter)