# calcule o valor do aumento de um funcionario
# if salario > 1250 aumento 10%
# if salario <= 1250 aumento 15%
cores = {
    'azul': '\033[34m',
    'verde': '\033[32m',
    'vermelho': '\033[31m',
    'branco': '\033[7m',
    'reset': '\033[m',
}
salario = int(input('Digite o valor do seu salário: '))
if salario <= 1250:
    reajuste = (salario * 15 / 100) + salario
else:
    reajuste = (salario * 10 / 100) + salario
print('Seu salário era de {}R${}{} com aumento ficou {}R${}{}'.format(cores['vermelho'], salario, cores['reset'], cores['azul'], reajuste, cores['reset']))
