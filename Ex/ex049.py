# Tabuada
print('\n')
v = int(input('Digite um numero para ver sua tabuada: '))
for c in range(1,11):
    print('{:2} X {:2} = {:2}'.format(c, v, c * v))
print('\n')