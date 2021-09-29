#leia o peso e a altura de uma pessoa. Calcule seu IMC e mostre seu status, de acordo com a tabela.
altura = float(input('Altura: '))
peso = float(input('peso: '))
imc = peso/(altura * altura)
if imc < 18.5:
    print('\033[31mVocê esta abaixo do peso\033[m')
elif imc <= 25:
    print('\033[34mVocê esta no peso ideal\033[m')
elif imc <= 30:
    print('\033[32mSobrepeso\033[m')
elif imc <= 40:
    print('\033[33mObesidade\033[m')
else:
    print('\033[35mObesidade Mórbida\033[m')