import os
os.system('cls')

lista_nomes = []

for i in range(4):
    nome = input('Digite um nome: ')
    lista_nomes.append(nome)

for i in range(4):
    print(f'Nomes: {lista_nomes[i]}')