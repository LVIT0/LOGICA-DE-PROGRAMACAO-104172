import os
os.system('cls')


while True:
    primeira_nota = float(input('Digite a primeira nota: '))
    segunda_nota = float(input('Digite a segunda nota: '))
    if primeira_nota and segunda_nota < 0 or primeira_nota and segunda_nota > 10:
        print('Nota iválida! ')
        print('Tente novamente: ')
    else:
        media = (primeira_nota + segunda_nota) / 2
        print(f'A média é: {media} ')
        break