import os
os.system('cls')

idade = int(input('digite sua idade: '))


if idade >= 65:
    print('Não são obrigados a votar')

elif idade >= 18:
    print("Voto obrigatório")

elif idade == 17:
    print("Voto opcional")

elif idade <= 16:
    print("Não podem votar")