import os
import time
os.system('cls')
print('CONTAGEM REGRESSIVA')

numero = int(input('Digite o número inicial: '))
numerof = int(input('Digite o número final: '))
if numero >= 2:
    for i in range(numero,numerof +1,-1):
        print(i)
        time.sleep(1)
elif numero <= 1:
    for i in range(numero,numerof +1,1):
        print(i)
        time.sleep(1)