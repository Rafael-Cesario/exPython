#4 jogadores jogam um dado. Guarde esse resultado em um dicionario. No final coloque esse dicionario em ordem. Mostre o vencedor = aquele que tirou o maior numero.
print('\033[32m')
from random import randint
from operator import itemgetter
jogo = {
    'Jogador 1': randint(1, 6),
    'Jogador 2': randint(1, 6),
    'Jogador 3': randint(1, 6),
    'Jogador 4': randint(1, 6)}
print('Valores sorteados')
for k,v in jogo.items():
    print(f'{k}: {v}')
print('Ranking')
ranking = list()
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i,v in enumerate(ranking):
    print(f'{i+1}° Lugar {v[0]}: {v[1]}')