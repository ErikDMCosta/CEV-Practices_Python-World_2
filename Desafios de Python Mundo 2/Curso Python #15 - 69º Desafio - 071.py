maior18 = 0
contm = 0
mmenor20 = 0
while True:
    print('-' * 30)
    print('     CADASTRE UMA PESSOA')
    print('-' * 30)
    sexo = 'O'
    idade = int(input('Digite sua idade: '))
    if idade > 18:
        maior18 += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite seu sexo: [M/F] ')).strip().upper()[0]

    if sexo == 'M':
        contm += 1

    if sexo == 'F' and idade < 20:
        mmenor20 += 1

    pergunta = ' '
    while pergunta not in 'SN':
        pergunta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

    if pergunta == 'N':
        break
print('============ FIM DO PROGRAMA ============')
print(f'Total de pessoas com mais de 18 anos: {maior18}')
print(f'Ao todo temos {contm} homens cadastrados')
print(f'E temos {mmenor20} mulheres com menos de 20 anos')
