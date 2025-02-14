cont = int(input("Tamanho da sequência: "))

somaPar = somaImpar = 0

while cont > 0:
    num = int(input("Número: "))
    if num % 2 == 0:
        somaPar = somaPar + 1
    else:
        somaImpar = somaImpar + 1

    cont -= 1

print(somaPar)
print(somaImpar)
