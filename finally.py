"""Situação 14:
Você criou um código que lê um dicionário com as notas dos estudantes e quis retornar a lista de notas de um estudante.

Caso o(a) estudante não esteja matriculado(a) na classe devemos tratar a exceção para aparecer a mensagem "Estudante não matriculado(a) na turma" e se a exceção não for lançada devemos exibir a lista com as notas do(a) estudante. Um texto avisando que "A consulta foi encerrada!" deve ser exibido com ou sem a exceção ser lançada.

Vamos trabalhar nesse exemplo com a exceção Key Error que interromperá o processo desse pedaço do código.

Vamos testar esse tratamento?"""
import os
def limpa():
    os.system('clear')
def calcular_media(x):    
    res = sum(x) / len(x)
    return res

notas = {'João': [8.0, 9.0, 10.0], 'Maria': [9.0, 7.0, 6.0], 'José': [3.4, 7.0, 8.0], 'Cláudia': [5.5, 6.6, 8.0], 'Kaio': [5,5, 6, 3,2]}

try:
    aluno = input('Informe o nome do aluno: ')
    notas_aluno = notas[aluno]
    media = calcular_media(notas_aluno)
    if media >= 7:
        situacao = "APROVADO(A)"
    elif media >= 5:
        situacao = "EM RECUPERAÇÃO"
    else:
        situacao = "REPROVADO(A)"
    print(f"O(a) aluno(a) teve média de: {media:.1f} e está {situacao}")

except KeyError:
    print(f"O(a) aluno(a) {aluno} não está cadastrado(a).")

finally:
    print("CONSULTA CONCLUÍDA.")