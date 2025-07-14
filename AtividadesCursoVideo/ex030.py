salario = float(input('Qual o seu salario? '))

if salario > 1250:
    salario += salario / 10 
    print(f'Você recebeu um aumento de 10%! Seu novo salario é de R$ {salario}')
else:
    salario += ((salario / 10) / 2) * 3 
    print(f'Você recebeu um aumento de 15%! Seu novo salario é de R$ {salario}')