#aprimore o desafio 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
#leia o nome do jogador e quantas partidas ele jogou, depois leia a quantidade de gols feitos em cada partida, salve o total de gols
print('\033[34m')
jogador = dict()
jogadores = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome: ')).capitalize()
    partidas = int(input('Total de partidas: '))
    jogador['gols'] = list()
    jogador['total'] = 0
    for c in range(0, partidas):
        jogador['gols'].append(int(input(f'Quantidade de gols na {c+1}° partida: ')))
    for i, v in enumerate(jogador['gols']):
        jogador['total'] += v
    jogadores.append(jogador.copy())
    c = str(input("Continuar[S/N]: ")).upper()
    if c == "N":
        break
print('-='*30)
print(f'{"N°":<5} {"Nome":<15} {"Gols":<15} {"Total":<15}')
for i,j in enumerate(jogadores):
    print(f'{i+1:<5}',end=' ')
    for v in j.values():
        print(f'{str(v):<15}',end=' ')
    print()
while True:
    while True:
        b = int(input("Mostrar dados de qual jogador(999 stop): "))
        if b <= len(jogadores) or b == 999:
            break
    if b == 999:
        break
    print(f'Dados : {jogadores[b-1]["nome"]}')
    for i,g in enumerate(jogadores[b-1]['gols']):
        print(f'Partida {i+1}: {g} Gols')