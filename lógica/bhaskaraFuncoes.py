import math

def calculaDelta(a, b, c):
    return b ** 2 - 4 * a * c

def calculaRaiz1(a, b, delta):
    return (-b + delta) / (2 * a)

def calculaRaiz2(a, b, delta):
    return (-b - delta) / (2 * a)

def main():
    a_digitado = float(input("Valor de A: "))
    b_digitado = float(input("Valor de B: "))
    c_digitado = float(input("Valor de C: "))
    imprime_raizes(a_digitado, b_digitado, c_digitado)

def imprime_raizes(a, b, c):
    delta = calculaDelta(a, b, c)
    if delta < 0:
        print("esta equação não possui raízes reais")

    elif delta == 0:
        raiz1 = calculaRaiz1(a, b, math.sqrt(delta))
        print("uma raiz real ", raiz1)

    else:
        raiz1 = calculaRaiz1(a, b, math.sqrt(delta))
        raiz2 = calculaRaiz2(a, b, math.sqrt(delta))
        print("Primeira raiz", raiz1)
        print("Segunda raiz", raiz2)
