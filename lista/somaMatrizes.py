'''

Recebe duas matrizes e devolve uma matriz que representa a soma
entre elas caso tenham dimensões iguais. Caso contrário,
devolve False.
'''

def soma_matrizes(m1, m2):
    lista_soma = []
    matriz = []

    # len(m1) resulta no número de linhas(listas)
    # len(m1[0] resulta no número de colunas
    if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
        return False

        # Percorre as linhas
    for i in range(len(m1)):

            # Percorre as colunas somando
        for j in range(len(m1[0])):
            valor = m1[i][j] + m2[i][j]
            lista_soma.append(valor)

        matriz.append(lista_soma)
        
    return print(lista_soma)
