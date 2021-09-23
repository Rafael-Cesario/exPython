#faça um algoritmo que leia o preço de um produto
#mostre o seu novo valor com 5% de desconto
produto = float(input('Valor do produto: R$'))
desconto = produto*95/100
print('Com 5% de desconto seu produto custara R${}'.format(desconto))