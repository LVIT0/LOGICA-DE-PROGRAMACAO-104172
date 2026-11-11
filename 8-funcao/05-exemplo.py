import os
os.system('cls')


def menu():

    print('Código | Descrição')
    print('  1    | Adicionar pessoas')
    print('  2    | Exibir resultados')
    print('  3    | Sair')
    
def mostrar_dados(nome, email, telefone):
        print(f'\nNome: {nome}\nE-mail: {email}\nTelefone: {telefone}')
        
while True:
    menu()
    escolha = input('Escolha: ')
    
    match escolha:
        case'1':
            nome = input('\nDigite seu nome: ')
            email = input('Digite seu E-mail: ')
            telefone = int(input('Digite seu telefone: '))
        case'2':
            os.system('cls')
            mostrar_dados(nome, email, telefone)
        case'3':
            break
        case'_':
            print('Não existe essa função')
            continue