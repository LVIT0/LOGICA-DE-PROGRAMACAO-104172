import os
os.system('cls')

def soma_numeros(numero1, numero2):
    resultado = numero1 + numero2
    return resultado
def subtracao_numeros(numero1, numero2):
    resultado = numero1 - numero2
    return resultado
def divisao_numeros(numero1, numero2):
    if numero2 == 0:
        return 'Atenção! Divisão por zero'
    return numero1 / numero2
def multiplicacao_numeros(numero1, numero2):
    resultado = numero1 * numero2
    return resultado
print('='*15)
print('  CALCULADORA')
print('='*15)
numero1 = int(input('\nDigite o primeiro número: '))
numero2 = int(input('\nDigite o segudo número: '))

print(f'\nO resultado da soma é: {soma_numeros(numero1, numero2)}')
print(f'\nO resultado da subtração é: {subtracao_numeros(numero1, numero2)}')
print(f'\nO resultado da divisão é: {divisao_numeros(numero1, numero2)}')
print(f'\nO resultado da multiplicação é: {multiplicacao_numeros(numero1, numero2)}')