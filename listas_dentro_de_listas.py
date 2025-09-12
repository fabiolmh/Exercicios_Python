import os

def limparTela():
    os.system('clear')

def media(nota):
    media = sum(nota) / len(nota)
    return media

notas_turma = ['João', 8.0, 9.0, 10.0, 'Maria', 9.0, 7.0, 6.0, 'José', 3.4, 7.0, 7.0, 'Cláudia', 5.5, 6.6, 8.0, 'Ana', 6.0, 10.0, 9.5]

nomes = []
notasJuntas = []
notas = []
medias = []

#Separando a lista principal em duas listas: nomes e notas gerais
for i in range(len(notas_turma)):
    if i % 4 == 0:
        nomes.append(notas_turma[i])
    else:
        notasJuntas.append(notas_turma[i])


#Separando as notas individualmente
for i in range(0,len(notasJuntas),3):
    grupo = [notasJuntas[i], notasJuntas[i +1], notasJuntas[i+2]]
    notas.append(grupo)
    medias.append(media(grupo))

    limparTela()

#Apresentando as notas e as médias
for i in range (len(notas)):
    print(f'Aluno: {nomes[i]}.')
    print(f'Notas: {notas[i]}.')
    print(f'Média bimestral: {medias[i]:.1f}')
    print('-' * 100)