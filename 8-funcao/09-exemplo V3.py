import os
os.system('cls')

# Função com parãetros e com retorno

def calcular_notas(nota1, nota2):
    media = (nota1 + nota2) / 2
    return media

def verificar_notas(media):
    if media >= 7:
        return'APROVADO!'

    else:
        return'REPROVADO!'

print('= SOLICITANDO NOTAS =')

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))


media = calcular_notas(nota1, nota2)
situacao = verificar_notas(media)
print('= EXIBINDO NOTAS =')
print(f'Média: {media}')
print(f'Resultado: {situacao}')
