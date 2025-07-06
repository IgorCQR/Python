salario = float(input('Qual o seu salario? '))
aumento = int(input('Qual o valor do aumento(%)? '))

novaumento = (salario / 100) * aumento
salario += novaumento

print(f'Recebendo um aumento de {aumento}, seu novo salario sera de R$ {salario}')