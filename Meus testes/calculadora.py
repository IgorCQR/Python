print("CALCULADORA PRA LA DE FODA")
Numero = int(input("Digite um número: "))
Numero2 = int(input("Digite outro número: "))

result1 = Numero + Numero2
result2 = Numero - Numero2
result3 = Numero * Numero2
result4 = Numero / Numero2
result5 = Numero ** Numero2 # MULTIPLICACAO DUPLA (**) é POTENCIA
result6 = Numero % Numero2 # RESTO DA DIVISAO
result7 = Numero ** (1/2) # RAIZ QUADRADA
result8 = Numero2 ** (1/2)

print(f"A soma entre {Numero} e {Numero2} è: {result1}")
print(f"A diferença entre {Numero} e {Numero2} è: {result2}")
print(f"O produto entre {Numero} e {Numero2} è: {result3}")
print(f"A divisão entre {Numero} e {Numero2} è: {round(result4)} (valor arredondado)") #ROUND arredonda o valor
print(f"A potência entre {Numero} (base) e {Numero2} (expoente) è: {result5}")
print(f"O resto da divisão entre {Numero} e {Numero2} è: {result6}")
print(f'A raiz quadrada de {Numero} é {result7:.3f}') # :.f DEFINE NUMERO DE CASAS PÓS VIRGULA
print(f'A raiz quadrada de {Numero2} é {result8:.3f}')