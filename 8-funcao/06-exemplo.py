import os
os.system('cls')


lista_produtos = []


def mostrar_dados(lista_produtos):
    for i in range(3):
        print(f'{i+1} - {lista_produtos[1]}')
print('= SOLIÇITANDO DADOS =')

def tentativa(lista_produtos):
    for i in range(3):
        produto = input('\nDigite o nome do produto:')
        lista_produtos.append(produto)
        
tentativa(lista_produtos)

mostrar_dados(lista_produtos)