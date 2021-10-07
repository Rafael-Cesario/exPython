#leia o nome e a média de um aluno. Quarde a situação em um dicionário. No final mostre na tela
print('\033[32m')
aluno = dict()
nome = str(input('Nome: ')).capitalize()
média = float(input('Média: '))
if média >= 7:
    apr = "Aprovado"
else:
    apr = "Reprovado"
aluno['nome'] = nome
aluno['média'] = média
aluno['apr'] = apr
print(f'Nome: {aluno["nome"]}')
print(f'Média: {aluno["média"]}')
print(f'Situação: {aluno["apr"]}')
