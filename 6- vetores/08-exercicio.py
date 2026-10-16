import os
os.system("cls")

notas = []

for i in range(4):
    nota = float(input(f"Digite sua {i+1}º nota "))
    notas.append(nota)

media = sum(notas) / len(notas)

if media >= 7:
    print("Aprovado")
elif media >= 5:
    print("Recuperação")
else:
    print("Reprovado")

print("\n--- RESULTADOS ---")
print(f"Média aritmética: {media:.2f}")