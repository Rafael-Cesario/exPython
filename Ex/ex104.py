#deixe o usuario digitar apenas um numero
def lint(txt):
    while True:
        n = input(txt).strip()
        if n.isnumeric():
            return n
        else:
            print("\033[31mDigite um numero\033[m")


n = lint('Digite um numero: ')
print(f'Você digitou o numero {n}')