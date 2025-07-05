senha = input('Crie uma senha: ')

if senha.isnumeric() == True:
    print('sua senha é numerica')
else:
    print('sua senha é alfabetica')

print(type(senha))