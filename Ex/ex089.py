#leia o nome e duas notas de varios alunos, salve em uma lista e mostre um boletim
print('\033[34m')
alunos = list()
while True:
    nome = str(input('Nome: ')).capitalize()
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    m = round((n1 + n2) / 2)
    alunos.append([nome, [n1, n2], m])
    c = str(input('Continuar [S/N]: '))
    if c in "Nn":
        break
print('-='*20)
print(f'{"N°":<3}{"Nome":<20}{"Média":<6}')
print('-='*20)
for i,v in enumerate(alunos):
    print(f'{i + 1:<3}{alunos[i][0]:<20}{alunos[i][2]:<6}')
while True:
    aluno = int(input('Digite o numero do aluno para ver suas notas[999 stop]: ')) - 1
    if aluno == 998:
        break
    print(f'{alunos[aluno][0]}: {alunos[aluno][1][0]}/{alunos[aluno][1][1]}')
