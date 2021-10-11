#Entrada de dados monetários
from pacotes import moedas, estilos, dados

estilos.letra("Azul")
valor = dados.leiaDinheiro()
porcentagem = float(input('porcentagem: '))


moedas.resumo(valor, porcentagem, "Amarelo")
estilos.letra("Default")