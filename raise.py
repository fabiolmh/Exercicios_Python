"""Situação 14:
Você criou um código que lê um dicionário com as notas dos estudantes e quis retornar a lista de notas de um estudante.

Caso o(a) estudante não esteja matriculado(a) na classe devemos tratar a exceção para aparecer a mensagem "Estudante não matriculado(a) na turma" e se a exceção não for lançada devemos exibir a lista com as notas do(a) estudante. Um texto avisando que "A consulta foi encerrada!" deve ser exibido com ou sem a exceção ser lançada.

Vamos trabalhar nesse exemplo com a exceção Key Error que interromperá o processo desse pedaço do código.

Vamos testar esse tratamento?"""

def media(lista: list=[0]) -> float:
    calculo = sum(lista) / len(lista)

    
    if len(lista) > 4:
        raise ValueError("A lista não pode conter mais de 4 notas.")

    return calculo
try:
    notas = [4, 9, 10, 10]
    resultado = media(notas)
except ValueError:
    print("A lista não pode conter mais de 4 notas.")
except TypeError:
    print("Um dos valores passados nas notas não é númerico.")
else:
    print(f"{resultado:.1f}")