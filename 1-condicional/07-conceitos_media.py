import os
os.system
#ENTRADA.

nome = str(input('Digite seu nome: '))
pn = int(input('Digite a primeira nota: '))
sn = int(input('Digite a segunda nota: '))
print('O nome é: ', nome)
media = (pn + sn) / 2

if media >= 9:
    print('Aprovado pelo conceito (A)')
elif 9 > media >= 7.5:
    print('Aprovado pelo conceito (B)')
elif 7.5 > media >= 6:
    print('Aprovado pelo conceito (C)')

elif 6 > media >= 4:
    print('Reprovado pelo conceito (D)')

else:
    print('Reprovado pelo conceito (E)')
