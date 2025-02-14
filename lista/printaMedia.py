def getAverage(scores):
    average = 0
    for i in scores:
        average = average + i

    return average / len(scores)

print(getAverage([92, 88, 12, 77, 57, 100, 67, 38, 97, 89]))
print(getAverage([45, 87, 98, 100, 86, 94, 67, 88, 94, 95]))
