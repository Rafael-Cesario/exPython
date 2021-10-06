#verifique se o mesmo numero de parentes que abre também estão fechando
print('\033[34m')
expressão = str(input('Digite uma expressão com parenteses: '))
par = []
for l in expressão:
    if l == "(":
        par.append(l)
    elif l == ")":
        if len(par) == 0:
            par.append(l)
            break
        else:
            par.pop()
if len(par) == 0:
    print('Sua expressão é valida')
if len(par) > 0:
    print('Sua expressão é invalida')