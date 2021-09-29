#calcule se um ano é bissexto
cores = {
    'azul': '\033[34m',
    'verde': '\033[32m',
    'vermelho': '\033[31m',
    'branco': '\033[7m',
    'reset': '\033[m',
}
from datetime import date
ano = int(input('Que ano gostaria de analisar? Coloque 0 para o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(cores['azul'], 'O ano {} é bissexto'.format(ano))
else:
    print(cores['branco'], 'O ano {} não é bissexto'.format(ano))