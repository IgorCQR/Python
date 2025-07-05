text = input('Digite qualquer coisa: ')

print(f'è alfabetico? {text.isalpha()}')
print(f'è numerico? {text.isnumeric()}')
print(f'é alfanumerico? {text.isalnum()}')
print(f'possui somente espaços? {text.isspace()}')
print(f'as letras são minusculas? {text.islower()}')
print(f'as letras são maisculas? {text.isupper()}')
print(f'esta capitalizada? {text.istitle()}')