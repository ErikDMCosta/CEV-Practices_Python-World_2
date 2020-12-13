print('-' * 60)
print('                 Sequência de Fibonacci')
print('-' * 60)
contador = int(input('Quantos termos você quer mostrar? '))
n1 = 0
n2 = 1
print('~' * 60)
print('{} → {}'.format(n1, n2), end='')
inicio = 3
while inicio <= contador:
    n3 = n1 + n2
    print(' → {}'.format(n3), end='')
    n1 = n2
    n2 = n3
    inicio += 1
print('  →  FIM!')
print('~' * 60)