import os
os.system('cls')

vetor_numeros = []

for i in range(5):
    numero = int(input('Digite um número: '))
    vetor_numeros.append(numero)
print(f'Primeiro número do vetor: {vetor_numeros[0]}')
print(f'Ultimo número do vetor: {vetor_numeros[4]}')