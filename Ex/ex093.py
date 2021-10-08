#leia o nome do jogador e quantas partidas ele jogou, depois leia a quantidade de gols feitos em cada partida, salve o total de gols
print('\033[34m')
jogador = dict()
jogador['nome'] = str(input('Nome: '))
jogador['partidas'] = int(input('Total de partidas: '))
jogador['gols'] = list()
jogador['total'] = 0
for c in range(0, jogador['partidas']):
    jogador['gols'].append(int(input(f'Quantidade de gols na {c+1}° partida: ')))
for i, v in enumerate(jogador['gols']):
    jogador['total'] += v
print('-='*20)
print(jogador)
print('-='*20)
for k, v in jogador.items():
    print(f'{k}: {v}')
print('-='*20)
print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'>>> Na partida {i+1}: {v} Gols')
print('-='*20)