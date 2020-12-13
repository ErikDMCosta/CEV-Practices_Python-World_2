from time import sleep

valor1 = int(input('\nQual é o 1º valor numérico? '))
valor2 = int(input('\nQual é o 2º valor numérico? '))
descicao = 0

while descicao != 5: # problema de estruturação do código
    print('''\n
        Menu de opções

        [ 1 ] Somar
        [ 2 ] Multiplicar
        [ 3 ] Maior
        [ 4 ] Novos números
        [ 5 ] Sair do programa ''')
    descicao = int(input('\nDentro das opções acima, qual é a sua escolha? '))

    if descicao == 1:
        soma = valor1 + valor2
        print('A soma entre {} e {} é igual a {} .'.format(valor1, valor2, soma))
    elif descicao == 2:
        multplicação = valor1 * valor2
        print('A multplicação entre {} e {} é igual a {} .'.format(valor1, valor2, multplicação))
    elif descicao == 3:
        if valor1 > valor2:
            print('Entre os valores {} e {} o maior valor é o de {} .'.format(valor1, valor2, valor1))
        else:
            print('Entre os valores {} e {} o maior valor é o de {} .'.format(valor1, valor2, valor2))
    elif descicao == 4:
        print('Informe os números novamente: ')
        valor1 = int(input('\nQual é o 1º valor numérico? '))
        valor2 = int(input('\nQual é o 2º valor numérico? '))
    elif descicao == 5:
        print('Finalizando...')
    else:
        print('Opção ínvalida. Tente novamente')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa! Volte sempre!')