import os
os.system('cls')

numeros = []

while True:
    numeros.append(int(input('Digite um número inteiro: ')))
    soma_positivos = sum([x for x in numeros if x > 0])
    negativos = sum([x for x in numeros if x < 0])

    if len(numeros) == 5:
        print(f'Soma dos números positivos: {soma_positivos}')
        print(f'Quantidade de números negativos: {negativos}')
        break