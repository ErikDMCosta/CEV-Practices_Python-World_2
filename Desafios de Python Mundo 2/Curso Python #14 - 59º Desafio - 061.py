print("="*20)
print("10 TERMOS DE UMA P.A - 2.0")
print("="*20)

contagem = 0

termo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite razão: "))

while contagem != 10:
    print("{}".format(termo), end=" ↠ ")
    termo += razao
    contagem += 1
print("Terminou o programa.")
