import random

print('\n\033[1;32m==================== <-> GAME <-> =====================\033[m')

print('\n\033[1;33m=============== </> TENTE ADIVINHAR </> ===============\033[m')

número = int
ram = random.randint(0, 10)
vezes = 0

while ram != número:

    número = int(input('\n\033[1;30mDigite um numero inteiro de 0 a 10: '))
    vezes += +1

    if número == ram:
        print('\n\033[1;32mVocê venceu!\033[m')
        print('\n\033[0;30mAcertou o numero aleatório sorteado pela máquina.\033[m\033[1;32m PARABÉNS!\033[m')
        print('\n\033[0;30mO número de tentativas foi de \033[0;33m{}\033[m\033[0;30m veze(s).\033[m'.format(vezes))
        break

    if número < ram:
        print('\n\033[0;30mMais... Tente mais uma vez.\033[m')

    if número > ram:
        print('\n\033[0;30mMenos... Tente mais uma vez.\033[m')

    else:
        print('\n\033[1;31m=====================================================================\033[m')
        print('\n\033[1;31mO computador venceu !\033[m')
        print('\n\033[0;30mErrou o numero sorteado pela máquina.\033[m\033[1;31m TENTE DENOVO!\033[m')
        print('\n\033[0;30mO número de tentativas foi de \033[0;33m{}\033[m\033[0;30m veze(s).\033[m'.format(vezes))
        print('\n\033[1;31m=====================================================================\033[m')