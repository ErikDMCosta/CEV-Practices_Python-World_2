media = soma = loops = maior = menor = 0
resposta = 'S'

while resposta in 'Ss':

    number = int(input('Escreva algum número: '))
    soma += number
    loops += 1
    if loops == 1:
        maior = menor = number
    else:
        if number > maior:
            maior = number
        if number < menor:
            menor = number

    resposta = str(input('Deseja continuar? [SIM/NÃO] ')).upper().strip()[0]

''' Aqui pra baixo irei escrever fora do While'''

media = soma / loops
print('Foram digitados {} e a soma dos números são de {} e a média entre os números foi de {} . '.format(loops, soma, media))
print('O maior valor foi de {} e o menor valor foi de {}.'.format(maior, menor))

print('Programa encerrado.')
