idade = int(input("Informe sua idade: "))

if idade > 18 or idade == 18:
    print("Você é maior de idade! Já pode ser preso!")
else:
    print("Você ainda é menor de idade! Aproveite enquanto dura")

numero = int(input("Informe um valor: "))

if numero % 2 == 0: # RESTO DA DIVISAO % 
    print("O número {} é par!" .format(numero))
else:
    print("O número {} é impar!" .format(numero))