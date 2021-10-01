#fatorial
v = int(input('Fatorial de: '))
c = v
f = 1
while c > 0:
    f *= c
    c -= 1
print('{}! = {}'.format(v,f))
