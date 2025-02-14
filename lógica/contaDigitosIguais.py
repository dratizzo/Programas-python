num = int(input("Número inteiro: "))
dig = int(input("Dígito: "))

soma = 0
cont = salva = num

while salva > 0:
    if salva % 10 == dig:
        soma = soma + 1

    salva = salva // 10

print("O dígito", dig, "ocorre", soma, "vezes em", num)
