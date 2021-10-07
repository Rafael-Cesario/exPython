#sortear 6 numeros entre 1 e 60 e salvar em lista
from random import randint
j = []
jogos = []
jogadas = int(input('Quantos sorteios devo fazer: '))
while True:
    while True:
        v = randint(1, 60)
        if v not in j:
            j.append(v)
        j.sort()
        if len(j) == 6:
            break
    jogos.append(j[:])
    j.clear()
    if len(jogos) == jogadas:
        break
for c in range(0,jogadas) :
    print(f'Jogo {c + 1}: {jogos[c]}')