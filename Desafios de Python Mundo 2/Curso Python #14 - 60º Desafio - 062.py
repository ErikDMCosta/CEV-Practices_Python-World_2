print("-="*30)
print("                GERADOR - 10 TERMOS DE UMA P.A - 3.0")
print("-="*30)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} ↠ '.format(termo),  end='')
        termo += razão
        cont += 1
    print('PAUSA')
    mais = int(input('\nQuantos termos você quer mostrar a mais? '))
print('\nProgressão finalizada com {} termos mostrados.'.format(total))