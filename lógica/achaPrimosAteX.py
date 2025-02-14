def n_primos(x):
    qtd_primos = 1
    i = 3
    while i <= x:
        if primo(i) == True:
            qtd_primos += 1
        i += 1

    return qtd_primos
        
def primo(n):
    fator = 2
    while n % fator != 0 and fator < n/2:
        fator += 1
    if n % fator == 0:
        return False
    else:
        return True
