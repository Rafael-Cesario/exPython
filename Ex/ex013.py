#faça um algoritmo que leia o salário de um funcionario
#Mostre seu novo sálario com 15% de aumento.
salario = float(input('Qual o seu salário? R$'))
aumento = float(input('Aumento em porcentagem: '))
novoSalario = salario + (salario*aumento/100)
print('Com um aumento de {:.0f}% seu salário vai passar a ser de R${:.2f}'.format(aumento,novoSalario))