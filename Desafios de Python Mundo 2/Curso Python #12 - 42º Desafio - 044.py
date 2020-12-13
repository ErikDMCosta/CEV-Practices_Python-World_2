print('{:=^40}'.format(' Lojas Costa '))
preco = float(input('Qual é o preço das compras ? R$ '))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual é a sua opção? '))
if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R$ {:.2f}.'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    tparcel = int(input('Em quantas parcelas deseja fazer? '))
    parcela = total / tparcel
    print('Sua compra será parcelada em {}x de R$ {:.2f} com juros.'.format(tparcel, parcela))
else:
    total = preco
    print('Opção inválida de pagamento. Tente novamente.')
print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final.'.format(preco, total))