#soma digitos do número

numero = int(input("Digite um número: "))

soma = 0
while numero > 0:
    digito = numero % 10

    soma = digito + soma

    numero = numero // 10

print(soma)
