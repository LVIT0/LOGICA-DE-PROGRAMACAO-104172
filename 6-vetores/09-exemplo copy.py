import os
os.system('cls')

numero_total = []
numero_pares = []
numero_impar = []
vez = 1
while True:


    numero = float(input(f'Digite o {vez}º número:  '))
    numeros_totais.append(numero)
    vez += 1
    
    if numero == 0:
        print('Número inválido')
        print('Tente digitar um número maior que zero')
        os.system('cls')
        continue
    
    if numero % 2 == 0.0:
        numero_pares.append(numero)
    else:
        numero_impar.append(numero)
        
    print(f'Números pares: {len(numero_pares)}')
    print(f'Números imres: {len(numero_impar)}')