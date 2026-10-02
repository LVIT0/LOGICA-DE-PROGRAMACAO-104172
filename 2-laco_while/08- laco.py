import os
os.system('cls')


while True:
    nota = float(input('Digite uma nota entre 0 e 10: '))

    if nota < 0 or nota > 10:
        print('Nota inválida. ')
        print('Tente novamente! \n')
    else:
        print(f'Nota: {nota}')
        break