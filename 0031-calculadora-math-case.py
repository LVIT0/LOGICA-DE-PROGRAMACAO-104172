import os
os.system('cls')

print('Calculadora com Math-Case')

numero1 = float(input('Digite o primeiro numero: '))
operador = input('Digite o operador soma(+), produto(*), divisão(/), subtração(-), potência(**): ')
numero2 = float(input('Digite o segundo numero: '))

print(f'O primeiro número que você escolheu foi {numero1}')
print(f'O operador que você escolheu foi {operador}')
print(f'O segundo número que você escolheu foi {numero2}')

match operador:
    case '+':
        print(f'A soma é {numero1 + numero2}')
    case '*':
        print(f'O produto é {numero1 * numero2}')
    case '/':
        print(f'A divisão é {numero1 / numero2}')
    case '-':
        print(f'A subtração é {numero1 - numero2}')
    case '**':
        print(f'A potencia é {numero1 ** numero2}')
