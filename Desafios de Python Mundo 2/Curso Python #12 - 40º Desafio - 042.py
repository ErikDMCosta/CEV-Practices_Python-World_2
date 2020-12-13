# Introdução do código
print('\033[0;33m-'*30)
print('\033[0;35mAnalisador de Triângulo - 2.0')
print('\033[0;33m-'*30)
# Variáveis Reais
reta1 = float(input('\033[0;30mQual é o comprimento da primeira reta? '))
reta2 = float(input('\033[0;30mQual é o comprimento da segunda reta? '))
reta3 = float(input('\033[0;30mQual é o comprimento da terceira reta? '))
# if (...):
if reta1 + reta2 > reta3 or reta2 + reta3 > reta1 or reta1 + reta3 > reta2:
    print("\033[0;37mOs números digitados correspondem a de um \033[0;35mTriângulo")
    if reta1 == reta2 == reta3:
        print('\033[0;30mTodos os lados são iguas sendo assim é \033[0;31mEquilátero\033[0;30m.')
    # else if (...):
    elif reta1 == reta2 or reta2 == reta3 or reta3 == reta1 or reta3 == reta2:
        print('\033[0;30mApenas dois lados são iguais sendo assim é \033[0;32mIsósceles\033[0;30m.')
    # else if (...):
    elif reta1 != reta2 != reta3:
        print('\033[0;30mTodos os lados são diferentes sendo assim é \033[0;34mEscaleno\033[0;30m.')
    # else:
    else:
        print('Os números digitados podem não estar de acordo, tente de novo.')
