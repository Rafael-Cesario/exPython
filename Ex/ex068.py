#Par ou impar com o PC
from random import randint
print('Eae vamos jogar par ou impar')
cont = 0
while True:
    jogador = str(input('Par ou impar? ')).strip().upper(), int(input('Diga um numero: '))
    computador = randint(0,10)
    total = jogador[1] + computador
    if total % 2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'IMPAR'
    if resultado == jogador[0]:
        print(f'\033[32mVoce jogou {jogador[1]} e o computador {computador}. total {total} = {resultado}')
        print('Parabéns você venceu\033[m')
        cont += 1
    else:
        print(f'\033[31mVoce jogou {jogador[1]} e o computador {computador}. total {total} = {resultado}')
        print('GAME OVER\nQue pena você perdeu\033[m')
        print(f'Total de vítorias: {cont}')
        break

    
    
