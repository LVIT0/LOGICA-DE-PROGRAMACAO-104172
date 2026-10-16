import os
os.system("cls")

numeros = []

for i in range(5):
    num = float(input(f"Digite seu {i+1}º Número: "))
    numeros.append(num)

menor_numero = min(numeros)
maior_numero = max(numeros)

print(f'Numeros: {numeros}')




print(f"Maior número: {maior_numero}")
print(f"Menor número: {menor_numero}")