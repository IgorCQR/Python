print('MULTIPLOS DE 3')

a = 0
for i in range(1,501):
    if i % 2 == 1:
        if i % 3 == 0:
            a += i
            print(f'Os multiplos (impares): {i}')
print(f'Soma dos multiplos: {a}')