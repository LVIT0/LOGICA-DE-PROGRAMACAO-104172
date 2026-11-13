import os
os.system('cls')


# função sem retorno e sem parâmetros

def logo_senai():
    os.system('cls')
    print('='*15)
    print('     SENAI')
    print('='*15)

# função sem retorno e com parâmetros

def mostrar_dados(nome, idade):
    print(f'{nome} tem {idade} anos ')

# função sem retorno e sem parâmetros

logo_senai()
print('\n= SOLICITANDO DADOS =')
nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

# função sem retorno e com parâmetros

logo_senai()
print('\n= EXIBINDO DADOS =')

mostrar_dados(nome, idade)