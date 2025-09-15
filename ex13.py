"""13. Crie uma função que recebe uma lista como parâmetro e converta todos os valores da lista para float. A função deve conter um tratamento de erro indicando o tipo de erro gerado e retornar a lista caso não tenha ocorrido nenhum erro. Por fim, deve ter a cláusula finally para imprimir o texto: 'Fim da execução da função'."""
import os

def limpa():
    os.system("clear")

def transformando_em_float(lista: list)-> list | None:
    try:
        lista_float = [float(item) for item in lista]
        return lista_float
    except (ValueError, TypeError) as e:
        print("Há itens na lista que não podem ser transformados em números.")
        return None
    finally:
        print("Fim da execução da função")

#main
limpa()
listaDeNumeros = []
escolha = int(input("Informe quantos itens deseja implementar na lista: "))
for i in range(escolha):
    item = input(f"Informe o {i + 1}º número: ")
    listaDeNumeros.append(item)

nova_lista = transformando_em_float(listaDeNumeros)

if nova_lista is not None:
    limpa()
    print(f"Lista original: {listaDeNumeros}")
    print(f"Lista convertida: {nova_lista}")