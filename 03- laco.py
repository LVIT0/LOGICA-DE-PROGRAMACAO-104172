import os
os.system('cls')


QUANTIDADE_NOTAS = 2
for i in range(QUANTIDADE_NOTAS):
    while True:
        nota = float(input(f'Digite a {i + 1} nota entre 1 e 10: '))
        if nota >= 0 and nota <= 10:
            soma = soma + nota
            print(f'A média é: {nota}')
        else:
            print('Nota inválida, tente novamente ')
            break
        break