from datetime import date
anonasc = int(input('Em que ano você nasceu? '))
anoatual = date.today().year
idade = anoatual - anonasc
if idade < 18:
    saldo = 18 - idade
    print('Você nasceu em {} tem {} anos no ano de {} e ainda irá se alistar, falta {} anos para o alistamento.'.format(anonasc,idade,anoatual,saldo))
    ano = anoatual + saldo
    print('Sendo assim seu alistamento será no ano de {}.'.format(ano))
elif idade == 18:
    print('Você nasceu em {} tem {} anos no ano de {} e deve alistar ao quartel IMEDIATAMENTE!.'.format(anonasc,idade,anoatual))
elif idade > 18:
    saldo = idade - 18
    print('Você nasceu em {} tem {} anos no ano de {} prazo passou de {} anos para o alistamento.'.format(anonasc,idade,anoatual,saldo))
    ano = anoatual - saldo
    print('Sendo assim seu alistamento foi no ano de {}.'.format(ano))
else:
    print('Os digitos são inválidos, tente novamente.')