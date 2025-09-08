"""5. Você foi contratado(a) como cientista de dados de uma associação de skate. Para analisar as notas recebidas de skatistas em algumas competições ao longo do ano, você precisa criar um código que calcula a pontuação dos(as) atletas. Para isso, o seu código deve receber 5 notas digitadas pelas pessoas juradas.

Para calcular a pontuação de um(a) skatista, você precisa eliminar a maior e a menor pontuação dentre as 5 notas e tirar a média das 3 notas que sobraram. Retorne a média para apresentar o texto:

"Nota da manobra: [media]"""
import os
#Funções
#Limpar tela
def limpar():
    os.system('clear')

def media(lista):
    res = sum(lista) / len(lista)
    return res

#Variaveis globais
notas = []
apresentacaoNotas = []

#Inicio de interação programa com o usuário
limpar()
#Usuario informa as notas
for i in range(1, 6):
    n = float(input(f'Informe a {i}ª nota: '))
    notas.append(n)
    apresentacaoNotas.append(n)

menor = min(notas)
maior = max(notas)
notas.remove(menor)
notas.remove(maior)
limpar()
res = media(notas)

print(f'Notas da manobra: ${apresentacaoNotas}')
print(f'Média da Manobra [NOTA FINAL]: {res:.1f}')