tamanho = int(input("Digite uma sequência de valores: "))

produto = 1
i = 0

while i < tamanho:
    valor = int(input("Digite um valor: "))
    produto = produto * valor
    i = i + 1

print("O produto é: ", produto)