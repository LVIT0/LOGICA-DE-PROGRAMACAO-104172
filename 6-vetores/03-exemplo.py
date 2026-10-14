import os
os.system('cls')

nota = []

for i in range(3):
    nota = float(input('Digite sua nota: '))
    lista_nota.append(nota)

    media = sum(lista_nota) / len(lista_nota)

print(f'Sua média: {media:.2f}')