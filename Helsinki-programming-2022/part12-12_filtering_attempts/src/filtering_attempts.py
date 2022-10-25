class CourseAttempt:
    def __init__(self, student_name: str, course_name: str, grade: int):
        self.student_name = student_name
        self.course_name = course_name
        self.grade = grade

    def __str__(self):
        return f"{self.student_name}, grade for the course {self.course_name} {self.grade}"

def names_of_students(attempts: list):
    return map(lambda t: t.student_name, attempts) # map(funcion,lista)

def course_names(attempts: list):
    courses= sorted(map(lambda t: t.course_name, attempts))
    for x in range(len(courses)-1):
        if courses[x]==courses[x+1]: # nombres no repetidos
            courses.pop(x+1)
    return courses

def accepted(attempts: list):
    aceptados = filter(lambda attempt : attempt.grade >= 1, attempts)
    return aceptados

def attempts_with_grade(attempts: list, grade: int):
    return filter(lambda attempt : attempt.grade == grade, attempts)

def passed_students(attempts: list, course: str):
    lista = filter(lambda attempt : attempt.course_name == course and attempt.grade >= 1, attempts)
    names= sorted(map(lambda t: t.student_name, lista))
    return names

###########################################
if __name__=="__main__":

    s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
    s2 = CourseAttempt("Olivia C. Objective", "Introduction to AI", 5)
    s3 = CourseAttempt("Peter Python", "Introduction to AI", 0)
    s4 = CourseAttempt("Jack Java", "Introduction to AI", 3)

    for attempt in passed_students([s1, s2, s3, s4], "Introduction to AI"):
        print(attempt)

######################################
# solucion profesor
#
# def accepted(attempts: list):
#     return filter(lambda s: s.grade>0, attempts)
 
# def attempts_with_grade(attempts: list, grade: int):
#     return filter(lambda s: s.grade==grade, attempts)
 
# def passed_students(attempts: list, course: str):
#     course_attempts = filter(lambda s: s.course_name==course and s.grade>0, attempts)
#     course_students = map(lambda s: s.student_name, course_attempts)
#     return sorted(course_students)