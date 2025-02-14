#Calcula fatorial em sequência

def fatorial(x):
    soma = 1
    while x > 1:
        soma = x * soma
        x = x - 1

    print(soma)

x = 1

while x >= 0:
    x = int(input("Digite um valor para ser calculado o fatorial - 0 encerrar: "))
    fatorial(x)
