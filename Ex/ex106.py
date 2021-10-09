#Sistema interativo de ajuda em Python
#Digite FIM para parar
cores = {
    "0" : "\033[m",
    "34" : "\033[34m",
    "32": "\033[32m"
}
def ajuda(c):
    print(cores["34"])
    help(c)
    print(cores["0"])

def titulo(txt, c):
    print(cores[f"{c}"],end=' ')
    print('-'* (len(txt) + 4))
    print(f'  {txt}')
    print('-'* (len(txt) + 4))
    print(cores[f"{c}"],end=' ')

while True:
    titulo("Sistema de ajuda PyHelp", 32)
    c = str(input("  Digite um comando: "))
    if c.upper() == "FIM":
        break
    ajuda(c)
titulo("FIM", 34)