def fatorial(x):
    produto = 1
    while x != 0:
        produto = produto * x
        x = x - 1
    return produto

def coeficiente_binomial(n, k):
    return fatorial(n) / (fatorial(k) * (fatorial(n - k)))

#n = int(input("Digite um número: "))
#k = int(input("Digite a classe: "))

#coeficiente = coeficiente_binomial(n, k)

#print(coeficiente)
