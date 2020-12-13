numero = contagem = soma = 0
while True:
    numero = int(input('Escreva um número: [999 para encerrar] '))
    contagem += 1
    if numero == 999:
        contagem -= 1
        break
    soma += numero
print(f'A soma dos {contagem} valores foi de {soma} !')
