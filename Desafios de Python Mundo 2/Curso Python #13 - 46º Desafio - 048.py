soma = 0
contagem = 0
for calculo in range(1, 501, 2):
        if calculo % 3 == 0:
            soma = soma + calculo
            contagem = contagem + 1
print("A soma de todos os {} valores solicitados {}".format(contagem,soma))
