s = ''
while s != 'M' and s != 'F':
    s = input('Qual o seu sexo? [M/F] ').upper().strip()
    if s != 'M' and s != 'F':
        print('Opção incorreta! Tente novamente')
print('Sexo registrado com sucesso!')