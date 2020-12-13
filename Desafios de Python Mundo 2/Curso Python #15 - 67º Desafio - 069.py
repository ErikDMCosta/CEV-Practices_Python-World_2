numero = calculo = contador = int
multi = 1
while True:
    print('-' * 30)
    numero = int(input('Quer ver a tabuada de que valor? '))
    print('-' * 30)
    if numero < 0:
        break
    for contador in range(1, 11):
        calculo = numero * multi
        print(f'{numero} X {multi} = {calculo}')
        multi += 1
print('PROGRAMA TABUADA ENCERRADO. Volte Sempre!')
