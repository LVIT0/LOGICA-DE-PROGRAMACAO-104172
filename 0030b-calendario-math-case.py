import os
os.system('cls')

dia = int(input('Considere que Domingo é o dia 1 e Sábado é o dia 7\nDigite qual é o dia da semana:'))


match dia:
    case 1:
        print('Hoje é Domingo')
    case 2:
        print('Hoje é Segunda-Feira')
    case 3:
        print('Hoje é Terça-Feira')
    case 4:
        print('Hoje é Quarta-Feira')
    case 5:
        print('Hoje é Quinta-Feira')
    case 6:
        print('Hoje é Sexta-Feira')
    case 7:
        print('Hoje é Sábado')
    case _:
        print('Dia inválido.')


if dia >= 2 and dia <=6:
    print('Dia útil')
else:print('Final De Semana')