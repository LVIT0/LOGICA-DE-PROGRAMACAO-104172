from dataclasses import dataclass
import os
os.system('cls')

@dataclass

class Cliente:
    nome: str
    telefone: str
    email: str

lista_clientes = []

dados_do_cliente = Cliente(
    nome= input('Digie seu nome: '),
    telefone= (input('Digite seu número de telefone: ')),
    email= input('Digite seu E-mail: ')
)

lista_clientes.append(dados_do_cliente)

for cliente in lista_clientes:
    print('='*35)
    print(f'Nome: {cliente.nome}')
    print(f'Telefone: {cliente.telefone}')
    print(f'E-mail: {cliente.email}')
    print('='*35)