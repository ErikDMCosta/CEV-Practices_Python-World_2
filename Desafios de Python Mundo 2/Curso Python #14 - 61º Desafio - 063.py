print('-='*20)
print('         SEQUÊNCIA DE FIBONACCI')
print('-='*20)
termo = int(input('\nEscreva o número de termos: '))
contagem = 2
num1 = 0
num2 = 1
print('\n{} ↠ {} ↠ '.format(num1, num2), end='')
while contagem != termo:
    num3 = num1 + num2
    print('{} ↠ '.format(num3), end='')
    num1 = num2
    num2 = num3
    contagem += 1
print('FIM!')
print('\nO programa foi finalizado.')