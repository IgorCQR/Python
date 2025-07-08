from random import choice # CHOICE só funciona com lista

n1 = input('Primeiro nome: ')
n2 = input('Segundo nome: ')
n3 = input('Terceiro nome: ')
n4 = input('Quarto nome: ')
lista = [n1, n2, n3, n4] 

print(f'O aluno escolhido foi{choice(lista)}')