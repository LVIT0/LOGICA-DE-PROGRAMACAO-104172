import time
import os
os.system('cls')


ano_atual = time.localtime().tm_year
def idade(ano_de_nascimento):
    resultado = ano_atual - ano_de_nascimento
    return resultado

ano_de_nascimento = int(input('Digite o ano de nascimento: '))
resultado = idade(ano_de_nascimento)

print(f'Ano atual: {ano_atual}.\nIdade: {resultado} anos')
