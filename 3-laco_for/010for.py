import os
os.system('cls')

print('ACUMULANDO VALORES EM VARÁVEL.')
soma = 0
numero = 0
for i in range(3):
    numero = int(input(f'\nDigite um número para somar: '))
    soma += numero
print(f'\nValor final da variavel soma: {soma}')