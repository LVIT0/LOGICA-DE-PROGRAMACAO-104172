import os

os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    print('BANCO COFRINHO')
    print(' ')
    print('1 | VER SALDO ')
    print('2 | DEPOSITAR ')
    print('3 | SACAR ')
    print('4 | VER EXTRATO ')
    print('0 | SAIR ')

def ver_saldo(saldo):
    print(f'Saldo: R$ {saldo}')


def ver_extrato(extrato):
    print('Extrato:')
    if len(extrato) == 0:
        print('Nenhuma movimento realizado. ')
    else:
        for movimento in extrato:
            print(f'{movimento}')


def calculo_soma(saldo, valor):
    valor = float(input('Digite o valor que deseja depositar: '))
    if valor <= 0:
        print('Valor inváldo. ')
        return saldo
    else:
        resultado = saldo + valor
        extrato.append(f'Depósito: R$ {valor:.2f}')
        print('Depósito com sucesso! ')
        print(f'Resultado: R$ {resultado:.2f}')
        return resultado


def calculo_subtracao(saldo, valor):
    valor = float(input('Digite o valor que deseja sacar: '))
    if valor <= 0:
        print('Valor inváldo.')
        return saldo
    elif valor > saldo:
        print('Saldo insuficiente')
        return saldo
    else:
        resultado = saldo - valor
        extrato.append(f'Saque: R$ {valor:.2f}')
        print('Saque com sucesso!')
        print(f'Resultado: R$ {resultado:.2f}')
    return resultado

saldo = 500.0
extrato = []

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    menu()
    opcao = input('\nEscolha a opção: ')

    match opcao:
        case '1':
            ver_saldo(saldo)
            input('Pressione enter para continuar')


        case '2':
            saldo = calculo_soma(saldo, extrato)
            input('Pressione enter para continuar')

        case '3':
            saldo = calculo_subtracao(saldo, extrato)
            input('Pressione enter para continuar')

        case '4':
            ver_extrato(extrato)
            input('Pressione enter para continuar')

        case '0':
            input('Pressione enter para finalizar: ')
            print('Consulta finalizada com sucesso! ')
            break

        case _:
            print('Inválido, tente novamente')
            input('Pressione enter para continuar') 
            continue