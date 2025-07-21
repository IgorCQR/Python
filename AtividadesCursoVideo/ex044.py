print('MULTIPLOS DE 3 IMPARES')

cont = 0
a = 0
for i in range(3,501,3):
    if i % 2 == 1:
        a += i
        cont += 1
print(f'Soma dos multiplos: {a}')
print(f'Foram somados {cont} numeros')