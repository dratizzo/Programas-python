import math

a = float(input("Valor de A: "))
b = float(input("Valor de B: "))
c = float(input("Valor de C: "))

delta = b ** 2 - 4 * a * c

if delta < 0:
    print("esta equação não possui raízes reais")

elif delta == 0:
    delta = math.sqrt(delta)
    
    raiz1 = (-b + delta) / (2 * a)
    
    print("uma raiz real ", raiz1)

elif delta > 0:
    delta = math.sqrt(delta)
    
    raiz1 = (-b + delta) / (2 * a)
    raiz2 = (-b - delta) / (2 * a)

    print("Primeira raiz", raiz1)
    print("Segunda raiz", raiz2)