import os
import time
os.system('cls')
print('CONTAGEM REGRESSIVA')

numero = int(input('Digite o número inicial: '))
numerof = int(input('Digite o número final: '))
if numero > numerof:
    for i in range(numero,numerof -1,-1):
        print(i)
        time.sleep(0.5)
elif numero < numerof:
    for i in range(numero,numerof +1,1):
        print(i)
        time.sleep(0.5)
