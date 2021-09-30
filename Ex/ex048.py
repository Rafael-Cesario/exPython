#somar numeros
s = 0
con = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        con += 1
        s += c
print(s)
print(con)