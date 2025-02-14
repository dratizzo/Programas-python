lista = [2, 4, 2, 2, 3, 3, 1]

for i in range(len(lista)):
    j = i + 1
    while j < len(lista):
        if lista[i] == lista[j]:
            del lista[j]
        else:
            j += 1

lista.sort()
print(lista)
