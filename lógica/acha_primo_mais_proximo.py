def maior_primo(x):
    while x > 1:
        contaDivisoes = 0
        i = 2  # Começamos com i = 2, pois todo número é divisível por 1
        
        while i * i <= x:  # Verificamos até a raiz quadrada de x
            if x % i == 0:
                contaDivisoes += 1
            i += 1

        # Se não tiver divisores além de 1 e ele mesmo, é primo
        if contaDivisoes == 0:
            return x
        
        x -= 1  # Se não for primo, tenta o próximo número menor

a = int(input("Número inteiro maior ou igual a 2: "))
print(maior_primo(a))