import os
os.system
#ENTRADA.

altura = float(input('digite sua altura: '))
peso = float(input('digite seu peso: '))

#PROCESSAMENTO.

imc = peso / (altura * 2)
print(f'Seu IMC é de:, {imc:.2f}')

#SAÍDA.

if imc <= 18.5:
    print('Abaixo do peso. ')
elif imc <= 24.9:
    print('Peso ideal.(Parabéns!)')
elif imc <= 29.9:
    print('Levemente acima do peso.')
elif imc <= 34.9:
    print('Obesidade grau 1.')

elif imc <= 39.9:
    print('Obesidade grau 2 (severa).')

elif imc >= 40:
    print('Obesidade grau 3 (mórbida).')