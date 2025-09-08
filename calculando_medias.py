import os

def limparTela():
    os.system('clear')

def media(lista):
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