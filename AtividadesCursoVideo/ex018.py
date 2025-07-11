nome = input('Nome completo: ').strip() # para eliminar espaços extras

print(nome.upper())
print(nome.lower())

dividido = nome.split()
print(f'Seu primeiro nome é {dividido[0]}, e ele tem {len(dividido[0])} letras')

print(f'Seu nome completo tem {len(''.join(dividido))} letras')

print(f'Seu nome tem ao todo {len(nome) - nome.count(' ')} letras') # outra maneira de eliminar os espaços internos