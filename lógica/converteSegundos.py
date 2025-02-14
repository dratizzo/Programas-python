segundosTotal = int(input("Quantos segundos? "))

dia = segundosTotal // 86400
hora = segundosTotal % 86400 // 3600
segundos_restantes = segundosTotal % 86400 % 3600
minutos = segundos_restantes // 60
segundos = segundos_restantes % 60

print(dia, "dias,", hora, "horas,", minutos, "minutos e", segundos, "segundos.")

