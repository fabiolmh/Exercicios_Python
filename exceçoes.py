"""Situação 13:
Você criou um código que lê um dicionário com as notas dos estudantes e quis retornar a lista de notas de um estudante.

Caso o(a) estudante não esteja matriculado(a) na classe devemos tratar a exceção para aparecer a mensagem "Estudante não matriculado(a) na turma" e se a exceção não for lançada devemos exibir a lista com as notas do(a) estudante.

Vamos trabalhar nesse exemplo com a exceção Key Error que interromperá o processo desse pedaço do código.

Vamos testar esse tratamento?"""

import os
def limpar():
    os.system('clear')

def media(x):
    md = sum(x) / len(x)
    return md

notas_turma = {
    'João': [8.0, 9.0, 10.0],
    'Maria': [9.0, 7.0, 6.0],
    'José': [3.4, 7.0, 7.0],
    'Cláudia': [5.5, 6.6, 8.0],
    'Ana': [6.0, 10.0, 9.5]
}

try:
    escolha = input('Escolha o nome do aluno que deseja verificar a média: ')
    notas_do_aluno = notas_turma[escolha]
except KeyError:
    print('Aluno não cadastrado.')
else:
    limpar()
    resultado = media(notas_do_aluno)
    print(f'O(a) aluno(a) {escolha} tirou média {resultado:.1f}')