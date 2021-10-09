#faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
def escreva(txt):
    b = len(txt) + 6
    print(f'\033[34m-'*b)
    print(f'   {txt}')
    print(f'-'*b, '\033[m')


a = str(input('Titulo: ')).upper()
escreva(a)