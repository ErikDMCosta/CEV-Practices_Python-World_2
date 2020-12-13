print("="*40)
print("Indentificador de números primos")
print("="*40)
numero = int(input("Escreva um numero inteiro: "))
total = 0
for contagem in range(1, numero + 1):
    if numero % contagem == 0:
        print('\033[34m', end=' ')
        total += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(contagem), end=' ')
print('\n\033[mO número {} foi divisível {} vezes.'.format(numero, total))
if total == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')