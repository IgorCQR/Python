print('Sequência de Fibonacci')
print('-=-' * 10)

n1 = int(input('Informe o número inicial: '))
termos = int(input('Informe a quantidade de termos: '))
contador = 0


while contador <= termos:
    n1 = (n1 - 1) + (n1 - 2)
    print(n1)
    contador += 1