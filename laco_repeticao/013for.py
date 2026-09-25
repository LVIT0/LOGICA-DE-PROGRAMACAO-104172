import os
os.system('cls')

vezes = 1
nota = 0
QUANTIDADE = 3

for i in range(QUANTIDADE):
    nota += float(input(f'Digite sua {vezes}º nota: '))
    vezes += 1
    media = nota / 3
if media >= 7:
    print(f'A média é {media:.1f}')
    print('Aprovado!')
elif media >= 4:
    print(f'A média é {media:.1f}')
    print('Recuperação!')
elif media < 4:
    print(f'A média é {media:.1f}')
    print('Reprovado!')