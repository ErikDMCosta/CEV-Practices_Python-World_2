num1 = float(input('Qual é o primeiro número? '))
num2 = float(input('Qual é o segunda número? '))

if num1 > num2:
    print('O primeiro é o maior número.')
elif num2 > num1:
    print('O segundo é o maior número.')
elif num1 == num2:
    print('Sendo assim os dois números são iguais.')
else:
    print("O dígito não é correspondentemente válido tente novamente.")