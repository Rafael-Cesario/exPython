#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.
metros = float(input('Digite um valor em metros: '))
c = metros * 100
m = metros * 1000
print('{}m em:' .format(metros))
print('centimetros: {:.0f}cm' .format(c))
print('milimetros: {:.0f}mm' .format(m))
