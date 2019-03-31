from random import choice

palavras = ['Pé', 'Mão', 'Amor', 'Perna', 'Corpo', 'Luva']
preposicoes = ['de', 'da', 'do']
predicado = ['amor', 'quem?', 'vinil', 'cor', 'vento']

while True:
    palavraC = choice(palavras)
    preposicaoC = choice(preposicoes)
    predicadoC = choice(predicado)
    print(palavraC, preposicaoC, predicadoC)

