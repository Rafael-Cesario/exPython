# crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
media = (n1 + n2) / 2
print('Sua nota é', media)
if media < 5:
    print('\033[31mREPROVADO\033[m')
elif media < 6.9:
    print('\033[1;33mRECUPERAÇÃO\033[m')
else:
    print('\033[1;94mAPROVADO\033[m')