import os
os.system('cls')

def numero_positivo_ou_negativo(numero):
    if numero > 0:
        return 'O número é positivo'
    elif numero < 0:
        return 'O número é negativo'
    else:
        return 'O número é neutro'
print('='*30)
print('NÚMEROS POSITIVOS OU NEGATIVOS')
print('='*30)
numero = int(input('\nDigite um número: '))
resultado = numero_positivo_ou_negativo(numero)

print(resultado)