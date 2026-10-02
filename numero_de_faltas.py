import os
os.system('cls')

media = float(input('Digite sua média: '))
faltas = int(input('Digite o numero de faltas: '))


media1 = 7
faltas1 = 40

if media >= media1  and faltas <= faltas1:
    print('Aprovado!')
else:
    print('Reprovado!')