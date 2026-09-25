import os
os.system('cls')
QUANTIDADE = 5
impares = 0
pares = 0

for i in range(QUANTIDADE):

    numero = int(input(f'Digite um número: '))
    if numero % 2 == 0:
        pares += 1
    else: impares =impares+ 1
print(f'Os quantidade de números impares é: {impares}')
print(f'Os quantidade de números pares é: {pares}')
