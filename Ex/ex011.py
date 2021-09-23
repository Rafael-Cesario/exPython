#um prorama que leia a largura e a altura de uma parede em metros.
#calcule a sua área e quantidade de tinta necessária para pintá-la
#cada litro de tinta pinta uma área de 2m²

larg = float(input('Qual é a largura da sua parede: '))
alt = float(input('Qual é a altura da sua parede: '))
area = larg * alt
print('largura: ', larg)
print('Altura: ', alt)
print('Área: {}m²'.format(area))
tinta = area /2
print('Tinta necessária para pintar a parede: {}L'.format(tinta))