import os
os.system('cls')

vetor_notas = []
QUANTIDADE_DE_NOTAS = 2

for i in range(QUANTIDADE_DE_NOTAS):
    vetor_notas.append(float(input(f'Digite a {i + 1}ª nota: ')))
    
media = sum(vetor_notas) / QUANTIDADE_DE_NOTAS

for posicao, notas in enumerate (vetor_notas, start=1):
    print(f'{posicao}ª nota: {notas}')