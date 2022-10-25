# write your solution here
if True:
    # this is never executed
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exam_points = input("Exam points: ")
else:
    # hard-coded input
    student_info = "students1.csv"
#   id;first;last
#   12345678;peter;pythons

    exercise_data = "exercises1.csv"
#   id;e1;e2;e3;e4;e5;e6;e7
#   12345678;4;1;1;4;5;2;4

    exam_points = "exam_points1.csv"
#   id;e1;e2;e3
#   12345678;4;1;4
######################################

names = {}

with open(student_info) as new_file:
    for line in new_file:
        parts = line.split(';')
        if parts[0] == "id":
            continue
        names[parts[0]] = parts[1].strip() + " " + parts[2].strip()

exercises = {}

with open(exercise_data) as new_file:
    for line in new_file:
        parts = line.split(';')
        if parts[0] == "id":
            continue
        exercises[parts[0]] = int(parts[1])+int(parts[2])+int(parts[3])+int(parts[4])+int(parts[5])+int(parts[6])+int(parts[7])

exams = {}

with open(exam_points) as new_file:
    for line in new_file:
        parts = line.split(';')
        if parts[0] == "id":
            continue
        exams[parts[0]] = int(parts[1])+int(parts[2])+int(parts[3])


# print encabezados 30col, 10col, 10col, 10col, 10col, 10col
print("name                          exec_nbr  exec_pts. exm_pts.  tot_pts.  grade")

for id, name in names.items():
    if id in exercises:
        total_exerc=exercises[id]
    if id in exams:
        total_exams=exams[id]
    exec_pts = int(total_exerc/4)
    total_grade = total_exams + exec_pts

    if total_grade >= 0 and total_grade <= 14:
        grade = 0
    elif total_grade >= 15 and total_grade <= 17:
        grade = 1
    elif total_grade >= 18 and total_grade <= 20:
        grade = 2
    elif total_grade >= 21 and total_grade <= 23:
        grade = 3
    elif total_grade >= 24 and total_grade <= 27:
        grade = 4
    elif total_grade >= 28:
        grade = 5

    print(f"{name:30}{total_exerc:<10}{exec_pts:<10}{total_exams:<10}{total_grade:<10}{grade:<10} ")

