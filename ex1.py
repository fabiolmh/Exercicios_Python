"""1. Escreva um código que lê a lista abaixo e faça:
lista = [16, 14, 63, 65, 17, 99, 70, 11, 20, 48, 79, 32, 17, 89, 12, 25, 66]
- A leitura do tamanho da lista
- A leitura do maior e menor valor
- A soma dos valores da lista
"""
import os

def limpar():
    os.system('clear')


lista = [16, 14, 63, 65, 17, 9, 70, 11, 20, 48, 49, 32, 17, 8, 12, 25, 98]

limpar()

tamanho = len(lista)
maior = lista[0]
soma = 0
for i in lista:
    soma = soma + i
    if i > maior:
        maior = i

print(f'Tamanho da lista: {tamanho}')
print(f'Maior valor da lista: {maior}')
print(f'Soma de todos os valores da lista: {soma}')