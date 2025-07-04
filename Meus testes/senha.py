senha = input("Digite a senha: ")

while senha != "app123":
    print("senha incorreta!")
    senha = input("Digite a senha: ")
    if senha == "app123":
        print("ACERTOU!")
        break