"""2. Escreva uma função que gere a tabuada de um número inteiro de 1 a 10, de acordo com a escolha da pessoa usuária.:"""
import os
def tabuada(n):
    print(f'TABUADA DE {n}:')
    for i in range(1, 10):
        res = n + i
        print(f'{n} + {i} = {res}')

def limpar():
    os.system('clear')

numero = int(input("Informe um número inteiro: "))
limpar()
tabuada(numero)
