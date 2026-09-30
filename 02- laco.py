import os
os.system('cls')

while True:
    nota = float(input('Digite a sua nota: '))
    if nota < 0 or nota > 10:
        print('Nota inválida, tente novamente. ')
    else:
        print('A sua nota é: ', nota)
        break