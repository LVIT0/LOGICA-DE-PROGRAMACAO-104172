import os
os.system('cls')

notas = []


def media(notas):
    return sum(notas) / len(notas)

def aprovacao(resultado):
    if resultado >= 7:
        return 'Aprovado'
    else:
        return 'Reprovado'
    

def notas_medias(notas, resultado, situacao):

for i, nota in range(2):
    nota = float(input(f'Digite sua {i + 1}ª nota: '))
    notas.append(nota)

resultado = media(notas)
print(f'Sua média é: {resultado:.2f}')
