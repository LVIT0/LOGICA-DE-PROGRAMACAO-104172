import os
os.system('cls')

notas = []

def media(notas):
    resultado = sum(notas) / len(notas)
    return resultado



for i in range(3):
    nota = float(input(f'Digite a {i + 1}ª nota: '))
    notas.append(nota)

resultado = media(notas)
print(f'Sua média é: {resultado:.1f}')