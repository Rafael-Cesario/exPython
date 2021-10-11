#Criando Modulos
#melhor o ex107 criando um função dentro de um modula para formatar moedas
#melhore o ex108
#melhore o ex109
#melhore o ex110 criando pacotes
from pacotes import moedas, estilos

estilos.letra("Azul")
valor = float(input('Valor: '))
porcentagem = float(input('porcentagem: '))


moedas.resumo(valor, porcentagem, "Amarelo")
estilos.letra("Default")