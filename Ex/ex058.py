#Tente adivinhar o numero que o computador esta pensando
print('\n')
from random import randint
print('Tente adivinhar em qual numero o computador está pensando')
jogador = int(input('Diga um numero de 0 a 10: '))
computador = randint(0,10)
errou = 0
while jogador != computador:
    print('\033[31mQue pena você errou\033[m')
    errou += 1
    jogador = int(input('Diga outro numero: '))
print('\033[32mVocê venceu parabéns\033[m')
print('Numero de tentativas: {}'.format(errou + 1))
print('\n')