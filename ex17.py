"""7. Você foi contratado(a) como uma pessoa cientista de dados para auxiliar um laboratório que faz experimentos sobre o comportamento de uma cultura de fungos. O laboratório precisa avaliar constantemente a razão (divisão) entre os dados de pressão e temperatura do ambiente controlado recolhidos durante a experimentação para definir a melhor condição para os testes.

Para cumprir com a demanda, você precisa criar uma função divide_colunas que recebe os dados das colunas de pressão e temperatura (que vem no formato de listas) e gerar uma nova coluna com o resultado da divisão. Os parâmetros da função são as duas listas e você deve tratar dentro dela ao menos 2 tipos de exceções:

Verificar se as listas têm o mesmo tamanho (ValueError)
Verificar se existe alguma divisão por zero (ZeroDivisionError)
Para testar a função, vamos realizar a divisão entre duas listas de dados coletados no experimento, com os valores de pressão e temperatura do ambiente controlado.

Como teste, use os seguintes dados:"""
import os
def limpaTela():
    os.system("clear")

def divide_colunas(pressao: list, temperatura: list)-> list:
    if len(pressao) != len(temperatura):
        raise ValueError("As listas possuem tamanhos diferente e não podem ser correlacionadas.")
    if 0 in temperatura:
        raise ZeroDivisionError("Não pode ser realizada divisão por 0")
    razao = []
    for p, t in zip(pressao, temperatura):
        razao.append(p / t)
    return razao        

#Variaveis globais
media = []
#Dados sem exceção
pressoes = [100, 120, 140, 160, 180]
temperaturas = [20, 25, 30, 35, 40]

#Exceção de ZeroDivisionError
#pressoes = [60, 120, 140, 160, 180]
#temperaturas = [0, 25, 30, 35, 40]

#Exceção de ValueError
#pressoes = [100, 120, 140, 160]
#temperaturas = [20, 25, 30, 35, 40]

#main
try:
    media = divide_colunas(pressoes, temperaturas)
    print(f"Lista de pressões: {pressoes}")
    print(f"Lista de temperaturas: {temperaturas}")
    print([f"{m:.2f}" for m in media])
except Exception as e:
    print(f"Error: {e}")
    print(f"Tipo do erro: {type(e).__name__}")