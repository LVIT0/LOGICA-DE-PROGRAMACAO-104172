import os
os.system('cls')

def produto_inflacionado(preco):
    if preco < 100:
        resultado = preco + (preco * 0.10)
    elif  preco >= 100:
        resultado = preco + (preco* 0.20)
        return preco

print(F'O preço final do produto é: R$ {produto_inflacionado}:.2f')