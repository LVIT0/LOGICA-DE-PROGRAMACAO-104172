import os
os.system('cls')

print('CADASTRAMENTO:')
print() # pular uma linha

login = input('Crie seu login: ')
senha = input('Crie sua senha: ')
input('Clique qualquer tecla para continuar: ')
os.system('cls')

while True:
    login_salvo = input('Digite seu login: ')
    senha_salva = input('Digite sua senha: ')

    if login_salvo == login and senha_salva == senha:
        print('Bem vindo!')
        break

    else:
        print('Senha ou login incorreto!')
        print('Tente novamente: ')
        input('Clique qualquer tecla para continuar: ')
        os.system('cls')