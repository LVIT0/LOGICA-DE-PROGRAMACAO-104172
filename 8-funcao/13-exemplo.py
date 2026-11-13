import os
os.system('cls')

def metros_para_centimetros(metros):
    centimetros = metros * 100
    return centimetros

metros = float(input('Digite a quantidade de metros: '))
centimetros = metros_para_centimetros(metros)

print(f'{metros} equivalem a {centimetros} centimetros')