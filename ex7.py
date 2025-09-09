"""7. Você recebeu uma demanda para tratar 2 listas com os nomes e sobrenomes de cada estudante concatenando-as para apresentar seus nomes completos na forma Nome Sobrenome. As listas são:
nomes = [joão, MaRia, JOSÉ]
sobrenomes = [SILVA, souza, Tavares]

O texto exibido ao fim deve ser parecido com:
Nome completo: Ana Silva"""
#Função que padroniza a escrita dos nomes (1ª maiuscula e restante minusculas)
def primeiraMaiuscula(nome, sobrenome):
    nomeTransformado = nome.title()
    sobrenomeTransformado = sobrenome.title()
    return f"{nomeTransformado} {sobrenomeTransformado}"

nomes = ["joão", "MaRia", "JOSÉ"]
sobrenomes = ["SILVA", "souza", "Tavares"]

nomeCompleto = list(map(primeiraMaiuscula, nomes, sobrenomes))

for i in nomeCompleto:
    print(f"Nome completo: {i}")