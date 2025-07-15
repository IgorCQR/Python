#print('\033[1;31;42mTESTE\003') # sempre inicia com \033[m ; feche com \033 para o back não preencher toda a tela
# ordem de formatação style(0,1,4,7), color(30 ate 37), background(40 ate 47)

a = 6
b = 9
#print('Os valores são \033[34m{}\033 e \033[35m{}\033'.format(a, b))


# cores com biblioteca
cores = {'limpa': '\033[m',
        'azul': '\033[34m',
        'amarelo': '\033[33m',
        'pretobranco': '\033[7;33m'}

nome = 'igor'
print('Seja bem-vindo, {}{}{}'.format(cores['amarelo'], nome, cores['limpa']))