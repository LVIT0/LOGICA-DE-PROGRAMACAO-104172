import os
import time
os.system('cls')

idade_list = []
sexo_list = []
salario_list = []
mulheres_maior_cinco_mil = 0
soma_salario = 0

while True:
    print('Código  | Descrição')
    print('  1     | Adicionar pessoa')
    print('  2     | Exibir resultados')
    print('  3     | Sair')

    escolha = float(input('\nEscolha: '))
    if escolha == 1:
        idade + int(input('Digite sua idade:'))
        idade_list.append(idade)
        print('M | Masculino')
        print('F | Feminino')
        sexo = input('Digite seu sexo: ').lower()
        sexo_list.append(sexo)
        salario = float(input('Média salarial: R$ '))
        soma_salario += salario
        salario_list.append(salario)
        if sexo == 'f' and salario >= 5000:
            mulheres_maior_cinco_mil += 1
        os.system('cls')
        continue
    elif escolha == 2:
        if len(idade_list) >  0:
            print('Nenhuma pessoa, foi adicionada ainda! ')
            break
        else:
            media_salarial = soma_salario / len(salario_list)
            maior_idade = max(idade_list)
            menor_idade = min(idade_list)
        print('Informações do grupo')
        print(f'Média salarial: {media_salarial}')
        print(f'Maior idade: {maior_idade}')
        print(f'Menor idade: {menor_idade}')
        print(f'Mulheres que recebem apartir de R$ 5.000,00: {mulheres_maior_cinco_mil}')
    elif escolha == 3:
        os.system('cls')
        print('Finalizando programa. ')
        time.sleep(1)
        os.system('cls')
        print('Finalizando programa. ')
        time.sleep(1)
        os.system('cls')
        print('Finalizando programa. ')
        time.sleep(1)
        os.system('cls')
        break