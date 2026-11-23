from dataclasses import dataclass
import os
os.system('cls')


@dataclass
class Cliente:
    #Nome da variável : tipo de variáel
    nome: str
    idade: int


lista_clientes = []

lista_clientes.append(Cliente('Raphaely', 18))
lista_clientes.append(Cliente('Leandro', 17))

for cliente in lista_clientes:
    print(f'Nome: {cliente.nome}')
    print(f'Idade: {cliente.idade} anos')
    print('='*15)