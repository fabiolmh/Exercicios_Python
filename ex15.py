"""15. Como desafio, você recebeu a tarefa de desenvolver um código que contabiliza as pontuações de estudantes de uma instituição de ensino de acordo com suas respostas num teste. Este código deve ser testado para um exemplo de 3 estudantes com uma lista de listas em que cada lista possui as respostas de 5 questões objetivas de cada estudante. Cada questão vale um ponto e as alternativas possíveis são A, B, C ou D.

Caso alguma alternativa em um dos testes não esteja entre as alternativas possíveis, você deve lançar um ValueError com a mensagem "A alternativa [alternativa] não é uma opção de alternativa válida". O cálculo das 3 notas só será realizado mediante as entradas com as alternativas A, B, C ou D em todos os testes. Se não for lançada a exceção, será exibida uma lista com as notas em cada teste.

Os dados para o teste do código são:

Gabarito da prova:
gabarito = ['D', 'A', 'B', 'C', 'A']
Copiar código
Abaixo temos 2 listas de listas que você pode usar como teste

Notas sem exceção:
testes_sem_ex = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'C', 'A'], ['D', 'B', 'A', 'C', 'A']]
Copiar código
Notas com exceção:
testes_com_ex = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'E', 'A'], ['D', 'B', 'A', 'C', 'A']]
Copiar código
Dica: Para verificar se uma entrada da lista não está entre as alternativas possíveis, use a estrutura lista[i] not in ['A','B','C','D']. Por exemplo, 1 not in [2,3,4]... Saída: True."""
import os
#Limpando a tela do usuário
def limpaTela():
    os.system("clear")

#Corrigindo cada prova
def corretor(resposta: list, gabarito: list)-> float:
    pontos = 0

    #aqui será feito a verificação das respostas, se estão ou não de acordo com as alternativas
    alternativas_validas = ['A', 'B', 'C', 'D']
    for alternativa in resposta:
        if alternativa not in alternativas_validas:
            raise ValueError(f"A alternativa {alternativa} não é uma opção válida")

    for i in range(len(gabarito)):    
        if resposta[i] == gabarito[i]:
            pontos = pontos + 2
    return pontos

#Variaveis globais do programa
gabarito = ['D', 'A', 'B', 'C', 'A']
provas = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'B', 'A'], ['D', 'B', 'A', 'C', 'A']]
estudantes = []
pontos = []

for i in range(len(provas)):
    aluno = input(f"Informe o nome do {i + 1} aluno: ")
    try:
        pontos = corretor(provas[i], gabarito)
        if pontos >= 7:
            situacao = "Aprovado(a)"
        elif pontos >= 6:
            situacao = "Em recuperação"
        else:
            situacao = "Reprovado(a)"
        estudantes.append([aluno, provas[i], pontos, situacao])

    except ValueError as e:
        print(f"Erro na prova do(a) aluno(a): {aluno}: {e}")
#Mostrar notas de cada aluno:
limpaTela()
for i in range(len(estudantes)):
    print(f"Aluno: {estudantes[i][0]}")
    print(f"Respostas: {estudantes[i][1]}")
    print(f"Pontos: {estudantes[i][2]}")
    print(f"Situação: {estudantes[i][3]}.")
    print("-"*25)