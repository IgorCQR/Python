n1 = float(input('Informe sua primeira nota: '))
n2 = float(input('Informe a segunda nota: '))

media = (n1 + n2) / 2

if media < 5:
    print(f'Com notas {n1} e {n2} você obtem média {media:.1f}. REPROVADO')
elif media > 5 and media <= 6.9:
    print(f'Com notas {n1} e {n2} você obtem média {media:.1f}. RECUPERAÇÃO')
else:
    print(f'Com notas {n1} e {n2} você obtem média {media:.1f}. APROVADO')