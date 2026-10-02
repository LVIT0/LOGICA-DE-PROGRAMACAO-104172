import os
os.system('cls')

print('Cardápio: ')

print('Código |     Prato          |Valor')
print('     ''1 |     Picanha        |'     'R$ 25,00')
print('     ''2 |     Lasanha        |'     'R$ 20,00')
print('     ''3 |     Stogonoff      |'      'R$ 18,00')
print('     ''4 |     Bife acebolado |'     'R$ 15,00')
print('     ''5 |     Pão com ovo    |'     'R$ 5,00')

prato = int(input('Escolha o seu prato: '))

match prato:

    case 1:
        print('Picanha: R$ 25,00')
    case 2:
        print('Lasanha: R$ 20,00')
    case 3:
        print('Strogonoff: R$ 18,00')
    case 4:
        print('Bife acebolado: R$ 15,00')
    case 5:
        print('Pão com ovo: R$ 5,00')