x = int(input("Tamanho da sequência: "))

somaPar = 0

while x != 0:
    y = int(input("Número: "))
    
    if y % 2 == 0:
        somaPar = somaPar + y

    x -= 1

print(somaPar)
