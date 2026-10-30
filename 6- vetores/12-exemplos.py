import os
os.system('cls')

vetor_pratos = []
vetor_precos = []

while True:

    print('Código |    Prato            |  Valor')
    print('Código |    Picanha          |  R$ 25,00')
    print('Código |    Lasanha          |  R$ 20,00')
    print('Código |    Strogonoff       |  R$ 18,00')
    print('Código |    Bife Acebolado   |  R$ 15,00')
    print('Código |    Pão com ovo      |  R$5,00')


    opcao = input('Escolha seu prato: ')

    match opcao:
        case 1:
            prato = 'Picanha'
            preco = 25
        case 2:
            prato = 'Lasanha'
            preco = 20
        case 3:
            prato = 'Strogonoff'
            preco = 18
        case 4:
            prato = 'Bife acebolado'
            preco = 15
        case 5:
            prato = 'Pão com ovo'
            preco = 5
        case _:
            print('Opção iválida. \nTente novamente...')
    if opcao >= 1 and opcao <= 5:
        vetor_pratos.append(prato)
        vetor_precos.append(preco)
        continuar = input('Deseja escolher outro prato? \nResponda S ou N: ').upper()
        if continuar == 'N':
            break
        os.system('cls')
    if sum(vetor_precos) == 0:
        print('\nNenhum prato selecionado.')
    else:
        print('\nPratos escolhidos ')
        for i, prato in enumerate(vetor_pratos, start=1):
            print(f'{i}º prato: {prato}')

        print(f'\nTotal: R$ {sum(vetor_precos)}')

        print('\nVolte sempre!')