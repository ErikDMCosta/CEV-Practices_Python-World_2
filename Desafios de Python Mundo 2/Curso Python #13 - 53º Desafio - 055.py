maior = 0
menor = 0
for contagem in range(1,6):
    peso = float(input('\n\033[0;30mQual é o peso da {}º pessoa? '.format(contagem)))
    if contagem == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('\n\033[0;31mO maior peso lido foi de {}Kg.'.format(maior))
print('\n\033[0;34mO menor peso lido foi de {}Kg.'.format(menor))




