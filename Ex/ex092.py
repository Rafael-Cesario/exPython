#leia nome, ano de nascimento e carteira de trabalho, e cadastre-os com idade em um dicionário, se por acaso a ctps for diferente de zero, o dicionario recebera também o ano de contratação e o salário. Acrescente além da idade, com quantos anos a pessoa vai se aposentar.
print('\033[34m')
from datetime import date, datetime
pessoa = dict()
pessoa['Nome'] = str(input('Nome: '))
nascimento = int(input('Ano de nascimento: '))
pessoa['idade'] = date.today().year - nascimento
pessoa['ctps'] = int(input('Carteira de trabalho [Digite 0 caso não tenha]: '))
if pessoa['ctps'] > 0:
    pessoa['contratação'] = int(input('Ano de contratação: '))
    pessoa['salario'] = float(input('Salário: R$  '))
    pessoa['aposentadoria'] = pessoa['idade'] + ((pessoa['contratação'] + 35) - datetime.today().year)
print('-='*20)
for k,v in pessoa.items():
    print(f'{k}: {v}')