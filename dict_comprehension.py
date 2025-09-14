"""Agora, a nossa demanda consiste em gerar um dicionário a partir da lista de listas que criamos na Situação 10 para passar para a pessoa responsável por construir as tabelas para a análise dos dados.

As chaves do nosso dicionário serão as colunas identificando o tipo de dado
Os valores serão as listas com os dados correspondentes àquela chave.
Vamos resolver esse desafio?

Para facilitar o nosso entendimento do processo vamos trabalhar com uma turma fictícia de 5 estudantes.

Dica: Utilize o formato"""

lista_completa = [[('João', 'J720'), ('Maria', 'M205'), ('José', 'J371'), ('Cláudia', 'C546'), ('Ana', 'A347')],
                  [[8.0, 9.0, 10.0], [9.0, 7.0, 6.0], [3.4, 7.0, 7.0], [5.5, 6.6, 8.0], [6.0, 10.0, 9.5]],
                  [9.0, 7.3, 5.8, 6.7, 8.5],
                  ['Aprovado', 'Aprovado', 'Reprovado', 'Aprovado', 'Aprovado']]

coluna = ["Notas", "Media", "Situação"]

cadastro = {coluna[i] : lista_completa[i+1] for i in range(len(coluna))}
estudantes = []

print(cadastro)