import os
os.system('cls')

while True:

    primeira_nota = float(input('Digite a 1ª nota: '))
    segunda_nota = float(input('Digite a 2ª nota: '))
    terceira_nota = float(input('Digite a 3ª nota: '))
    if primeira_nota and segunda_nota and terceira_nota < 0 or primeira_nota and segunda_nota and terceira_nota > 10:
        print('Nota inválida! ')
        print('Tente novamente: ')
    else:
        media = (primeira_nota + segunda_nota + terceira_nota) / 2
        if media > 7:
            print('Aprovado!')
            print(f'Sua média é: {media}')
        elif media > 5:
            print('Recuperação!')
            print(f'Sua média é: {media}')
        else:
            print('Reprovado!')
            print(f'Sua média é: {media}')
        break