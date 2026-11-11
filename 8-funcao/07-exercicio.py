import os
os.system('cls')

def mostrar_tabuada(numero):
    for i in range(1,11):
        print(f'{numero} x {i} = {numero * i}')
        
numero = int(input('Digite um numero para tabuada: '))

mostrar_tabuada(numero)