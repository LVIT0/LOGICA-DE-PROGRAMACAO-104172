import os
os.system('cls')

altura = float(input('Digite sua altura: '))
sexo = str(input('Coloque (M) para masculino e (F) para feminino: '))


match sexo:
    case "m":
        m = (72.7 * altura) - 58
        print(f'Seu peso ideal é: {m:.2f}')
    case 'f':
        f = (62.1 * altura) - 44.7
        print(f'Seu peso ideal é: , {f:.2}')