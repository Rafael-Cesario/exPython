# aprove o emprestimo para a compra de uma casa
# o programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Valor da casa: '))
salario = float(input('Salário: '))
anos = int(input('Quantos anos pretende pagar: '))
negado = salario * 30 / 100
mensal = casa / (anos*12)
print('\033[34mO valor mensal da casa é {:.2f}'.format(mensal))
if mensal > negado:
    print('\033[31mInfelizmente isso excede 30% do seu salário')
else:
    print('\033[34mParabéns pelo sua compra')
