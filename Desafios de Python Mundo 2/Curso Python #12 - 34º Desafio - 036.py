valc = float(input('\033[0;34mQual é o valor da casa? R$ '))
sal = float(input('\033[0;34mQual o valor do seu salário? R$ '))
apag = int(input('\033[0;34mEm quantos anos você pretende pagar? '))
prest = valc / (apag * 12)
mini = sal *30 / 100
print('\033[0;36mPara pagar uma casa de R${:.2f} em {} anos'.format(valc, apag), end='.')
# função print deverá receber
# como ultimo parâmetro a
# variável end="separador",
# onde "separador" pode ser
# um espaço, um x ou qualquer string.
print('\033[0;36m O valor da prestação será de R$ {}.'.format(prest))
if prest <= mini:
    print('\033[0;33mO valor da prestação mensal concede ao minimo')
    print('\033[1;32mO seu emprestimo foi concedido com sucesso')
else:
    print('\033[0;33mO seu salario não concede com o minimo para o emprestimo.')
    print('\033[1;31mO Seu emprestimo não foi concedido')

