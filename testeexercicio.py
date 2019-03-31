def ficha(jogador, gols):
    if jogador.strip() == None or jogador.strip() == '':
        jogador = '<desconhecido>'
    else:
        jogador = jogador
    if gols.strip() == None or gols.strip() == '':
        gols = '0'
    elif gols.isnumeric():
        gols = gols
    else:
        gols = '0'
    return jogador, gols

jogador_ficha = input('Diga o nome do jogador: ')
gols_ficha = input('Diga os gols que o jogador fez: ')

jog, gols_finalizado = ficha(jogador_ficha, gols_ficha)
print('O nome do jogador é {}.'.format(jog))
print('O(s) gol(s) que ele fez foram {} gols.'.format(gols_finalizado))
