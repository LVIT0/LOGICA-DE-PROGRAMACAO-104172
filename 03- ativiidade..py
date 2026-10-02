import os
os.system('cls')

numero1 = int(input('digite o primeiro número: '))
numero2 = int(input('digite o segundo número:  '))
numero3 = int(input('digite o terceiro número:  '))



maior_numero = max(numero1, numero2, numero3)
menor_numero = min(numero1, numero2,numero3)

print('Os números informados é:', numero1,',', numero2, 'e', numero3)
print('O maior_número é:', maior_numero)
print('A Menor número é:', menor_numero)