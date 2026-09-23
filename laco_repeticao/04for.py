import os
os.system('cls')

numero1 = 0.0

for i in range(1,6):
    numero = float(input(f'Digite o numero {i}: '))
    numero1 += numero
print(f'A soma dos noúmeros digitados é: {numero1}')