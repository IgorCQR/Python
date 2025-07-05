goss = 50
lonf = 5.5

print("Is this a number:", goss, ". And a other number", lonf) #Important: não concatene string e variavel utilizando +

print(f"Number one: {goss + lonf}") #operações com variaveis utilizando o F


#Exibindo o tipo de variavel
age = 15
name = "Edu"
altura = 1.57
If_student = True

print(type(age))
print(type(name))
print(type(altura))
print(type(If_student))

#convertendo variaveis 
# (float -> int)
altura = int(altura)
print(altura)

#(int -> float)
age = float(age)
print(age)

#(int -> str)
age = str(age)
print(age)

#(str -> bool) a variavel ficará como FALSE apenas se NÃO houver caracter
name = bool(name)
print(name)

#IS vai verificar se a variavel é ou não algo (TRUE or FALSE)
n = input('Informe algo')
print(n.isnumeric())