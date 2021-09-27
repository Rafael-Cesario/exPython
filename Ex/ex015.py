#Calcule o preço de um carro que custa R$60 por dia alugado e R$0.15 por km rodado
dias = int(input('Por quantos dias o carro foi alugado: '))
km = float(input('Quantos km o carro rodou? '))
valor = (dias*60) + (km*0.15)
print('valor: R${:.2f}'.format(valor))