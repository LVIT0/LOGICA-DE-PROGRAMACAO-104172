import os
os.system('cls')

def logo_senai():
    print('='*15)
    print(' SENAI BAHIA')
    print('='*15)
    
    
def mostrar_dados(nome, email, telefone):
    print(f'\nNome: {nome}\nE-mail: {email}\nTelefone: {telefone}')
    
logo_senai()
nome = input('\nDigite seu nome: ')

logo_senai()
email = input('Digite seu E-mail: ')

logo_senai()
telefone = int(input('Digite seu telefone: '))

logo_senai()
mostrar_dados(nome, email, telefone)