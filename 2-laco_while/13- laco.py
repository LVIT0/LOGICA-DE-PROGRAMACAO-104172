import os
os.system('cls')

soma_par = 0
soma_impar = 0
quantidade_par = 0
quantidade_impar = 0

while True:

    valor = float(input('Isira um valor: '))
    if valor == 0:
        break
    elif valor % 2 == 0:
        soma_par += valor
        quantidade_par += 1
    elif valor % 2 == 1:
        soma_impar += valor
        quantidade_impar += 1

soma_geral = soma_par + soma_impar
quantidade_geral = quantidade_par + quantidade_impar
media = soma_par / quantidade_par
media_geral = soma_geral / quantidade_geral
print(f'Média dos valores pares: {media}\nMédia geral: {media_geral}')
print(f'\nQuantidade de números pares: {quantidade_par}\nQuantidade de números impares: {quantidade_impar}: {quantidade_geral}')