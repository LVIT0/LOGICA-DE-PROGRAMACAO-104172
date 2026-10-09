import os
import time
os.system('cls')

quantidade_de_familias = 0
lista_de_filhos = []
lista_de_salarios = []

while True:
  
    print(' Código  |   Descrição')
    print('   1     |   Adicionar familiar')
    print('   2     |   Sair e exibir resultados')
    
    escolha = int(input('Escolha: '))

    if escolha == 1:

        salrario = int(input('Qual o salário da família ? R= R$ '))
        lista_de_salarios.append(salrario)
        quantidade_de_familias += 1

        filhos = int(input('Quantos filhos tem na família ? R= '))
        lista_de_filhos.append(filhos)
        continue

    elif escolha == 2:
        if quantidade_de_familias == 0:
            print('Nenhum dado foi registrado na pesquisa.')
            break
        maior_salario = max(lista_de_salarios)
        menor_salairo = min(lista_de_salarios)
        media_salario_da_populacao = sum(lista_de_salarios) / quantidade_de_familias
        media_filhos = sum (lista_de_filhos) / quantidade_de_familias

        print(f'RESULTADO DA PESQUISA ')
        print(f'\nTotal de respostas: {quantidade_de_familias} famílias ')
        print(f'Média do salário da população: R$ {media_salario_da_populacao}')
        print(f'Média do número de filhos: {media_filhos}')
        print(f'Maior salário: R$ {maior_salario}')
        print(f'Menor salário: R$ {menor_salario}')

        break