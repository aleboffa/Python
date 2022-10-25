# Write your solution here
import urllib.request
import json
from math import *

def retrieve_all():

    my_request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
    datos=json.loads(my_request.read())
    lista=[]
    for dato in datos:
        if dato["enabled"] == True:
            fullnombre = dato["fullName"]
            nombre = dato["name"]
            anio = dato["year"]
            sumexe = sum(dato["exercises"])
            linea = (fullnombre, nombre, anio, sumexe)
            lista.append(linea)
   
    return lista

def retrieve_course(course_name: str):
    pagina=f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats"
    my_request = urllib.request.urlopen(pagina)
    datos=json.loads(my_request.read())
    dict={}
    cant_students=0
    hours=0
    exercises=0
    weeks=len(datos)
    for dato in datos:
        tempo = datos[dato]
        stu=tempo["students"]
        if int(stu) > cant_students:
            cant_students=tempo["students"]
        hours=hours+tempo["hour_total"]
        exercises=exercises+tempo["exercise_total"]
        
    hours_average=trunc(hours/cant_students)
    exercises_average=trunc(exercises/cant_students)
    dict={
        'weeks': weeks,
        'students': cant_students,
        'hours': hours,
        'hours_average': hours_average,
        'exercises': exercises,
        'exercises_average': exercises_average
        }
   
    return dict    


if __name__ == "__main__":

    retrieve_all()

    retrieve_course("docker2019")