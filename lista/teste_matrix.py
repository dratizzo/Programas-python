tempValores = [[0], [0, 0, 0, 0, 0, 0], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                           [30, 27, 33, 26, 25 ,29], [-15, -12, 0, 20, 30]]


i = 0

while i < (len(tempValores)):
    teste_pontual(tempValores[i], [i])
    i += 1
