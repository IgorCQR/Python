n = int(input('Digite um numero: '))

print('A TABUADA DO {}: '.format(n))
for i in range(1,11):
    print(f'{n} X {i:2} = {n*i}')