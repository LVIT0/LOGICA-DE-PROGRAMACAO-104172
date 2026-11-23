from dataclasses import dataclass
import os
os.system('cls')

@dataclass

class Cliente:
    nome: str
    telefone: str
    email: str

    def mostrar_dados(self):
        print('='*35)
        print(f'Nome: {self.nome}')
        print(f'Telefone: {self.telefone}')
        print(f'E-mail: {self.email}')
        print('='*35)

    def email_marketing(self):
        print('='*35)
        print(f'Nome: {self.nome}')
        print(f'E-mail: {self.email}')
        print('='*35)

    def whatsapp_marketing(self):
        print('='*15)
        print(f'Nome: {self.nome}')
        print(f'Telefone: {self.telefone}')
        print('='*15)

lista_clientes = []

for i in range(2):
    dados_do_cliente = Cliente(
        nome= input('Digie seu nome: '),
        telefone= (input('Digite seu número de telefone: ')),
        email= input('Digite seu E-mail: ')
    )

lista_clientes.append(dados_do_cliente)
print('MOSTRAR DADOS')
for cliente in lista_clientes:
    cliente.mostrar_dados()
print('DADOS E-MAIL')
for cliente in lista_clientes:
    cliente.email_marketing()
print('DADOS WHATSAPP')
for cliente in lista_clientes:
    cliente.whatsapp_marketing()