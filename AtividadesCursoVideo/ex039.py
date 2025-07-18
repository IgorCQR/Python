altura = float(input('Informe sua altura (m): '))
peso = float(input('Informe seu peso (kg): '))

imc = peso / (altura**2)

if imc < 18.5:
    print(f'Seu IMC é {imc:.1f}. Você esta abaixo do peso')
elif 18.5 <= imc < 25:
    print(f'Seu IMC é {imc:.1f}. Você esta no peso ideal')
elif 25 <= imc < 30:
    print(f'Seu IMC é {imc:.1f}. Você esta com sobrepeso')
elif 30 <= imc < 40:
    print(f'Seu IMC é {imc:.1f}. Você esta com obesidade')
elif imc >= 40:
    print(f'Seu IMC é {imc:.1f}. Você esta com obesidade mórbida')