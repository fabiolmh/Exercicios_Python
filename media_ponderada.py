"""Nesta nova demanda, precisamos criar uma calculadora simples da média ponderada de notas de uma dada matéria. Vamos requisitar ao usuário a entrada das 3 notas (N1, N2, N3) do estudante e devolver a média ponderada deste estudante. Os pesos das notas são de, respectivamente 3, 2, 5.

Precisamos exibir um pequeno texto em que indicamos a média do(a) estudante.

Vamos resolver esse desafio?"""
n1 = float(input('Informe a nota 1: '))
n2 = float(input('Informe a nota 2: '))
n3 = float(input('Informe a nota 3: '))

ponderavel = lambda x, y, z: (x * 3 + y * 2 + z * 5) / 10

media = ponderavel(n1, n2, n3)

print(f'Média é igual a: {media}')