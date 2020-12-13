print('='*50)
print('{:^50}'.format('BANCO CEV'))
print('='*50)

saque = int(input('Que valor você deseja sacar? R$ '))
sacado = saque
base = 50
total = 0
while True:

    if sacado >= base:
        sacado -= base
        total += 1

    else:
        if total > 0:
            print(f'Total de {total} cédula(s) de R${base:.2f}')

        if base == 50:
            base = 20

        elif base == 20:
            base = 10

        elif base == 10:
            base = 1
        total = 0

        if sacado == 0:
            break

print('='*50)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
