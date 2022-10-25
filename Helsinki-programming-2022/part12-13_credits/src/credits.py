from functools import reduce

class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"
##################################
def sum_of_all_credits(attempts):
    credits=[]
    for attempt in attempts:
        credits.append(attempt.credits)
    return reduce(lambda reduced_sum, item: reduced_sum + item, credits, 0)

def sum_of_passed_credits(attempts):
    aceptados = filter(lambda attempt : attempt.grade >= 1, attempts)
    credits=[]
    for attempt in aceptados:
        credits.append(attempt.credits)
    return reduce(lambda reduced_sum, item: reduced_sum + item, credits, 0)

def average(attempts):
    aceptados = filter(lambda attempt : attempt.grade >= 1, attempts)
    grades=[]
    for attempt in aceptados:
        grades.append(attempt.grade)
    suma=reduce(lambda reduced_sum, item: reduced_sum + item, grades, 0)
    return suma/len(grades)

#################################################3    
# Write your solution
if __name__=="__main__":

    s1 = CourseAttempt("Introduction to Programming", 5, 5)
    s2 = CourseAttempt("Advanced Course in Programming", 0, 4)
    s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
    ag = average([s1, s2, s3])
    print(ag)

############################################
# solucion profesor
#
# def credit_summer(cr_sum, attempt):
#     return cr_sum + attempt.credits
 
# def sum_of_all_credits(attempts: list):
#     return reduce(credit_summer, attempts, 0)
 
# def sum_of_passed_credits(attempts: list):
#     accepted = filter(lambda s: s.grade > 0, attempts)
#     return reduce(credit_summer, accepted, 0)
 
# def average(attempts: list):
#     def grade_summer(cr_sum, attempt):
#         return cr_sum + attempt.grade 
 
#     accepted = list(filter(lambda s: s.grade > 0, attempts))
#     sum_of_grades = reduce(grade_summer, accepted, 0)
 
#     return sum_of_grades / len(accepted)
# Write your solution