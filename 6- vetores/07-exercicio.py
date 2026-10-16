import os
os.system("cls")

print('\n= INSERINDO NÚMEROS NO VETOR =')

vetor_notas = []
QUANTIDADES_NOTAS = 3

for i in range(QUANTIDADES_NOTAS):
    nota= int(input(f"Digite a {i+1}º Nota: "))
    vetor_notas.append(nota)

media = sum(vetor_notas) / QUANTIDADES_NOTAS

print("\n= EXIBINDO NOTAS")
for index, nota in enumerate(QUANTIDADES_NOTAS):
    print(f"Notas: {vetor_notas[index]}")