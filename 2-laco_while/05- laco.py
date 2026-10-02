import os
import time
os.system('cls')

while True:

    login = input('Criar login: ')
    senha = input('Criar senha: ')
    c_login = input('Login: ')
    c_senha = input('Senha: ')
    if login == c_login and senha == c_senha:
        print('Bem vindo! ')
    else:
        print('Seu login ou senha estão incorretos. ')
        time.sleep(2)
        input('Pressione qualquer tecla para continuar: ')
        os.system('cls')