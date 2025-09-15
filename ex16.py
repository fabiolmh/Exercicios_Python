"""16. Você está trabalhando com processamento de linguagem natural (NLP) e, dessa vez, sua líder requisitou que você criasse um trecho de código que recebe uma lista com as palavras separadas de uma frase gerada pelo ChatGPT.

Você precisa criar uma função que avalia cada palavra desse texto e verificar se o tratamento para retirar os símbolos de pontuação (',' '.', '!' e '?') foi realizado. Caso contrário, será lançada uma exceção do tipo ValueError apontando o 1º caso em que foi detectado o uso de uma pontuação por meio da frase "O texto apresenta pontuações na palavra "[palavra]".". Essa demanda é voltada para a análise do padrão de frases geradas pela inteligência artificial."""

import os
def limparTela():
  os.system("clear")

def avaliacao_palavras(lista: list)-> None:
    caracteres_invalidos = [",", "!", "?", "."]
    for palavra in lista:
        for char in caracteres_invalidos:
            if char in palavra:
                raise ValueError(f"O texto apresenta pontuações na palavra: {palavra}")

#main
limparTela()
lista_tratada = ['Python', 'é', 'uma', 'linguagem', 'de', 'programação', 'poderosa', 'versátil',
                  'e', 'fácil', 'de', 'aprender', 'utilizada', 'em', 'diversos', 'campos', 'desde',
                  'análise', 'de', 'dados', 'até', 'inteligência', 'artificial']

lista_nao_tratada = ['Python', 'é', 'uma', 'linguagem', 'de', 'programação', 'poderosa,', 'versátil',
                  'e', 'fácil,', 'de', 'aprender', 'utilizada', 'em', 'diversos', 'campos,', 'desde',
                  'análise', 'de', 'dados', 'até', 'inteligência', 'artificial!']

#teste com a lista tratada:
try:
    avaliacao_palavras(lista_tratada)
    print("Lista tratada: OK. Nenhuma pontuação encontrada.")
except ValueError as e:
    print(f"Erro ao avaliar a lista tratada: {e}")

print("-"*60)

try:
    avaliacao_palavras(lista_nao_tratada)
    print("Lista não tratada: Ok. Nenhuma pontuação encontrada.")
except ValueError as e:
    print(f"Erro ao avaliar a lista tratada: {e}")