import os
os.system('cls')

vetor_notas = []
QUANTIDADE_DE_NOTAS = 4

for i in range(QUANTIDADE_DE_NOTAS):
    vetor_notas.append(float(input(f'Digite a {i + 1}ª nota: ')))
    
media = sum(vetor_notas) / QUANTIDADE_DE_NOTAS
for posicao, notas in enumerate (vetor_notas, start=1):
    print(f'{posicao}ª nota: {notas}')
    maior_nota = max(vetor_notas)
    menor_nota = min(vetor_notas)
print(f'Média: {media}')
if media >= 7:
    print('Aprovado!')
elif media <= 6:
    print('Rcuperação!')
else:
    print('Reprovado!')

print(f'Maior nota: {maior_nota}')
print(f'Menor nota: {menor_nota}')