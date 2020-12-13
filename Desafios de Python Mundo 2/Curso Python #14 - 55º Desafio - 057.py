sexo = str
M = '\033[1;34mMasculino'
F = '\033[1;35mFeminino'

print('\n\033[1;33m=============== Validação de dados ===============\033[m')

print('\n\033[0;32mConsidere [M] para Masculino ou [F] para Feminino.\033[m')

while sexo == M or F:

    sexo = str(input('\n\033[1;30mQual é o seu sexo?\033[m \033[1;30m[\033[m\033[1;34mM\033[m \033[1;30mou\033[m \033[1;35mF\033[m\033[1;30m]\033[m ')).upper()

    if sexo in 'M':
        sexo = M
        print('\n\033[0;30mSeu sexo é \033[m{}\033[0;30m.\033[m'.format(sexo))
        break

    if sexo in 'F':
        sexo = F
        print('\n\033[0;30mSeu sexo é \033[0;30m{}.\033[m'.format(sexo))
        break

    else:
        print('\n\033[1;31mO valor digitado não corresponde com o que foi pedido acima, tente novamente.')

