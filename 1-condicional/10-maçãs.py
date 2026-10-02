import os
os.system('cls')

#ENTRADA.
maca = float(input('digite o numero de maçãs desejadas: '))

#PROCESSAMENTO.

valor1 = maca * 1.30
valor2 = maca * 1.0

#SAÍDA.

if maca <= 11:
    print('O valor é de:', 'R$', valor1)
    print('Sem desconto!')
elif maca >= 12:
    print('O valor é de:', 'R$', valor2)
    print('Com desconto!')