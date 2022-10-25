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

###########################################
if __name__=="__main__":

    s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
    s2 = CourseAttempt("Olivia C. Objective", "Introduction to Programming", 5)
    s3 = CourseAttempt("Peter Python", "Advanced Course in Programming", 2)

    for name in course_names([s1, s2, s3]):
        print(name)

#############################################
###  solucion profesor
#
# def names_of_students(course_names: list):
#     def student(attempt: CourseAttempt):
#         return attempt.student_name
 
#     return map(student, course_names)
#     # same using lambda function
#     # return map(lambda k: k.student_name, course_names)
 
# def course_names(course_names: list):
#     names = map(lambda k: k.course_name, course_names)
#     # remove duplicates by using a set
#     return sorted(list(set(names)))
 