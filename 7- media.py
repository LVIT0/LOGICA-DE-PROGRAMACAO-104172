import os
os.system('cls')

pn = int(input('digite a primeira nota: '))
sn = int(input('digite a segunda nota: '))
tn = int(input('digite a terceira nota: '))
media = (pn + sn + tn) / 3
# if (SE)

if media >= 7:
    print('Aprovado!')
#else (SENÃO)
else:
    print('Reprovado!.')

print('FIM DO ALGORITIMO')