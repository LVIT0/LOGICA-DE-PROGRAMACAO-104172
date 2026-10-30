import os
os.system('cls')

vetor_notas = []

for i in range(3):
    nota = float(input('Digite uma nota: '))
    vetor_notas.append(nota) #Inserindo a nota no vetor de notas

for i in range(3):
    print(f'Nota: {vetor_notas[i]}')