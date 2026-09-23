import os
os.system('cls')

print('MOSTRANDO OS NÚMEROS PARES ENTRE 1 E 10. ')
pares = 0
impares = 0
for i in range(3):
    numero = int(input('Digite um número: '))
    if i % 2 == 0:
        pares = pares + 1
else:
    impares = impares + 1

print(f'Quantidade de pares: {pares}')
print(f'Quantidade de pares: {impares}')