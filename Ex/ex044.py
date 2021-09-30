# calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento
p = float(input('Valor do produto: '))
c = str(input('Forma de pagamento\n1 - Dinheiro\n2 - Cartão\n: '))
if c == '1' or c.lower == 'dinheiro':
    print('Seu produto tem 10% de desconto e será {}'.format(p - (p * 10 / 100)))
elif c == '2' or c.lower == 'cartão':
    x = int(input('Em quantas vezes gostaria de pagar: '))
    if x == 1:
        print('Seu produto tem 5% de desconto e saira por R$ {:.2f}'.format(
            p - (p * 5 / 100)))
    elif x == 2:
        print('2x de R$ {}'.format(p / 2))
        print('Seu produto vai sair por R$', p)
    elif x >= 3:
        print('{}x de {}'.format(x, p / x))
        print('Seu produto vai sofrer juros e vai sair por R$ {:.2f}'.format(p + (p *20 / 100)))
else:
    print('Digite uma das opções acima')
