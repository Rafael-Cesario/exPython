# jo ken po
from random import choice
print('\033[1;33mVamos jogar Jo Ken Po')
j = str(input('Pedra, Papel ou Tesoura? \033[m')).strip()
c = choice(['pedra', 'papel' , 'tesoura'])
print('\033[34mComputador: {}\033[m'.format(c.capitalize()))
print('\033[33mJogador: {}\033[m'.format(j.capitalize()))
if j == c:
    print('\033[7mEMPATE\033[m')
else:
    if j == 'pedra':
        if c == 'papel':
            print('\033[1;31mVocê perdeu\033[m')
        else:
            print('\033[1;32mVocê venceu\033[m')
    elif j == 'papel':
        if c == 'tesoura':
            print('\033[1;31mVocê perdeu\033[m')
        else:
            print('\033[1;32mVocê venceu\033[m')
    else:
        if c == 'pedra':
            print('\033[1;31mVocê perdeu\033[m')
        else:
            print('\033[1;32mVocê venceu\033[m')
