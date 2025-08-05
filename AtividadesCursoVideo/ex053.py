s = ''
while s != 'M' and s != 'F':
    s = input('Qual o seu sexo? [M/F] ').upper()
    if s != 'M' and s != 'F':
        print('Opção incorreta! Tente novamente')