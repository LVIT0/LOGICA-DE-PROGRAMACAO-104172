import os
import time
os.system('cls')

lista = []

while True:


    print('SÉRIES DENDEZEIROS')
    print('1- GUARDAR SÉRIE')
    print('2- LISTA SÉRIES')
    print('0- SAIR')

    opcao = int(input('Escolha: '))

    match opcao:
        case 1:
            print('1- GUARDAR UMA SÉRIE: ')
            nome = input('Digite o nome da série: ').strip().upper()
            if nome == nome in lista:
                print('Série guardada.')
            else:
                lista.append(nome)
                os.system('cls')
                print('Série guardada com sucesso')
                time.sleep(1)
                os.system('cls')
                
        case 2:
            os.system('cls')
            print('LISTAR SÉRIES')
            if len(lista) == 0:
                print('Sem série guardada')
            else:
                for i, serie in enumerate(lista):
                    print(f'{i+1}. {serie}')
                    print(f'Total de séries: {len(lista)}')
                    
        case 0:
            print('Fim do progama.')
            input('Pressione uma tecla para continuar...')
            break
        case _:
            print('Opção iválida!')
            print('Pressione qualquer tecla para continuar...')