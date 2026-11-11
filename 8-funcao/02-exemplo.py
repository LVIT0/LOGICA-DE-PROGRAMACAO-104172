import os
os.system('cls')

#Criando uma função.

def cabecalho():
    print('\n')
    print('='*15)
    print('  SENAI BAHIA')
    print('='*15)
    return

cabecalho(1)  #Usando função.
nome = input('Digite seu nome: ')


cabecalho()
idade = input('Digite sua idade: ')

cabecalho()
print(f'Nome: {nome}')
print(f'Idade: {idade} anos')