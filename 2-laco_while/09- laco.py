import os
os.system('cls')

print('1- BAURIVIS:                R$7,00')
print('2- COXINHA DE FRANGO:       R$5,00')
print('3- PASTEL DE FRANGO:        R$6,00')
print('4- EMPADA DOCE:             R$4,00')
print('5- GELADINHO DE YAKULT:     R$3,00')
print() # pular uma linha



while True:

    produto = int(input('Qual você deseja: '))

    if produto < 1 or produto > 5:

        print('Pedido iválido! ')
        print('Tente novamente: ')

    else:
        match produto:
            case 1:
                print('Baurivis:  R$7,00')
            case 2:
                print('Coxinha de frango:  R$5,00')
            case 3:
                print('Pastel de frango:  R$6,00')
            case 4:
                print('Emapda doce:  R$4,00')
            case 5:
                print('Geladinho de yakult:  R$3,00')
        break