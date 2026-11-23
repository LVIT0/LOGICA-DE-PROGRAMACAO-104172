from dataclasses import dataclass
import os
os.system('cls')

print('='*17)
print('DADOS PACIENTE...')
print('='*17)

@dataclass
class Paciente:
    nome: str
    idade: str
    telefone: str
    endereco: str

    def mostrar_dados(self):
        print('='*15)
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade} anos')
        print(f'Telefone: {self.telefone}')
        print(f'Endereço: {self.endereco}')
        print('='*15)

    def nome_e_idade(self):
        print('='*15)
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade} anos')
        print('='*15)

    def nome_e_telefone(self):
        print('='*15)
        print(f'Nome: {self.nome}')
        print(f'Telefone: {self.telefone}')
        print('='*15)

lista_paciente = []

dados_do_paciente = Paciente(
    nome= input('Digite seu nome: '),
    idade= (input('Digite sua idade: ')),
    telefone= (input('Digite seu número de telefone: ')),
    endereco= input('Digite seu endereço: ')
)

lista_paciente.append(dados_do_paciente)
print('MOSTRAR DADOS')
for paciente in lista_paciente:
    paciente.mostrar_dados()
print('NOME E IDADE')
for paciente in lista_paciente:
    paciente.nome_e_idade()
print('NOME E TELEFONE')
for paciente in lista_paciente:
    paciente.nome_e_telefone()

