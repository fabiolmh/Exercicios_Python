"""3. Crie a função que leia a lista abaixo e retorne uma nova lista com os múltiplos de 3:
[97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]
Utilize o return na função e salve a nova lista na variável mult_3.
"""
import os

#Essa função apenas limpa a tela do terminal
def limpar():
    os.system('clear')

#Função que define os múltiplos de 3
def multiplosTres(lista):
    mult_3 = []
    for i in lista:
        if (i % 3 == 0):
            mult_3.append(i)
    return mult_3


lista = [97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]
multiplos_3 = multiplosTres(lista)
print(f'Os multiplos de 3 são: {multiplos_3}')