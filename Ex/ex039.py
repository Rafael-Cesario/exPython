# leia o ano de nascimento de um jovem e diga de acordo com sua idade
# se ele ainda vai se alista no exercito
# se é a hora de se alista
# se já passou da hora
# seu programa também devera mostrar o tempo que falta ou que passou do prazo

from datetime import date
nascimento = int(input('Em que ano você nasceu? '))
hoje = date.today().year
idade = hoje - nascimento
if idade < 18:
    print('\033[34mFalta {} anos para você se alistar'.format(18-idade))
elif idade == 18:
    print('\033[35mÉ hora de se alistar')
else:
    print('\033[31mJá passou {} anos do seu alistamento'.format(idade - 18))
