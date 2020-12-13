soma = 0
contador = 0
for contagem in range(1, 7):
    numero = int(input('Digite o {} valor: '.format(contagem)))
    if numero % 2 == 0:
        soma = soma + numero
        contador = contador + 1
print("Você informou {} números e a soma foi {}".format(contador, soma))
