n1 = float(input('Digite um valor: '))
n2 = float(input('Digite outro valor: '))

print('[1] SOMAR \n[2] MULTIPLICAR \n[3] MAIOR \n[4] NOVOS NÙMEROS \n[5] SAIR')

opcao = 0
while opcao != 5:
   opcao = int(input('Escolha uma opção: '))
   if opcao == 1:
      print(f'A soma entre {n1} e {n2} é igual a {n1 + n2}')
   elif opcao == 2:
      print(f'A multiplicação entre {n1} e {n2} é igual a {n1 * n2}')
   elif opcao == 3:
      print(f'O maior número é {max(n1,n2)}')
   elif opcao == 4:
      n1 = float(input('Digite o novo valor: '))
      n2 = float(input('Digite o novo valor: '))
print('FIM DO PROGRAMA')