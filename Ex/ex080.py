#leia alguns valores e adicione eles em ordem sem usar "sort()"
print('\033[34m')
valores = []
for c in range(0,5):
    n = (int(input('Digite um valor: ')))
    if c == 0 or n > valores[-1]:
        valores.append(n)
    else:
        pos = 0
        while pos < len(valores):
            if n <= valores[pos]:
                valores.insert(pos, n)
                break
            pos += 1
print(valores)