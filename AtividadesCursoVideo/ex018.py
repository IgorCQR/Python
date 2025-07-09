nome = input('Nome completo: ')

print(nome.upper())
print(nome.lower())

dividido = nome.split()
print(f'Tamanho do primeiro nome: {len(dividido[0])}')

print(f'Tamanho do nome sem os espaços: {len(''.join(dividido))}')
