from datetime import date
print('-'*32)
print('Confederação Nacional de Natação')
print('-'*32)
anonasc = int(input('Em que ano você nasceu? '))
anoatual = date.today().year
idade = anoatual - anonasc
print('Sua idade é de {} anos.'.format(idade))
if (idade >= 3) and (idade <= 9):
    print('Se enquadra na categoria MIRIM.')
elif (idade >= 10) and (idade <= 14):
    print('Se enquadra na categoria INFANTIL.')
elif (idade >= 15) and (idade <= 19):
    print('Se enquadra na categoria JUNIOR.')
elif (idade >= 20) and (idade <= 25):
    print('Se enquadra na categoria SÊNIOR.')
elif idade > 25:
    print('Se enquadra na categoria MASTER.')
else:
    print('O digito não se enquadra a uma idade mínima, tente novamente.')