import os 
os.system("cls")

print('\n= Nomes de livros')

vetor_livros = []

for i in range(5):
    livro = input (f"Digite {i+1}º livros: ")
    vetor_livros.append(livro)


print('\n= OS 5 nomes de livros escolhido')


for index in range(5):
        print(f'Livros: {vetor_livros[index]}')

