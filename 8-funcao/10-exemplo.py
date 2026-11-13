import os
os.system('cls')

def numero_impar_ou_par(numero):
    if numero %2 != 0:
        return 'O número é impar'
    else:
        return 'O número é par'

print('='*24)
print('NÚMEROS IMPARES OU PARES')
print('='*24)
numero = int(input('\nDigite um número: '))
resultado = numero_impar_ou_par(numero)

print(resultado)