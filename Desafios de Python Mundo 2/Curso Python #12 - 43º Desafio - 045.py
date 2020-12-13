from random import randint
from time import sleep

print('{:=^40}'.format(' Jokenpô '))
item = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('\033[1;37mEscolha uma opção conforme Nº:\033[m')
print('\033[1;37m[ 0 ] \033[0;33mPedra')
print('\033[1;37m[ 1 ] \033[0;30mPapel')
print('\033[1;37m[ 2 ] \033[0;34mTesoura')

jogador = int(input('\033[1;35mQual é a sua jogada? '))
print('{:=^40}'. format('\033[7;33m !! JO !! \033[m'))
sleep(1)
print('{:=^40}'.format('\033[7;34m!! KEN !!!\033[m'))
sleep(1)
print('{:=^40}'.format('\033[7;35m!!! PO !!!\033[m'))
sleep(1)

print('\033[0;36m-=\033[m'*11)
print('\033[0;35mComputador\033[m\033[0;30m jogou \033[m\033[0;35m{}.\033[m'.format(item[computador]))
print('\033[0;36mJogador\033[m\033[0;30m jogou \033[m\033[0;36m{}.\033[m'.format(item[jogador]))
print('\033[0;36m-=\033[m'*11)

if computador == 0: # Computador jogou Pedra.
    if jogador == 0:
        print('\033[0;30mEMPATE!')
    elif jogador == 1:
        print('\033[0;32mJOGADOR VENCEU!')
    elif jogador == 2:
        print('\033[0;31mCOMPUTADOR VENCEU!')
    else:
        print('\033[1;33mJOGADA INVÁLIDA!')

elif computador == 1: # Computador jogou Papel.
    if jogador == 0:
        print('\033[0;31mCOMPUTADOR VENCEU!')
    elif jogador == 1:
        print('\033[0;30mEMPATE!')
    elif jogador == 2:
        print('\033[0;32mJOGADOR VENCEU!')
    else:
        print('\033[1;33mJOGADA INVÁLIDA!')

elif computador == 2: # Computador jogou Tesoura.
    if jogador == 0:
        print('\033[0;32mJOGADOR VENCEU!')
    elif jogador == 1:
        print('\033[0;31mCOMPUTADOR VENCEU!')
    elif jogador == 2:
        print('\033[0;30mEMPATE!')
    else:
        print('\033[1;33mJOGADA INVÁLIDA!')

else:
    print('\033[1;33;41mDIGITO INVÁLIDO, TENTE NOVAMENTE!')