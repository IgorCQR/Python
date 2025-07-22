idade = 0
media = 0
mulhervinte = 0
velho = ''
maior = 0

for i in range(1,5):
    print(f'{'-'*5} {i}ª PESSOA {'-'*5}')
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').upper().strip()

    media += idade / 4

    if sexo == 'F' and idade < 20:
        mulhervinte += 1
    if sexo == 'M' and idade > maior:
        maior = idade
        velho = nome

print(f'A idade média do grupo é de {media:.1f} anos')
print(f'Há no grupo {mulhervinte} mulher(es) abaixo dos 20 anos')
print(f'O homem mais velho do grupo tem {maior} anos e se chama {velho}')