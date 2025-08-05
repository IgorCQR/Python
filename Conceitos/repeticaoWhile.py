# c = 1
# while c < 10:
#     print(c)
#     c = c + 1

# n = 'S'
# while n == 'S':       #Repete uma ação enquanto uma determinada condicao for verdadeira ou falsa
#     c = int(input('Digite um valor: '))
#     n = input('Quer continuar? [S/N] ').upper()

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um numero: '))
    if n != 0: # não incluir o numero 0
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Foram digitados {} numeros pares e {} numeros impares'.format(par, impar))