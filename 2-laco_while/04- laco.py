import os
os.system('cls')

soma = 0
QUANTIDADE_NOTAS = 2
for i in range(QUANTIDADE_NOTAS):
    while True:
        nota = float(input(f'Digite a {i + 1}ª nota entre 1 e 10: '))
        if nota < 0 or nota > 10:
            print('Nota inválida, tente novamente! ')
        else:
            soma = soma + nota
            print('A média: ', soma )
            break
        break
