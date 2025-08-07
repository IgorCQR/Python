print('GERADOR DE PA')
print('-=-' *10)

n1 = termo = int(input('Qual o primeiro termo da PA? '))
razao = int(input('Qual a razão dessa PA? '))
contador = 0
escolha = 10
contitermo = 0

while escolha != 0:
    print(f'{termo} -> ', end='')
    termo += razao
    contador += 1
    contitermo += 1
    if contador == escolha:
        print('PAUSA \n')
        escolha = int(input('Quantos termos você quer mostrar a mais? '))
        contador = 0 
print(f'Progressão finalizada com {contitermo} termos, com razão {razao}.')
