# faça o computador pensar em um numero e o usuario tenta adivinhar qual é esse numero.
from random import choice
from time import sleep
cores = {
    'azul': '\033[34m',
    'verde': '\033[32m',
    'vermelho': '\033[31m',
    'branco': '\033[7m',
    'reset': '\033[m',
}
print('Estou pensando em um número entre 0 e 5. Tente advinhar...')
lista = [0, 1, 2, 3, 4, 5]
r = choice(lista)
n = int(input('Em qual numero o computador esta pensando? '))
print(cores['azul'],'Processando...')
sleep(1)
if r == n:
    print(cores['verde'], 'Parabéns você acertou')
else:
    print(cores['vermelho'], 'Errou, era o numero {}' .format(r))
