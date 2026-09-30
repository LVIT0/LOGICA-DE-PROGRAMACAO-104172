import os
os.system('cls')

login_salvo = 'leandro'
senha_salva = 2304
tentativas = 1


while True:
    if tentativas <= 3:
        print(f'Tentativa: {tentativas}: ')
        login = input('Digite o login: ')
        senha = input('Digite a senha: ')
        tentativas += 1

        if login == login_salvo and senha == senha_salva:
            print('Bem vindo!')
            break
        else:
            print('Login ou senha inválido. ')
            print('Tente novamente!  ')
            input('Pressione uma tecla para continuar...')
            os.system('cls')
    else:
        print('= FIM =')
        break