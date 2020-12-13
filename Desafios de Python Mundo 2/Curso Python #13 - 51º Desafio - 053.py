# Código com base a video aula.

print('\033[1;36m=\033[m' * 10 + '\033[1;32m Descubra se sua frase é palíndromo \033[m' + '\033[1;36m=\033[m' * 10)

frase = str(input('\n\033[0;36mEscreva sua frase: \033[m'))


palavras = frase.split()

junto = ''.join(palavras)

inverso = ''


for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('\n\033[0;34mAs frases escritas correspondem a um\033[0;35m palíndromo \033[0;34m ! \033[m')
    print('\n\033[0;30mA escrita invertida fica assim: \033[33m{}'.format(inverso))
else:
    print('\n\033[0;31mAs frases escritas não correspondem a um\033[0;35m palíndromo \033[0;34m ! \033[m')
    print('\n\033[0;30mA escrita invertida fica assim: \033[33m{}'.format(inverso))





# Abaixo eu mesmo escrevi o código, porém sem utilizar um FOR como na Video-Aula.

"""


print('\033[1;36m=\033[m' * 10 + '\033[1;32m Descubra se sua frase é palíndromo \033[m' + '\033[1;36m=\033[m' * 10)

frase = str(input('\n\033[0;36mEscreva sua frase: \033[m'))


sem_espaco = frase.replace(' ', '')

maiusculo = sem_espaco.upper()

inverso = (maiusculo[::-1])


if inverso == maiusculo:
    print('\n\033[0;34mAs frases escritas correspondem a um\033[0;35m palíndromo \033[0;34m ! \033[m')
    print('\n\033[0;30mA escrita invertida fica assim: \033[33m{}'.format(inverso))
else:
    print('\n\033[0;31mAs frases escritas não correspondem a um\033[0;35m palíndromo \033[0;34m ! \033[m')
    print('\n\033[0;30mA escrita invertida fica assim: \033[33m{}'.format(inverso))


"""