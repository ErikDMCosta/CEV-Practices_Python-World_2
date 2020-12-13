nome = str(input('Qual é o nome ? '))
if nome == 'Erik':
    print('Seu nome é bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
else:
    print('Seu nome é bem normal.')
print("Tenha um bom dia, {}!".format(nome))