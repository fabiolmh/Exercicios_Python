"""6. Para atender a uma demanda de uma instituição de ensino para a análise do desempenho de seus(suas) estudantes, você precisa criar uma função que receba uma lista de 4 notas e retorne:

maior nota
menor nota
média
situação (Aprovado(a) ou Reprovado(a))
Para testar o comportamento da função, os dados podem ser exibidos em um texto:
O(a) estudante obteve uma média de [media], com a sua maior nota de [maior] pontos e a menor nota de [menor] pontos e foi [situacao] """
import os

###FUNÇÕES
#Função limpar tela
def limpar():
    os.system('clear')

#Função que calcula a média de acordo com as notas repassadas
def calculandoMedia(notas):
    res = sum(notas) / len(notas)
    return res

#Função que realizada a saída da situação do aluno
def situacao(media, aluno):
    if (media >= 7):
        print(f'{aluno} tirou média {media:.1f} e está APROVADO.')
    elif (media >= 5):
        print(f'{aluno} tirou média {media:.1f} e está EM RECUPERAÇÃO.')
    else:
        print(f'{aluno} tirou média {media:.1f} e está REPROVADO.')

#VARIAVEIS GLOBAIS
notas = []
maiorNota = 0
menorNota = 0
media = 0

#Parte visual do código
limpar()
aluno = str(input('Informe o nome do aluno: '))
limpar()
for i in range(1,5):
    nota = float(input(f'Informe a {i}ª nota: '))
    notas.append(nota)
limpar()

#chamadas de funções
media = calculandoMedia(notas)
menorNota = min(notas)
maiorNota = max(notas)

situacao(media,aluno)