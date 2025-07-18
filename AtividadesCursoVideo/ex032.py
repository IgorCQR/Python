print('=-='*20)
print('EMPRESTIMO BANCARIO')
print('=-='*20)

casa = float(input('Qual o valor do imóvel? R$'))
salario = float(input('Qual o seu salário? R$'))
anos = int(input('Em quantos anos deseja realizar o pagamento? '))

parcela = anos * 12
parcelado = casa / parcela
fracaosalario = (salario / 10) * 3

if fracaosalario >= parcelado:
    print(f'Para um imóvel de R$ {casa}, você irá pagar R$ {parcelado:.2f} em {parcela} meses. Considerando o atual salário, o emprestimo esta APROVADO!')
else:
    print(f'Para um imóvel de R$ {casa}, você irá pagar R$ {parcelado:.2f} em {parcela} meses. Considerando o atual salário, o emprestimo esta NEGADO!')