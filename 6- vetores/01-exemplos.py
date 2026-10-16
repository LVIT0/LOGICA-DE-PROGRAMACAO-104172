import os
os.system("cls")

notas = []

for i in range(3):
    nota = float(input("Digite uma nota: "))
    notas.append(nota)

for i in range(3):
    print(f"Notas: {notas[i]}")