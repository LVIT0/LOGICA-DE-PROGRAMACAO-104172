import os
os.system('cls')



def login(matricula, senha):
    return matricula and senha

def salario(salario_base):
    return salario_base

matricula = input('Digite sua matrícula: ')
senha = input('Digite sua senha: ')

while True:

    salario_base = float(input('\nDigite seu salário: '))
    if salario_base <= 0:
        print('Acrescente algum valor positivo.')
        os.system('cls')
        continue
    else:
        break

def v_transporte(vale_transporte):
    return vale_transporte

vale_transporte = input('Você deseja vale transporte?:  ').upper()

def v_refeicao(vale_refeicao):

vale_refeicao =








