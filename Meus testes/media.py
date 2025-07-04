print("MEDIA ARITIMETICA")

name = input("Informe seu nome: ")
idade = int(input("Informe sua idade: "))
nota1 = int(input("Qual sua primeira nota? "))
nota2 = int(input("Qual sua segunda nota? "))
nota3 = int(input("Qual sua terceira nota? "))

media = (nota1 + nota2 + nota3) / 3

print(f"Nome: {name}")
print(f"Idade: {idade}")
print(f"Notas: {nota1, nota2, nota3}")
print(f"Média: {media}")

if media > 6 or media == 6:
    print("VOCÊ PASSOU!")
else:
    print("VOCÊ NÃO PASSOU!")
