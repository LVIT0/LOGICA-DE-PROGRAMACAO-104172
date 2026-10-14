import os
os.system('cls')

vetor_numero = []
QUANTIDADE_DE_NUMEROS = 5
for i in range(QUANTIDADE_DE_NUMEROS):
    vetor_numero.append(int(input(f'Digite o {i + 1}º número:  ')))
    
    
    maior_numero = max(vetor_numero)
    menor_numero = min(vetor_numero)
    
print(f'Maior número: {maior_numero}')
print(f'Menor número: {menor_numero}')