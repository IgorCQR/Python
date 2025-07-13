# FATIAMENTO (pega uma ou mais letras de uma STRING)
frase = 'Curso em Video Python'
print(frase[9:14]) # de X ate Y
print(frase[0:8:2]) # de X ate Y pulando de 2 em 2
print(frase[:5]) # de 0 ate 5 (inicio vazio = 0)
print(frase[15:]) # fim vazio = final da string
print(frase[9::3]) 
print(frase[::2])


# ANALISE
print(len(frase)) # tamanho da string (caracteres)
print(frase.count('o',0,14)) # conta letras e faz fatiamento (cuidado com maiuscula e minuscula)
print(frase.find('deo')) # encontra a posicao de inicio de uma cadeia de caracter
print(frase.find('Android')) # caracter inexistente RETORNA -1
print('Curso' in frase) # mesmo esquema do FIND, mas retorna True e False


# TRANSFORMACAO
print(frase.replace('Python', 'Android')) # substitui um caracter por outro
print(frase.upper()) # deixa tudo maiusculo
print(frase.lower()) # deixa tudo minusculo
print(frase.capitalize()) # somente a primeira letra fica MAIUSCULA
print(frase.title()) # maiusculo todo o inicio de caracter
frase2 = '   Aprenda Python  '
print(frase2.strip()) # remove espaços desnecessarios (inicio e fim da cadeia)
print(frase2.rstrip()) # a mesma coisa, mas somente á direita
print(frase2.lstrip()) # a mesma coisa, mas somente á esquerda


# DIVISAO
print(frase.split()) # separa a cadeia em uma lista (é possivel mudar a forma de SPLIT)

# JUNCAO
print('-'.join(frase.split())) # junta a lista do SPLIT (junçao fica a seu criterio)

# EXTRA
dividido = frase.split()
print(dividido[0] [2])