peso = float(input('Qual é o seu peso em Kilogramas (kg)? '))
altura = float(input('Qual é a sua altura em metros (m) ? '))
IMC = (peso / (altura ** 2))
print('Seu IMC (Índice de Massa Corporal) é de {:.1f}.'.format(IMC))
if IMC < 18.5:
    print('\033[0;30mA sua situação se enquadra \033[0;37mAbaixo do peso.')
elif (IMC >= 18.5) and (IMC < 25):
    print('\033[0;30mA sua situação se enquadra \033[0;32mPeso Ideal.')
elif (IMC >= 25) and (IMC < 30):
    print('\033[0;30mA sua situação se enquadra \033[0;35mSobrepeso.')
elif (IMC >= 30) and (IMC < 40):
    print('\033[0;30mA sua situação se enquadra \033[0;33mObesidade.')
elif IMC >= 40:
    print('\033[0;30mA sua situação se enquadra \033[0;31mObesidade Mórbida.')
else:
    print('\033[0;30mO digito não é válido, veja se não esqueceu ponto ou vírgula, tente novamente.')