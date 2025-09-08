"""Recebemos mais uma demanda, desta vez, para criar uma pequena função que pudesse adicionar qualitativo (pontuação extra) às notas do trimestre dos estudantes da turma que ganhou a gincana de programação promovida pela escola. Cada estudante receberá o qualitativo de 0.5 acrescido à média.

Os dados recebidos correspondem a uma lista contendo as notas de alguns estudantes e uma variável com o qualitativo recebido.

Vamos resolver esse desafio?

Para facilitar o nosso entendimento do processo vamos aplicar o qualitativo às notas de 5 estudantes, mas você pode testar outros casos para treinar."""
notas = [6.0, 7.0, 9.0, 5.5, 8.0]
qualitativo = 0.5

notas_atualizadas = list(map(lambda x: x + qualitativo, notas))
print(notas_atualizadas)