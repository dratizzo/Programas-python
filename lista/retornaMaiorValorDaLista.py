def maior_elemento(lista):
    maiorValor = lista[0]
    for i in lista:
        if i > maiorValor:
            maiorValor = i

    return maiorValor
        
