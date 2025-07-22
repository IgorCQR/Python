from datetime import date
ano = 0
maior = 0
menor = 0

for i in range(1,8):
    ano = int(input('Informe o ano em que a {}ª pessoa nasceu? '.format(i)))
    if date.today().year - ano >= 18:
        maior += 1
    else:
        menor += 1
print(f'{maior} pessoas já atingiram a maioridade')

print(f'{menor} pessoas ainda não atingiram a maioridade')

