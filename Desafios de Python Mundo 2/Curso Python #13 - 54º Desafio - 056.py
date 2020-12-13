somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = 0
mulhernova = 0

# A média de idade do grupo de quatro pessoas
# O homem mais velho e como se chama
# Quantas mulheres tem menos de 20 anos

for pessoas in range(1, 5):

    print('\n------- {}º PESSOA -------'.format(pessoas))

    nome = str(input('\nQual é o seu nome? ')).strip()
    idade = int(input('\nQual é sua idade? '))
    sexo = str(input('\nPor favor, digite [M] para Masculino ou [F] para Feminino. ')).strip()

    somaidade += idade

    if pessoas == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome

    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome

    if sexo in 'Ff' and idade < 20:
        mulhernova += +1

mediaidade = somaidade / 4

print('\nA média de idade do grupo de quatro pessoas são {} anos.'.format(mediaidade))

print('\nO homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem,nomevelho))

print('\nA quantidade de mulheres menores de 20 anos são de {} mulheres.'.format(mulhernova))
