# Write your solution here
from os import name


def add_student(students, name):

    if name not in students:
        students[name]= []


    # for student in students:
    #     if name not in student:
    #         student["nombre"] = name
    #         student["course"] = ""

    return students

######################################
def add_course(students, name, course):
    if course[1] != 0:  ### course[1] es la nota del curso y no puede ser 0
        curso = students[name]
        for nombre in curso:
            if course[0] in nombre:
                if course[1] > nombre[1]:
                    students[name][0]=course
                return students
            
        if name in students:
            students[name].append(course)

    return students

######################################
def print_student(students, name):

    if not name in students:
        print(f"{name}: no such person in the database")
    else:

        if students[name]==[]:
            print(f"{name}:")
            print(" no completed courses")
        else:
            print(f"{name}:")
            print(f" {len(students[name])} completed courses:")
            suma = 0
            avg = 0
            for i in range(len(students[name])):
                curso = students[name][i]
                suma += curso[1]
                print(f"  {curso[0]} {curso[1]}") # course[0]=nombre curso   course[1]= puntaje curso (grade)
            avg = suma/len(students[name])   
            print(f" average grade {avg}")

##############################
def summary(students):
    suma = 0
    claves = list(students.keys())
    tuplas = list(students.values())
    max_prom= 0
    max_cant = 0
    clave_max_prom =""
    clave_max_cant =""
    hacer = True
    i = 0
    x = 1

    while hacer:

        for tupla in tuplas:            
            suma = 0

            for element in tupla:
                suma = suma + element[1]

            cant = len(tupla)
            promedio = suma/cant

            if max_prom < promedio:
                max_prom = promedio
                clave_max_prom = claves[i]

            if max_cant < cant:
                max_cant = cant
                clave_max_cant = claves[i]
            i = i + 1

        x = x + 1
        if x > len(claves):
            hacer = False

    print("students", len(claves)) #cant alumnos
    print()

    print("most courses completed",str(max_cant),clave_max_cant)

    print("best average grade",str(max_prom),clave_max_prom)

######################################
if __name__=="__main__":

    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    add_course(students, "Peter", ("Introduction to Programming", 1))
    add_course(students, "Peter", ("Advanced Course in Programming", 1))
    add_course(students, "Eliza", ("Introduction to Programming", 5))
    add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    summary(students)

###########################################
##
##  solucion profesor
##
###################
# def add_student(students: dict, name: str):
#     students[name] = {}
 
# def print_student(students: dict, name: str):
#     if not name in students:
#         print(f"{name}: no such person in the database")
#         return
 
#     students_completed_courses = students[name]
 
#     print(f"{name}:")
#     if len(students_completed_courses) == 0:
#         print(" no completed courses")
#     else:
#         print(f" {len(students_completed_courses):} completed courses:")
#         sum = 0
#         for course, grade in students_completed_courses.items():
#             course_grade = grade[1]
#             print(f"  {course} {course_grade}")
#             sum += course_grade
 
#         print(f" average grade {sum/len(students_completed_courses):.1f}")
 
# def add_course(students: dict, name: str, completion: tuple):
#     students_completed_courses = students[name]
#     course_name = completion[0]
#     course_grade = completion[1]
 
#     # failed course is not recorded in the database
#     if course_grade==0:
#         return
 
#     # if previous grade is higher, new grade is not recorded in the database
#     if course_name in students_completed_courses:
#         if students_completed_courses[course_name][1] > course_grade:
#             return
 
#     students_completed_courses[course_name] = completion
 
# def summary(students: dict):
#     print(f"students {len(students)}")
#     most_courses_count = 0
#     best_avg_grade = 0
#     for name, completions in students.items():
#         if len(completions) > most_courses_count:
#             most_courses = name
#             most_courses_count = len(students[most_courses])
 
#         sum = 0
#         for course, grade in completions.items():
#             sum += grade[1]
 
#         if len(completions)==0:
#             avg = 0
#         else:
#             avg = sum/len(completions)
 
#         if avg>best_avg_grade:
#             best_avg_grade = avg
#             best = name
 
#     print(f"most courses completed {most_courses_count} {most_courses}")
#     print(f"best average grade {best_avg_grade:.1f} {best}")
# # Write your solution here