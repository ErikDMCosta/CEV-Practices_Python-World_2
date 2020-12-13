chave = int
soma = 0
contagem = 0

print('-='*20)
print('      SOMADOR DE MULTIPLOS NÚMEROS')
print('-='*20)
chave = int(input('Escreva um número [999 para encerrar]: '))

while chave != 999:
    print('-=' * 20)
    soma += chave
    contagem += 1
    chave = int(input('Escreva um número [999 para encerrar]: '))

print('-/'*20)
print('\nA quantidade de digitos foi de {} números.'.format(contagem))
print('\nE a soma dos números é igual a {} .'.format(soma))
print('')
print('-/'*20)

print('\nEncerrou o programa !')
