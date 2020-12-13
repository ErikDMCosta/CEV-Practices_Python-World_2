numero = int(input('\nQual número deseja saber o fatorial? '))
count = numero
resultado = 1

print('\nCalculando {}! = '.format(numero), end='')
while count > 0:
    print('{}'.format(count), end='')
    print(' x ' if count > 1 else ' = ', end='')
    resultado *= count
    count -= 1
print('{}'.format(resultado))
