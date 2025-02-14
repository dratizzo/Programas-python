l = int(input("Lagura do retângulo: ")) #Contabiliza as colunas
h = int(input("Altura do retângulo: ")) #Contabiliza as linhas

i = l
j = h

while h >= 1:
    while l != 0:
        if (h > 1 and h < j) and (l > 1 and l < i):
            print(" ", end = "")
        else:
            print("#", end = "")
        l = l - 1
    h = h -1
    print()
    l = i


