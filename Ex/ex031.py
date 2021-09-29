#pergunte a distancia de uma viagem em km
#calcule o preço da passagem cobrando 0,50 por km para viagens até 200km e 0,45 para viagens mais longas
distancia = float(input('Digite a distancia da sua viagem: '))
if distancia <= 200:
    valor = distancia * 0.50
    print('O valor da sua viagem é: R${}'.format(valor))
else:
    valor = distancia * 0.45
    print('O valor da sua viagem é: R${}'.format(valor))