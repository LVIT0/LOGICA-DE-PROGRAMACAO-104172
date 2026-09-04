import os
os.system('cls')

nota = int(input('Digite uma nota '))

if nota >= 0 and nota <= 10:
    print('A nota é:', nota)
else:
    print('A nota tem que ser entre: 0 e 10.')