print('{:=40^}').format('LOJAS BANABARA')

compra = float(input('Valor das compras: R$'))

if compra > 80:
    print('Formas de pagamento: \n [1] à vista dinheiro/cheque \n [2] à vista cartão \n [3] 2x no cartão \n [4] 3x ou mais no cartão ')
    opcao = int(input('Qual é a opção? '))
    if opcao == 1:
        print(f'Pagando à vista você recebe 10% de desconto. Assim sua compra fica em R${compra - (compra / 10):.2f}')
    elif opcao == 2:
        print(f'Pagando à vista no cartão você recebe 5% de desconto. Sua compra fica em R${compra - ((compra / 10) / 2):.2f}')
    elif opcao == 3:
        print(f'Pagando em até 2x no cartão de crédito sua compra fica em 2x de R${compra / 2}')
    elif opcao == 4:
        parcela = int(input('Numero de parcelas: '))
        juros = (compra / 10) * 2
        print(f'Pagando em 3x ou mais no cartão sua compra receberá 20% de juros.')
        print(f'Ao final você irá pagar R${compra + juros:.2f}, com um acréscimo de R${juros:.2f}. O valor parcelado fica em {parcela}x de R${(compra + juros) / parcela:.2f}')
    else:
        print('Opção inválida. Tente novamente')
else:
    print('Pagamento somente à vista!')