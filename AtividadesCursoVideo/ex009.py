produto = float(input('Informe o preço do produto: '))
desconto = int(input('Informe o desconto(%): '))

valodesconto = (produto / 100) * desconto

produto -= desconto

print('Com desconto de {} porcento, o produto terá valor de R${:.2f}'.format(desconto,produto))