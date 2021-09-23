#crie um programa que mostre o seu dobro e o seu triplo
n = int(input('Digite um numero: '))
dobro = n * 2 
triplo = n * 3
raiz = n ** (1/2)
print('O numero que você digitou é: {}' .format(n))
print('O dobro dele é: {}' .format(dobro))
print('O triplo dele é: {}' .format(triplo))
print('A raiz quadrada dele é: {:.2f}' .format(raiz))