import os
os.system('cls')

vetor_notas = []

for i in range(3):
    vetor_notas.append(float(input(f'Digite a {i + 1}ª nota: ')))
    
for i, notas in enumerate (vetor_notas):
    print(f'{i + 1}ª nota: {notas}')