import time
import os
os.system('cls')

lista = []

while True:
    print('HOSPITAL SAGRADA FAMÍLIA')
    print('1- CADASTRAR')
    print('2- LISTA PACIENTE')
    print('3- ATUALIZAR PACIENTE')
    print('2- EXCLUIR PACIENTE')

    opcao = int(input('Escolha: ')).strip()
    
    match opcao:
        
        case 1:
            print('1- CADASTRAR')
            nome = input('Dgite seu nome: ').strip().upper()
            sobrenome = input('Digite seu sobrenome: ').strip().upper()
            nome_sobrenome = nome + ' ' + sobrenome
            lista.append(nome_sobrenome)
            print('NOME CADASTRADO COM SUCESSO!')
            time.sleep(1)
            os.system('cls')
        case 2:
            os.system('cls')
            print('2- LISTA PACIENTE')
            if len(lista) == 0:
                print('Sem nomes na lista.')
            else:
                for i, cadastro in  enumerate(lista):
                    print(f'{i+1}. {cadastro}')
                    print(f'Total de nomes: {len(lista)}')
        case 3:
            print('3- ATUALIZAR PACIENTE')
            atualizacao = input('Digite: ')
            if atualizacao in lista:
                novo = input('Novo nome: ')
                posicao = lista.index[atualizacao]
                lista[posicao] = novo
                