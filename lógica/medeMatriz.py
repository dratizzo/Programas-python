def dimensoes(matriz):
    '''
    Length of X is the number of rows.
    Length of X[0] is the length of the first row, aka number of columns.
    '''
    row = len(matriz)
    col = len(matriz[0])

    print(str(row) + "X" + str(col))
