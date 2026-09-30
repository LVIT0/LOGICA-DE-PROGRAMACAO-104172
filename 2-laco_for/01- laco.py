import os
os.system('cls')

while True:
    numero = int(input('Digite um número entre 1 e 10: '))
    if numero < 1 or numero > 10:
        print('Número inválido, tente novamente!  ')
    else:
        print('O número está entre 1 e 10. ')
        break #Serve para parar o laço de repetição