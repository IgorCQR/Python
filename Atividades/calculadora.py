print("CALCULADORA PRA LA DE FODA")
Numero = int(input("Digite um número: "))
Numero2 = int(input("Digite outro número: "))

result1 = Numero + Numero2
result2 = Numero - Numero2
result3 = Numero * Numero2
result4 = Numero / Numero2
result5 = Numero ** Numero2 # MULTIPLICACAO DUPLA (**) é POTENCIA
result6 = Numero % Numero2 # RESTO DA DIVISAO

print(f"A soma entre {Numero} e {Numero2} è: {result1}")
print(f"A diferença entre {Numero} e {Numero2} è: {result2}")
print(f"O produto entre {Numero} e {Numero2} è: {result3}")
print(f"A divisão entre {Numero} e {Numero2} è: {round(result4)} (valor arredondado)") #ROUND arredonda o valor
print(f"A potência entre {Numero} (base) e {Numero2} (expoente) è: {result5}")
print(f"O resto da divisão entre {Numero} e {Numero2} è: {result6}")
