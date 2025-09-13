print('OPERAÇÃO COM FRAÇÕES')

numerador1 = int(input('Informe o numerador da primeira fração: '))
denominador1 = int(input('Informe o denomiador da primeira fração: '))

numerador2 = int(input('Informe o numerador da segunda fração: '))
denominador2 = int(input('Informe o denominador da segunda fração: '))

if numerador1 == 0 or numerador2 == 0:
    print('Valor do numerador incorreto!')
else:
  opcao = int(input('Opções: \n[1] Soma \n[2] Subtração \n[3] Produto \n[4] Divisão \nEscolha: '))

match(opcao):
   case(1):
      if(denominador1 == denominador2):
         resultado = (numerador1 + numerador2) / denominador1
         print(f"O resultado é {resultado:.2f} ou {numerador2 + numerador1}/{denominador1}")
      else:
         resultado = ((numerador1/denominador1) * denominador2) + ((numerador2/denominador2) * denominador1) 
         print(f"O resultado é {resultado:.2f} ou {((numerador1*denominador2) + (numerador2*denominador1))}/{denominador1*denominador2}")
   case(2):
      if(denominador2 == denominador1):
         resultado = (numerador1 - numerador2) / denominador1
         print(f"O resultado é {resultado:.2f} ou {numerador1 - numerador2}/{denominador1}")
      else:
         resultado = ((numerador1/denominador1) * denominador2) - ((numerador2/denominador2) * denominador1) 
         print(f"O resultado é {resultado:.2f} ou {((numerador1*denominador2) - (numerador2*denominador1))}/{denominador1*denominador2}")
   case(3):
      resultado = (numerador1 * numerador2) / (denominador1 * denominador2)
      print(f"O resultado é {resultado:.2f} ou {numerador1*numerador2}/{denominador1*denominador2}") 
   case(4):
      resultado = (numerador1 * denominador2) / (denominador1 * numerador1)
      print(f"O resultado é {resultado:.2f} ou {numerador1*denominador2}/{denominador1*numerador2}") 
