#Situação 7:
#Nesta nova demanda, precisamos gerar uma lista de tuplas com os nomes dos estudantes e o código ID de cada um para a plataforma de análise dos dados. A criação do código consiste em concatenar a primeira letra do nome do estudante a um número aleatório de 0 a 999. Os dados recebidos correspondem a uma lista dos nomes de cada estudante.
#Vamos resolver esse desafio?
#Para facilitar o nosso entendimento do processo vamos trabalhar com uma turma fictícia de 5 estudantes.
import random

def criaId():
    id = random.randint(0,4)
    return id

estudantes = ["João", "Maria", "José", "Cláudia", "Ana"]
ids = []
codigo = []

id = criaId()
for i in range(len(estudantes)):
    while (id in ids):
        id = criaId()
    ids.append(id)
    codigo.append([estudantes[i][0] + str(ids[i])])

for i in range(len(estudantes)):
    print(f'Nome do estudante: {estudantes[i]}')
    print(f'Código do estudante: {codigo[i]}')
    print('-' * 40)