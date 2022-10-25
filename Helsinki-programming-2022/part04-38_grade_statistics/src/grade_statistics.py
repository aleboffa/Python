# Write your solution here
def input_from_user():
    students=[]
    while True:
        text = input("Exam points and exercises completed: ")
        if text == "":
            break
        text = text.split()
        students.append(text)
    return students

def Statistics(students):
    expoints=0
    student=[]
    grade0=0
    grade1=0
    grade2=0
    grade3=0
    grade4=0
    grade5=0
    points_avg=0
    porcentaje=0

    for student in students:
        student[0]=int(student[0])
        expoints=int(student[1])/10
        student[1]=int(expoints) #parte entera y redondeo para abajo
        if student[0] < 10 or (student[0] + student[1]) <= 14:
            grade0 = grade0 + 1      
        else:
            if student[0] + student[1] <= 17:
                grade1 = grade1 + 1
            elif student[0] + student[1] <= 20:
                grade2 = grade2 + 1
            elif student[0] + student[1] <= 23:
                grade3 = grade3 + 1
            elif student[0] + student[1] <= 27:
                grade4 = grade4 + 1
            elif student[0] + student[1] <= 30:
                grade5 = grade5 + 1
        points_avg = points_avg + student[0] + student[1]
    points_avg = points_avg / len(students)
    porcentaje = (grade1 + grade2 + grade3 + grade4 + grade5) / len(students) * 100

    print("Statistics: ")
    print("Points average:", f"{points_avg:.1f}")
    print("Pass percentage:", f"{porcentaje:.1f}")
    print("Grade distribution:")
    print("5:", grade5*"*")
    print("4:", grade4*"*") 
    print("3:", grade3*"*")        
    print("2:", grade2*"*")
    print("1:", grade1*"*")
    print("0:", grade0*"*")

# your main function goes here
def main():
    inputs = input_from_user()
    Statistics(inputs)

# run the main function
main()