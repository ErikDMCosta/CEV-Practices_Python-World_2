import random

print('-=' * 23)
print("         VAMOS JOGAR PAR OU IMPAR")
print('-=' * 23)

resposta = str
resultado = str
vitorias = 0

while True:
    ram = random.randint(1, 10)

    """ Solicitação dos valores  """
    valor = int(input('Diga um valor: '))
    soma = ram + valor
    parimpar = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]

    """ Testando se é PAR ou IMPAR """
    if soma % 2 == 0:
        resposta = 'PAR'
        resultado = 'P'

    else:
        resposta = 'ÍMPAR'
        resultado = 'I'

    ''' Testando quem errou e acertou '''
    if parimpar == resultado:
        vitorias += 1
        print('-' * 55)
        print(f'\nVocê jogou {valor} e o computador {ram}. Total de {soma} DEU {resposta}.\n')
        print('-' * 55)
        print('Parabéns! Você Venceu da máquina.')
        print('Vamos jogar novamente...')

    elif parimpar != resultado:
        print('-' * 55)
        print(f'\nVocê jogou {valor} e o computador {ram}. Total de {soma} DEU {resposta}.\n')
        print('-' * 55)
        print('               Você Perdeu da máquina.')
        print(f'\n          GAME OVER! Você venceu {vitorias} vezes.')
        print('-' * 55)
        break
