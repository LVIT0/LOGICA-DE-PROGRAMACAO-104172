import os
os.system('cls')

numero1 = int(input('digite o primeiro numero: '))
numero2 = int(input('digite o segundo numero:  '))

media = (numero1 + numero2) / 2
soma = (numero1 + numero2)
produto = (numero1 * numero2)
maior_numero = max(numero1, numero2)
menor_numero = min(numero1, numero2)

if numero1 == numero2:
    print('Os números são iguais')

else: print('Os números são diferentes')

print('A Média é:', media)
print('A soma é:', soma)
print('O produto é:', produto)
print('O maior_numero é:', maior_numero)
print('A Menor numero é:', menor_numero)