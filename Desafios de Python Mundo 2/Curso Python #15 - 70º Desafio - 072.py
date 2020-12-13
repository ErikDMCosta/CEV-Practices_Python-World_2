soma = contamil = valorbarato = cont = 0
produtobarato = str

print('-' * 35)
print('         LOJA SUPER BARATÃO')

while True:

    print('-' * 35)
    produto = str(input('Nome do Produto: '))
    preco = int(input('Preço: R$ '))

    if preco > 1000:
        contamil += 1
    cont += 1

    if cont == 1:
        valorbarato = preco
        produtobarato = produto
    else:
        if preco < valorbarato:
            valorbarato = preco
            produtobarato = produto

    soma = soma + preco

    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

    if resposta == 'N':
        break

print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi de R${soma:.2f}')
print(f'Temos {contamil} produtos mais de R$1000.00')
print(f'O produto mais barato foi {produtobarato} que custa R${valorbarato:.2f}')
