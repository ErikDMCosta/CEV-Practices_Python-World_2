"""
Algoritmo:

Escreva ("Contagem regressiva de 10 ! ! !")
laço Contador (10, -1, -1)
    EscrevanaTela(Contador)
    TempoDurma(0.5)
Escreva ("Kbooom boooom boooom")

"""
from time import sleep

print("Contagem regressiva de 10 ! ! !")

for Contador in range(10, -1, -1):
    print(Contador)
    sleep(0.5)
print("Kbooom boooom boooom" * 1000)