from datetime import date # pegar a data de hoje

ano = int(input('Informe um ano qualquer (tecle 0 para pegar o ano atual): '))

if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano é bissexto')
else:
    print('O ano não é bissexto')