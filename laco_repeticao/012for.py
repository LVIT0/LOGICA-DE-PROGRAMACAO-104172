import os
os.system('cls')

nota = 0
vezes = 1

for i in range(4):
    nota += int(input(f'Digite sua {vezes}º nota: '))
    media = nota / 4
    vezes += 1
print(f'A média é: {media}')