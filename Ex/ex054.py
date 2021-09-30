#quantas pessoas já são adultas
from datetime import date
maior = 0
menor = 0
for idade in range(0,7):
    nascimento = int(input('Em que ano você nasceu? '))
    idade = date.today().year - nascimento
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print('{} pessoas são de maior e {} pessoas são de menor'.format(maior, menor))
