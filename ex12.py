"""12. Faça um programa que solicite à pessoa usuária digitar um texto que será uma chave a ser pesquisada no seguinte dicionário: idades = {'Júlia': 16, 'Carol': 23, 'Alberto': 19, 'Roberta': 17}, armazenando o resultado do valor em uma variável. O código deve conter um tratamento de erro KeyError, imprimindo a informação 'Nome não encontrado', caso ocorra o erro; e imprimir o valor caso não ocorra nenhum.

Teste o programa com um nome presente em uma das chaves do dicionário e com um que não esteja no dicionário para verificar a mensagem de erro."""
import os
def limpar():
    os.system("clear")


idades = {'Júlia': 16, 'Carol': 23, 'Alberto': 19, 'Roberta': 17}

#main
limpar()
try:
    nome = input("Informe o nome da pessoa que deseja saber a idade: ")
    idade = idades[nome]
except KeyError:
    print("Nome não encontrado.")
else:
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
finally:
    print("Consulta concluída.")