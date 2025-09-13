print('OPERAÇÃO COM FRAÇÕES')

numerador1 = int(input('Informe o numerador da primeira fração: '))
denominador1 = int(input('Informe o denomiador da primeira fração: '))

denominador2 = int(input('Informe o denomiador da segunda fração: '))
numerador2 = int(input('Informe o numerador da segunda fração: '))

if numerador1 == 0 or numerador2 == 0:
    print('Valor do numerador incorreto!')
else:
  opcao = int(input('Opções: \n[1] Soma \n[2] Subtração \n[3] Produto \n[4] Divisão \nEscolha: '))

if opcao == 1:
   resultado = ((numerador1/denominador1) * denominador2) + ((numerador2/denominador2) * denominador1) 
elif opcao == 2:
   resultado = ((numerador1/denominador1) * denominador2) - ((numerador2/denominador2) * denominador1) 
elif opcao == 3:
   resultado = (numerador1/denominador1) * (numerador2/denominador2)
elif opcao == 4:
   resultado = (numerador1/denominador1) / (numerador2/denominador2)

print(f'O resultado da operação é {resultado:.2f}')