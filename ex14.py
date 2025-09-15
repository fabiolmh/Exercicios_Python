"""4. Crie uma função que recebe duas listas como parâmetros e agrupe os elementos um a um das listas, formando uma lista de tuplas de 3 elementos, no qual o primeiro e segundo elemento da tupla são os valores na posição i das listas e o terceiro elemento é a soma dos valores na posição i das listas.
A função deve conter um tratamento de erro indicando o tipo de erro gerado e retornar como resultado a lista de tuplas. Caso as listas enviadas como parâmetro tenham tamanhos diferentes, a função deve retornar um IndexError com a frase: 'A quantidade de elementos em cada lista é diferente.' Dados para testar a função:"""
import os
def limpa():
    os.system("clear")

def agrupar(x: list, y:list)-> list | None:
    if len(x) != len(y):
        raise IndexError("LISTAS POSSUEM TAMANHOS DIFERENTES.")
    z = []
    try:
        for i in range(len(x)):
            soma = x[i] + y[i]
            z.append([x[i], y[i], soma])
        return z
    except IndexError as e:
        print(f"Erro capturado no códgio principal: {e}")
        print(f"Tipo do erro: {type(e).__name__}")
        print(f"Mensagem: {e}")

#main
lista1 = [4,6,7,9,25]
lista2 = [-4,13,8,7,9]

try:
    resultado = agrupar(lista1, lista2)
    print(resultado)
except IndexError as e:
    print(f"Erro: {e}")