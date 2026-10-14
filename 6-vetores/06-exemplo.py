import os
os.system('cls')

nomes_de_livros = []

for i in range(5):
    nomes_de_livros.append(input(f'Digite o {i + 1}º nome de um livro: '))
    
for i, livros in enumerate (nomes_de_livros):
    print(f'{i} : {livros}')