# Write your solution here
from datetime import *
import csv

def cheaters():
    inicial_time=[]
    cheater=[]
    tres_horas=timedelta(hours=3)

    with open("start_times.csv") as my_file:
        for line in csv.reader(my_file, delimiter=";"):
            inicial_time.append(line)

    with open("submissions.csv") as my_file:
        ejer_time = []
        for line in csv.reader(my_file, delimiter=";"):
            ejer_time.append(line)

    for i in range(len(inicial_time)):
        nombre=inicial_time[0]
        hora=inicial_time[1]
        stu_ini = datetime(hora)
        inicial = timedelta(stu_ini)
        tiempo_ejer=ejer_time[3]
        duracion_ejer = datetime(tiempo_ejer)
        if duracion_ejer > inicial + tres_horas:
            cheater.append(inicial_time[0])

    return cheater


if __name__ == "__main__":
    cheaters()

# start_times.csv       name;hh:mm
# submissions.csv       name;task;points;hh:mm