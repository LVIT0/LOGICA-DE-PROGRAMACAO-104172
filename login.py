import os
os.system

login = input('Digite seu login: ')
senha = input('Digite sua senha: ')

login = 'leandro.vitor'
senha = '2304'

login_esta_correto = login
senha_esta_correto = senha

if login and senha:
    print('Bem vindo Leando')
else:
    print('login ou senha invalido')