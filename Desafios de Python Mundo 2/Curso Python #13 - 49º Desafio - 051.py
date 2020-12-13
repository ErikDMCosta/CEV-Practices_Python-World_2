print("="*20)
print("10 TERMOS DE UMA P.A - 1.0")
print("="*20)

termo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite razão: "))
decimo = termo + (10 - 1) * razao

for contagem in range(termo, decimo + razao, razao):
    print("{}".format(contagem), end=" ↠ ")
print("Terminou o programa.")