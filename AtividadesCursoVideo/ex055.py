n1 = float(input('Digite um valor: '))
n2 = float(input('Digite outro valor: '))

print('[1] SOMAR \n[2] MULTIPLICAR \n[3] MAIOR \n[4] NOVOS NÙMEROS \n[5] SAIR')

opcao = 0
while opcao != 5:
   opcao = int(input('Escolha uma opção: '))
   if opcao == 1:
      print(f'A soma entre {n1} e {n2} é igual a {n1 + n2}')
      print('=-=' * 15)
   elif opcao == 2:
      print(f'A multiplicação entre {n1} e {n2} é igual a {n1 * n2}')
      print('=-=' * 15)
   elif opcao == 3:
      print(f'Entre {n1} e {n2}, o maior número é {max(n1,n2)}')
      print('=-=' * 15)
   elif opcao == 4:
      n1 = float(input('Digite o novo valor: '))
      n2 = float(input('Digite o novo valor: '))
      print('[1] SOMAR \n[2] MULTIPLICAR \n[3] MAIOR \n[4] NOVOS NÙMEROS \n[5] SAIR')
   else:
      print('OPÇÃO INEXISTENTE. TENTE NOVAMENTE')
      print('=-=' * 15)
      print('[1] SOMAR \n[2] MULTIPLICAR \n[3] MAIOR \n[4] NOVOS NÙMEROS \n[5] SAIR')
print('FIM DO PROGRAMA')