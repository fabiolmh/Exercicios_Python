""" Situação 3:
Recebemos uma nova demanda, desta vez, de calcular a média de um estudante a partir de uma lista e retornar tanto a média quanto a situação do estudante ("Aprovado(a)" se a nota for maior ou igual a 6.0, caso contrário, será "Reprovado(a)").
Além disso, precisamos exibir um pequeno texto em que indicamos a média do(a) estudante e qual a situação. Os dados recebidos correspondem a uma lista contendo apenas as notas de um estudante em uma dada matéria.
Vamos resolver esse desafio?
Para facilitar o nosso entendimento do processo vamos aplicar as notas de apenas um estudante, mas você pode testar outros casos para treinar."""
import os

def limparTela():
    os.system('clear')

def media(lista :list) -> float: #A nossa funcao recebe um dado do tipo LISTA e retorna um FLOAT
    calculo = sum(lista) / len(lista)
    return calculo

notas = []
limparTela()
qtdNotas = int(input('Informe a quantidade de notas para que seja realizado o calculo da média: '))
limparTela()

for i in range(1, qtdNotas + 1):
    nota = float(input(f'Informe a {i}ª nota: '))
    notas.append(nota)
    limparTela()

resultado = media(notas)

if (resultado >= 7):
    print(f'Média: {resultado:.1f}')
    print(f'Aluno APROVADO.')
elif (resultado >= 5):
    print(f'Média: {resultado:.1f}')
    print(f"Aluno EM RECUPERAÇÃO.")
else:
    print(f'Média: {resultado:.1f}')
    print('Aluno REPROVADO.')