nome = input('Qual é o seu nome: ').capitalize().strip()

#É possivel colocar um IF dentro do outro(ELSE é opcional)
if nome == 'Gustavo' or nome == 'Igor':
    print('Belo nome!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo': # estrutura aninhada é feita com ELIF (coloque quantos forem necessarios)
    print('Seu nome é bem genérico')
else:
    print('Seu nome é chato!')
print(f'Tenha um bom dia, {nome}')