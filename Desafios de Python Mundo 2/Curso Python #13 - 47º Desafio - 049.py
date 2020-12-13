numero = int(input('Digite um número inteiro e descubra sua tabuada: '))

for calculo in range(1,11):
    resultado = calculo * numero
    print("O número digitado {} sendo assim {} X {} = {}".format(numero, numero, calculo, resultado))

"""

numero = int(input('Digite um número inteiro e descubra sua tabuada: '))
print('{} x {} = {}'.format(N, 1, N*1))
print('{} x {} = {}'.format(N, 2, N*2))
print('{} x {} = {}'.format(N, 3, N*3))
print('{} x {} = {}'.format(N, 4, N*4))
print('{} x {} = {}'.format(N, 5, N*5))
print('{} x {} = {}'.format(N, 6, N*6))
print('{} x {} = {}'.format(N, 7, N*7))
print('{} x {} = {}'.format(N, 8, N*8))
print('{} x {} = {}'.format(N, 9, N*9))
print('{} x {} = {}'.format(N, 10, N*10))

"""