"""8. Como cientista de dados em um time de futebol, você precisa implementar novas formas de coleta de dados sobre o desempenho de jogadores e do time como um todo. Sua primeira ação é criar uma forma de calcular a pontuação do time no campeonato nacional a partir dos dados de gols marcados e sofridos em cada jogo.

Escreva uma função chamada calcula_pontos que recebe como parâmetros duas listas de números inteiros, representando os gols marcados e sofridos pelo time em cada partida do campeonato. A função deve retornar a pontuação do time e o aproveitamento em percentual, levando em consideração que a vitória vale 3 pontos, o empate vale 1 ponto e a derrota 0 pontos.

Observação: se a quantidade de gols marcados numa partida for maior que a de sofridos, o time venceu. Caso seja igual, o time empatou e se for menor, o time perdeu. Para calcular o aproveitamento devemos fazer a razão entre a pontuação do time pela pontuação máxima que ele poderia receber.

Para teste, utilize as seguintes listas de gols marcados e sofridos:

gols_marcados = [2, 1, 3, 1, 0]
gols_sofridos = [1, 2, 2, 1, 3]"""
import os

def logo():
    print('='*120)
    print(' ' * 50, "CAMPEONATO BRASILEIRO", ' ' * 50)
    print('='*120)

def limpar():
    os.system('clear')
    logo()

def calcula_pontos(golsMarcados, golsSofridos):
    if (golsMarcados > golsSofridos):
        pontos = 3 
    elif (golsMarcados == golsSofridos):
        pontos = 1
    else:
        pontos = 0
    return pontos

limpar()
jogos = int(input("Informe a quantidade de jogos que teremos no campeonato: "))
time = str(input('Informe o nome do time do seu coração: '))
golsFavoraveis = 0
golsContra = 0
pontos = 0

for i in range(1, jogos + 1):
    limpar()
    print(f"=== {time} X ADVERSÁRIO {i} ===")
    golsFavoraveis = int(input("QUANTOS GOLS FEITOS: "))
    golsContra = int(input("QUANTOS GOLS SOFRIDOS: "))
    pontos = pontos + calcula_pontos(golsFavoraveis, golsContra)

aproveitamento = (pontos / (jogos * 3)) * 100

limpar()
print(f"Time: {time}")
print(f"Jogos: {jogos}")
print(f"Pontos no campeonato: {pontos}")
print(f"Aproveitamento: {aproveitamento:.1f}%")