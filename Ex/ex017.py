#Calcule e mostre o comprimento da hipotenusa
from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
#h1 = (co ** 2 + ca ** 2) ** (1/2)
h1 = hypot(ca, co)
print('A hipotenusa vai medir {:.2f}'.format(h1))
