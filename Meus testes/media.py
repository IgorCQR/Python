print("MEDIA ARITIMETICA")

name = input("Informe seu nome: ")
idade = int(input("Informe sua idade: "))
nota1 = float(input("Qual sua primeira nota? "))
nota2 = float(input("Qual sua segunda nota? "))
nota3 = float(input("Qual sua terceira nota? "))

media = (nota1 + nota2 + nota3) / 3

print(f"Nome: {name}")
print(f"Idade: {idade}")
print(f"Notas: {nota1, nota2, nota3}")
print(f"Média: {media:.1f}")

if media >= 6:
    print("VOCÊ PASSOU!")
else:
    print("VOCÊ NÃO PASSOU!")
