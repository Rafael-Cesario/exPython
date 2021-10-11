#Criando Modulos
from Modulos import moeda, cor

cor.letra("Azul")
valor = float(input('Valor: '))
porcentagem = float(input('porcentagem: '))


cor.letra("Amarelo")
print(f'A metade de R${valor:.2f} é: R${moeda.metade(valor)} ')
print(f'O dobro de R${valor:.2f} é: R${moeda.dobro(valor):.2f}')
print(f'Aumentando {porcentagem:.2f}% de R${valor:.2f} temos: R${moeda.aumentar(valor, porcentagem):.2f}')
print(f'Diminuindo {porcentagem:.2f}% de R${valor:.2f} temos: R${moeda.diminuir(valor, porcentagem):.2f}')
cor.letra("Default")