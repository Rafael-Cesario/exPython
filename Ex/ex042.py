#calcule os valores e diga se é possivel formar um triângulo, mostre que tipo de triângulo é
v1 = float(input('Valor 1: '))
v2 = float(input('Valor 2: '))
v3 = float(input('Valor 3: '))
if v1 < v2 + v3 and v2 < v1 + v3 and v3 < v1 + v2:
    print('\033[32mÉ possivel formar um triângulo\033[m')
    if v1 == v2 and v1 == v3:
        print('\033[44mSeu triângulo é um triângulo Equilátero\033[m')
    elif v1 == v2 or v1 == v3 or v2 == v3:
        print('\033[43mSeu triângulo é um triângulo Isósceles\033[m')
    else:
        print('\033[7mSeu triângulo é um triângulo Escaleno\033[m')
else:
    print('\033[31mNão é possivel formar um triângulo\033[m')
