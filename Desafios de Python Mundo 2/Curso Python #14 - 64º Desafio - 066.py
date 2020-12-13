print('~*'*40)
print('                         Contador de números e somador')
print('~*'*40)

number = int(input('Escreva algum número: '))

loops = int == 0
soma = 0
resultado = 0

while number != 999:
    print('Escreva outro número, caso deseja encerrar apenas escreva o número 999')
    number = int(input('Seu número: '))
    loops += 1
    soma += number
soma = soma - 991
print('')
print('-*'*40)
print('                  O número de vezes digitadas foi de ', end='')
print(loops)
print('-*'*40)
print('                  A soma dos números digitados foi de ', end='')
print(soma)
print('-*'*40)

