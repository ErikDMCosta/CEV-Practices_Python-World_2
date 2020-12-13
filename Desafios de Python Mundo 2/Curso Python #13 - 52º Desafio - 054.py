""" Exercício Python #054 - Grupo da Maioridade """

from datetime import date

anoAtual = date.today().year

contador_menor = 0

contador_maior = 0

calculo = int

print('\n\033[1;34mAno de nascimento para saber se e maior ou menor de idade\033[m')

print('\n\033[0;33mSabendo que estamos no ano de\033[m\033[0;35m {}'.format(anoAtual))

for contagem in range(1, 8):

    ano_de_nascimento = int(input('\n\033[0;32mEm que ano a {}º pessoa nasceu? '.format(contagem)))

    calculo = (anoAtual - ano_de_nascimento)

    print('\n\033[m\033[0;30mSua idade é de \033[0;33m{} anos.\033[m'.format(calculo))

    if calculo < 21: # calculo for menor que 21
        contador_menor += 1
        print('\033[0;31mMenor de idade.\033[m')

    else:            # calculo for maior ou igual a 21
        contador_maior += 1
        print('\033[0;34mMaior de idade.\033[m')

print('\n\033[0;31mO número dos que ainda não atingiram a maioridade\033[m\033[0;30m são de {} pessoa(s).'.format(contador_menor))

print('\n\033[0;34mE o número dos que já são de maiores\033[m\033[0;30m são de {} pessoa(s).'.format(contador_maior))



