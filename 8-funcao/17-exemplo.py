import os
os.system('cls')


def media(notas):
    return sum(notas) / len(notas)

def aprovacao(resultado):
    if resultado >= 7:
        return 'Aprovado'
    else:
        return 'Reprovado'

def notas_medias(notas, resultado, situacao):
    print('\n--- Resultados ---')
    for i, nota in enumerate(notas, start=1):
        print(f'{i}ª nota: {nota:.1f}')
    print(f'Sua média é: {resultado}')
    print(f'Situação: {aprovacao}')


notas = []

for i in range(2):
    while True:
        nota = float(input(f'Digite sua {i + 1}ª nota: '))
        if 0 <= nota <= 10:
            notas.append(nota)
            break
        else:
            print('Valor inválido ')

resultado = media(notas)
situacao = aprovacao(resultado)

print(f'Situação: {situacao}')
print(f'Resultado: {resultado}')