# List comprehension
# [ expressão for item in lista]
"""Situação 8:
Recebemos a demanda de criar uma lista com as médias dos estudantes da lista de listas que criamos na Situação 6. Lembrando que cada lista da lista de listas possui as três notas de cada estudante.

Vamos resolver esse desafio?

Dica: Utilize o formato:"""
import os
def limparTela():
    os.system('clear')

def media(nota):
    media = sum(nota) / len(nota)
    return media

notas = [[8.0, 9.0, 10.0], [9.0, 7.0, 6.0], [3.4, 7.0, 7.0], [5.5, 6.6, 8.0], [6.0, 10.0, 9.5]]
medias = []

medias = [media(nota) for nota in notas]

limparTela()
for i in range(len(notas)):
    print('-' * 50)
    print(f'Id do Aluno: 00{i}')
    print(f'Notas: {notas[i]}')
    (f'Média : {medias[i]}')
    situacao = 'Aprovado' if medias[i] >= 7 else 'Reprovado'
    print(f'Aluno 00{i} foi {situacao}')
  