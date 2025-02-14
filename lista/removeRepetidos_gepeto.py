def remove_repetidos(lista):
    resultado = []
    for i in lista:
        if i not in resultado:  # Verifica se o valor já foi adicionado
            resultado.append(i)  # Adiciona o valor à nova lista

    resultado.sort()  # Ordena a lista final
    return resultado
