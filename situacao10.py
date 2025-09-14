"""Situação 10:
Recebemos duas demandas a respeito desse projeto com as notas dos estudantes:

Criar uma lista da situação dos estudantes em que caso se sua média seja maior ou igual a 6 receberá o valor "Aprovado" e caso contrário receberá o valor "Reprovado".
Gerar uma lista de listas com:
Lista de tuplas com o nome dos estudantes e seus códigos
Lista de listas com as notas de cada estudante
Lista com as médias de cada estudante
Lista da situação dos estudantes de acordo com as médias
Os dados que utilizaremos são os mesmos que geramos nas situações anteriores (nomes, notas, medias).

Vamos resolver esse desafio?

Para seguirmos o processo, vou deixar logo abaixo as estruturas de dados que já produzimos."""
import os

def limparTela():
    os.system('clear')

def calcularMedia(nota):
    """Calcula a média de uma lista de notas."""
    return sum(nota) / len(nota)

nomes = [('João', 'J720'), ('Maria', 'M205'), ('José', 'J371'), ('Cláudia', 'C546'), ('Ana', 'A347')]
notas = [[8.0, 9.0, 10.0], [9.0, 7.0, 6.0], [3.4, 7.0, 7.0], [5.5, 6.6, 8.0], [6.0, 10.0, 9.5]]

limparTela()

# 1. Cria a lista de médias e de situações com a condição correta (>= 6)
medias = [calcularMedia(nota) for nota in notas]
situacao = ["Aprovado(a)" if m >= 6 else "Reprovado(a)" for m in medias]

# 2. Cria a lista de listas conforme a segunda demanda
relatorio_estudantes = [
    nomes,
    notas,
    medias,
    situacao
]

# Imprime o relatório completo para verificação
print("Relatório completo de estudantes:")
print(f"Lista de Nomes e Códigos: {relatorio_estudantes[0]}")
print(f"Lista de Notas: {relatorio_estudantes[1]}")
print(f"Lista de Médias: {[f'{m:.2f}' for m in relatorio_estudantes[2]]}")
print(f"Lista de Situações: {relatorio_estudantes[3]}")

print("\n" + "-" * 50 + "\n")

# Loop para imprimir os resultados individuais
for i in range(len(notas)):
    print(f"Aluno(a): {nomes[i][0]}")
    print(f"Média: {medias[i]:.1f}")
    print(f"Situação: {situacao[i]}")
    print("-" * 50)