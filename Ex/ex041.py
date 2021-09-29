#mostre a categoria de acordo com a idade
idade = int(input('Idade: '))
print('\033[34m')
print('='*30)
if idade < 10:
    print('Sua categoria é MIRIM')
elif idade < 15:
    print('Sua categoria é INFANTIL')
elif idade < 20:
    print('Sua categoria é JUNIOR')
elif idade == 20:
    print('Sua categoria é SÊNIOR')
else:
    print('Sua categoria é MASTER')
print('='*30)
print('\033[m')
