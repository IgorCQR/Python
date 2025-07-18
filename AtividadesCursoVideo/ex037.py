from datetime import date
ano = int(input('Informe o ano de seu nascimento: '))

alistamento = date.today().year - ano

if alistamento < 18:
    print(f'Você não esta na idade para se alistar. Ainda faltam {18 - alistamento} anos. Seu alistamento será em {date.today().year + (18 - alistamento)}')
elif alistamento == 18:
    print('Você esta no momento exato para se alistar')
else:
    print(f'Seu alistamento ocorreu há {alistamento - 18} ano(s), em {date.today().year - (alistamento - 18)}')