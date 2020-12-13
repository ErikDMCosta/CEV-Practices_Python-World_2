num = int(input('\033[0;35mEscreva um número inteiro:'))
print('''\033[0;30m Escolha uma das bases para conversão:
\033[0;34m[ 1 ] converter para BINÁRIO
\033[0;32m[ 2 ] converter para OCTAL
\033[0;33m[ 3 ] converter para HEXADECIMAL''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('\033[0;34mO número {} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('\033[0;32mO número {} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opcao ==3:
    print('\033[0;33mO número {} convertido para HEXADECIAL é igual a {}'.format(num,hex(num)[2:]))
else:
    print('\033[0;31mO número escolhido não faz referência com uma das três opções.')
