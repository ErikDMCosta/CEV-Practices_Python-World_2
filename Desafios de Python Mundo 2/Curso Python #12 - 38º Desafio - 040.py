nota1 = float(input('Qual foi sua primeira nota? '))
nota2 = float(input('Qual foi sua segunda nota? '))
media = (nota1 + nota2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é de {:.1f}'.format(nota1,nota2,media))
if media < 5:
    print('Infelizmente está REPROVADO, tente na próxima.')
elif 7 > media >= 5: # Mesma coisa que ->>> (media >= 5) and (media < 7):
    print('Está em RECUPERAÇÂO, não desista!')
elif media >= 7:
    print('Parabéns! Está APROVADO!')
else:
    print('Os digitos escritos são inválidos, tente novamente')